#!/usr/bin/env python3
"""QAFindings: conservative descriptive summaries, never automatic publication.

Python 3.10+; standard library only. Real records and outputs must stay outside
this repository. Demo observations are completely synthetic and not findings.
This is a limited validator for this project's schema, not a JSON Schema engine.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "instruments" / "survey.schema.json").read_text(encoding="utf-8"))
ITEMS = tuple(SCHEMA["x-frequency-items"])
CORE = tuple(f"P{i:02d}" for i in range(1, 9))
LABELS = ("0", "1", "2", "3", "4", "DK", "NA", "SKIP")
CONTEXT = tuple(k for k, spec in SCHEMA["properties"].items() if "enum" in spec)
MIN_N, MIN_CELL = 20, 5
MAX_BYTES, MAX_RECORDS = 10_000_000, 50_000


def is_frequency(value: Any) -> bool:
    """Reject bools, which Python otherwise treats as integers."""
    return type(value) is int and 0 <= value <= 4


def validate_record(record: Any) -> dict[str, Any]:
    if not isinstance(record, dict):
        raise ValueError("A record must be a JSON object.")
    if set(record) - set(SCHEMA["properties"]):
        raise ValueError("Unexpected fields: remove identifiers and unsupported metadata.")
    if not set(SCHEMA["required"]).issubset(record):
        raise ValueError("Required protocol or eligibility metadata is missing.")
    for key, value in record.items():
        spec = SCHEMA["properties"][key]
        if "$ref" in spec:
            valid = is_frequency(value) or (type(value) is str and value in LABELS[5:])
        elif "const" in spec:
            valid = type(value) is str and value == spec["const"]
        elif spec.get("type") == "boolean":
            valid = type(value) is bool
        elif "enum" in spec:
            valid = type(value) is str and value in spec["enum"]
        else:
            raise ValueError("Unsupported schema definition; update and review the validator.")
        if not valid:
            # Do not echo potentially sensitive values or input records.
            raise ValueError("A record contains a value incompatible with the protocol schema.")
    return record


def ensure_external(path: Path) -> Path:
    resolved = path.expanduser().resolve()
    if resolved == ROOT or ROOT in resolved.parents:
        raise ValueError("Participant inputs and generated outputs must be outside this repository.")
    return resolved


def load_records(path: Path) -> list[dict[str, Any]]:
    path = ensure_external(path)
    if path.stat().st_size > MAX_BYTES:
        raise ValueError("Input exceeds the reviewed size limit.")
    records = []
    with path.open(encoding="utf-8-sig") as stream:
        for line_number, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                records.append(validate_record(json.loads(line)))
            except (ValueError, TypeError) as exc:
                raise ValueError(f"Invalid record at line {line_number}; contents not displayed.") from exc
            if len(records) > MAX_RECORDS:
                raise ValueError("Input exceeds the reviewed record limit.")
    return records


def eligible(record: dict[str, Any]) -> bool:
    return all(record[k] for k in ("consent", "adult", "eligible_experience")) and any(
        is_frequency(record.get(k)) for k in CORE
    )


def safe_counts(counts: dict[str, int], minimum_n: int = MIN_N) -> bool:
    return sum(counts.values()) >= minimum_n and all(v == 0 or v >= MIN_CELL for v in counts.values())


def withheld() -> dict[str, str]:
    # No total, complement or percentage is returned for a suppressed table.
    return {"status": "withheld", "reason": "insufficient_observations_or_small_cells"}


def marginal(records: list[dict[str, Any]], field: str) -> dict[str, Any]:
    options = LABELS if field in ITEMS else tuple(SCHEMA["properties"][field]["enum"])
    observed = Counter(str(r.get(field, "SKIP")) for r in records)
    counts = {option: observed[option] for option in options}
    if not safe_counts(counts):
        return withheld()
    result: dict[str, Any] = {
        "status": "candidate_requires_human_review",
        "n": sum(counts.values()),
        "counts": counts,
    }
    if field in ITEMS:
        valid_n = sum(counts[str(v)] for v in range(5))
        if valid_n < MIN_N:
            return withheld()
        result.update(valid_n=valid_n, frequent_or_always_share=(counts["3"] + counts["4"]) / valid_n)
    return result


def pair_table(records: list[dict[str, Any]], predictor: str, outcome: str) -> dict[str, Any]:
    bins = ("0_1", "2", "3_4")
    counts = {f"{group}|{level}": 0 for group in bins for level in ("0_2", "3_4")}
    for record in records:
        x, y = record.get(predictor), record.get(outcome)
        if not (is_frequency(x) and is_frequency(y)):
            continue
        group = "0_1" if x <= 1 else "2" if x == 2 else "3_4"
        level = "0_2" if y <= 2 else "3_4"
        counts[f"{group}|{level}"] += 1
    if not safe_counts(counts):
        return withheld()
    group_n = {group: sum(counts[f"{group}|{level}"] for level in ("0_2", "3_4")) for group in bins}
    if any(0 < n < MIN_N for n in group_n.values()):
        return withheld()
    return {
        "status": "candidate_requires_human_review",
        "predictor": predictor,
        "outcome": outcome,
        "paired_valid_n": sum(counts.values()),
        "counts": counts,
        "outcome_high_share_by_predictor": {
            group: counts[f"{group}|3_4"] / n if n else None for group, n in group_n.items()
        },
        "interpretation": "Exploratory sample description; no causal or population inference.",
    }


def summarize(records: list[dict[str, Any]], expected_synthetic: bool) -> dict[str, Any]:
    if not records:
        raise ValueError("No records supplied.")
    for record in records:
        validate_record(record)
    if any(r["is_synthetic"] is not expected_synthetic for r in records):
        raise ValueError("Synthetic/real origin mismatch. Do not mix or relabel data.")
    selected = [r for r in records if eligible(r)]
    if not selected:
        raise ValueError("No eligible observations; no results generated.")
    audit_counts = {"included": len(selected), "excluded": len(records) - len(selected)}
    audit: dict[str, Any] = {"status": "candidate_requires_human_review", "counts": audit_counts} if safe_counts(audit_counts) else withheld()
    return {
        "protocol_version": "0.1.0",
        "is_synthetic": expected_synthetic,
        "notice": "SYNTHETIC DEMONSTRATION - NOT STUDY FINDINGS" if expected_synthetic else "PRIVATE ANALYSIS - NOT CLEARED FOR PUBLICATION",
        "human_disclosure_review_required": True,
        "scope": "Nonprobability respondent reports; not unique companies.",
        "rules": {"minimum_valid_n": MIN_N, "minimum_nonzero_cell": MIN_CELL, "suppression": "whole_table"},
        "audit": audit,
        "marginals": {key: marginal(selected, key) for key in (*CONTEXT, *ITEMS)},
        "exploratory_pairs": {
            "H1": pair_table(selected, "T01", "P01"),
            "H2": pair_table(selected, "A02", "P02"),
        },
    }


def demo_records() -> list[dict[str, Any]]:
    """Balanced artificial patterns for testing, not a model of any population."""
    values: tuple[Any, ...] = (0, 1, 2, 3, 4, "DK", "NA", "SKIP")
    rows = []
    for i in range(80):
        row: dict[str, Any] = {"protocol_version": "0.1.0", "is_synthetic": True, "consent": True, "adult": True, "eligible_experience": True}
        for key in CONTEXT:
            options = SCHEMA["properties"][key]["enum"]
            row[key] = options[i % len(options)]
        row.update({key: values[(i + j) % len(values)] for j, key in enumerate(ITEMS)})
        rows.append(row)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--demo", action="store_true", help="Use only in-memory synthetic examples.")
    source.add_argument("--input", type=Path, help="Private JSONL export outside the repository.")
    parser.add_argument("--out", type=Path, required=True, help="New private JSON output outside the repository; never overwritten.")
    args = parser.parse_args()
    try:
        destination = ensure_external(args.out)
        if destination.exists():
            raise ValueError("Output already exists; choose a new path. Nothing was overwritten.")
        records = demo_records() if args.demo else load_records(args.input)
        result = summarize(records, expected_synthetic=args.demo)
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open("x", encoding="utf-8") as stream:
            json.dump(result, stream, ensure_ascii=False, indent=2, allow_nan=False)
            stream.write("\n")
    except (ValueError, OSError) as exc:
        # OSError filenames may be sensitive; print only a generic message.
        parser.exit(2, (str(exc) if isinstance(exc, ValueError) else "Input/output error; verify private paths and permissions.") + "\n")
    print("Synthetic demonstration saved; not study findings." if args.demo else "Private summary saved; human disclosure review required before any publication.")


if __name__ == "__main__":
    main()
