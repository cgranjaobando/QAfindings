# Definiciones y operacionalización

**v0.1.0 · propuesta no validada.** [Fuentes R1, R4, R7](../references/REFERENCES.md).

## Definiciones de trabajo

- **Aseguramiento de calidad:** actividades planificadas y sistemáticas que aportan confianza en el cumplimiento de requisitos de calidad. No promete cero defectos ni exige un cargo concreto.
- **Prevención de introducción:** actuar sobre requisitos, diseño, decisiones o procesos antes de introducir un problema.
- **Prevención de escape:** detectar un defecto existente antes de que llegue a usuarios. Es valiosa, pero no demuestra que se evitó introducirlo.
- **Prevención de recurrencia:** cambiar y comprobar un proceso a partir de problemas anteriores.
- **Control/testing:** evaluar productos o resultados; puede alimentar el aseguramiento. No se lo clasifica como inútil ni incompatible con QA.
- **Participación temprana:** oportunidad real de intervenir antes de fijar una solución; no basta asistir antes de programar.
- **Enfoque declarado:** etiqueta informada por el participante. Se conserva incluso si sus prácticas contradicen expectativas sobre esa etiqueta.

La tabla es un marco de medición del proyecto, no una certificación ni una transcripción de una norma. Una práctica puede servir a varias funciones. Revisar código, por ejemplo, puede detectar defectos, mientras que asegurar sistemáticamente que se realizan revisiones acordadas se refiere al proceso.

| Dimensión | Indicadores | Qué no permite concluir |
| --- | --- | --- |
| Análisis y requisitos antes de implementar | P01, P02, P03, P07 | Que no se introdujeron defectos |
| Aplicación y mejora de procesos | P04, P05, P06, P08 | Que toda la organización cumple una norma |
| Capacidad de influir y recursos | A01-A03; earliest_quality; ticket_state | Que existe un veto unilateral de QA |
| Presión y criterios de evaluación | T01-T04 | Causalidad económica o intención de directivos |
| Control y respuesta a defectos | C01-C02 | Ausencia o presencia completa de QA |
| Resultados percibidos | O01-O02 | Tasas reales de defectos o pérdidas financieras |
| Prácticas iterativas y de retroalimentación | F01-F03; framework | Grado certificado de agilidad |
| Contexto | role, experience, company_size, qa_role_present, release_cadence | Identidad o conteo de empresas únicas |

## Escala común

Sobre las ocasiones pertinentes de los tres meses de referencia: **0 Nunca; 1 Rara vez; 2 Algunas veces; 3 Frecuentemente; 4 Siempre; DK No sé/no pude observarlo; NA No hubo ocasión aplicable; SKIP Prefiero no responder.**

No se asigna un porcentaje exacto a expresiones verbales antes de comprobar su interpretación en el piloto. DK, NA, SKIP y campos ausentes no son cero. La ausencia de una oportunidad no implica fallo del proceso.

## Regla contra conclusiones circulares

No definir QA por la presencia de una persona titulada QA ni por la obligación de redactar todos los tickets entre todos. No definir buen Agile mediante el resultado que se pretende explicar. No tomar un ticket detallado como prueba de que nunca hubo revisión preventiva. Las entrevistas preguntan por decisiones, alternativas y qué permanecía abierto.

Los análisis principales son por ítem. No hay ponderaciones, ranking, semáforo ni puntuación global validada. Agrupar 3-4 como frecuencia alta es una simplificación analítica declarada, no un umbral normativo.
