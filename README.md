# QAFindings

## Aseguramiento de calidad en el trabajo real de software

**Estado: protocolo inicial v0.1.0, en revisión. No se está reclutando ni recolectando datos. No hay resultados empíricos del proyecto.**

QAFindings es un proyecto de investigación pública sobre las prácticas de aseguramiento de calidad que profesionales de software reportan en sus equipos, la capacidad de influir en decisiones y las condiciones organizativas que favorecen o limitan la prevención. Incluye equipos que se identifican como ágiles y equipos que usan otros enfoques.

**Pregunta central:** ¿qué prácticas sistemáticas de calidad se realizan, en qué momento pueden modificar decisiones y qué relación describen los profesionales entre esas prácticas, los recursos y la presión de entrega?

No partimos de que Agile funciona ni de que es incompatible con QA. Tampoco equiparamos tener un cargo de QA con realizar aseguramiento, ni la ausencia de ese cargo con ausencia de calidad. Mediremos prácticas concretas realizadas por cualquier integrante del equipo. La presión comercial y los incentivos económicos son mecanismos por investigar, no conclusiones anticipadas sobre un sistema económico.

> Repositorio público no significa respuestas públicas. No publiques testimonios, nombres de empresas, tickets internos, capturas, grabaciones, contactos ni respuestas de encuestas en issues, discusiones, commits o pull requests.

### Alcance y límites

La primera fase propuesta combina una encuesta en español y entrevistas confidenciales, con reclutamiento voluntario en varias comunidades y roles. La unidad de análisis es **una persona describiendo un equipo de referencia**, no una empresa auditada. No se obtendrá una muestra representativa de todas las empresas, ni se establecerán causas con una encuesta transversal. Una futura fase de auditoría documental necesitaría autorización y un protocolo independiente.

El horizonte de recuerdo será los últimos tres meses de trabajo en un mismo equipo dentro de los últimos doce meses. Los instrumentos son nuevos y **no están validados todavía**. Se requiere revisión metodológica, pilotaje, evaluación ética y comprobación de privacidad antes del trabajo de campo.

### Navegar el proyecto

| Material | Ubicación |
| --- | --- |
| Problema, objetivos, preguntas y diseño | [Protocolo](research/PROTOCOL.md) |
| Definiciones y medición de prácticas | [Operacionalización](research/OPERATIONALIZATION.md) |
| Muestreo, exclusiones, análisis y límites | [Plan de análisis](research/ANALYSIS_PLAN.md) |
| Plan para registrar antes de recolectar | [Prerregistro](research/PREREGISTRATION.md) |
| Encuesta y diccionario legible por máquina | [Encuesta](instruments/survey.es.md) · [Esquema](instruments/survey.schema.json) |
| Entrevistas y revisión de instrumentos | [Guía](instruments/interview.es.md) · [Piloto](instruments/PILOT.md) |
| Consentimientos y protección de participantes | [Privacidad](ethics/PRIVACY.md) · [Encuesta](ethics/consent-survey.es.md) · [Entrevista](ethics/consent-interview.es.md) |
| Condiciones obligatorias antes de abrir | [Control de lanzamiento](ethics/LAUNCH_CHECKLIST.md) |
| Convocatoria neutral | [Reclutamiento](recruitment/INVITATION.es.md) |
| Bibliografía y búsqueda pendiente | [Revisión inicial](research/LITERATURE_REVIEW.md) · [Referencias](references/REFERENCES.md) |
| Artículo en construcción | [Manuscrito](manuscript/article.es.md) |
| Fases, recursos y trazabilidad | [Hoja de ruta](research/ROADMAP.md) · [Decisiones](research/DECISIONS.md) |
| Código, pruebas y datos permitidos | [Análisis](analysis/README.md) · [Política de datos](data/README.md) |

### Protección por defecto

- Encuesta: sin nombre, correo, empresa, perfiles, tickets ni texto libre. El proveedor, sus registros técnicos y la configuración de privacidad siguen pendientes de revisión; todavía no se ofrece un formulario activo.
- Entrevistas: confidenciales y seudonimizadas; pueden usar un alias y no requieren grabación. Los datos de contacto, cuando sean necesarios, estarán separados. No se vincularán entrevistas con respuestas individuales de la encuesta.
- Publicación: protocolo, instrumentos, código, síntesis temática y agregados revisados. Nunca microdatos reales ni transcripciones. Las celdas pequeñas y combinaciones identificables se revisarán antes de publicar.

### Ruta al artículo

El repositorio permite desarrollar un manuscrito con introducción, métodos, resultados, discusión, limitaciones, referencias y declaraciones de ética y autoría. **Un borrador en GitHub no es un artículo revisado por pares.** Los resultados permanecerán pendientes hasta disponer de datos válidos. El prerregistro externo, un identificador persistente y una eventual evaluación editorial son pasos separados y no se han realizado.

Las orientaciones metodológicas de referencia incluyen ACM SIGSOFT Empirical Standards, CHERRIES y COREQ. Son guías, no certificaciones de este proyecto. La bibliografía inicial está identificada en [REFERENCES.md](references/REFERENCES.md).

### Contribuir

Se aceptan críticas a las definiciones, revisiones metodológicas y mejoras del código, incluso cuando contradigan la motivación inicial. Lee [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md) y [GOVERNANCE.md](GOVERNANCE.md). Las contribuciones públicas de GitHub muestran la identidad de la cuenta; no son un canal anónimo de participación.

La asignación de responsabilidades, el canal privado de contacto, el proveedor de recolección y la revisión ética todavía deben completarse. El proyecto no representa a empleadores de sus colaboradores.

**English summary:** QAFindings is a public, pre-data research project studying reported quality-assurance practices, decision influence, and delivery pressures in software teams. The first proposed study uses a Spanish-language survey and separate confidential interviews. Public materials do not include participant-level data. There are no findings, ethics approval, or registered study yet. See [README.en.md](README.en.md).
