# Protocolo de investigación

**QAFindings · v0.1.0 · 2026-09-20 · borrador previo a datos.**

No existe aprobación ética, prerregistro externo, formulario activo ni evidencia empírica del proyecto. Las decisiones propuestas aquí deben revisarse antes del piloto. Fuentes: [bibliografía](../references/REFERENCES.md).

## 1. Título provisional

**Prácticas reportadas de aseguramiento de calidad, participación en decisiones y presión de entrega en equipos de software: un estudio de métodos mixtos.**

English: *Reported quality-assurance practices, decision influence, and delivery pressure in software teams: a mixed-methods study.*

## 2. Problema y justificación

Un cargo llamado QA, un conjunto de pruebas o una reunión de refinamiento no permiten establecer por sí solos cómo se asegura la calidad. ASQ distingue el aseguramiento sistemático del proceso de la inspección del producto, reconociendo su relación [R1]. Es necesario observar qué actividades se realizan, quién puede modificar decisiones y qué seguimiento tienen las mejoras, sin asumir que esas actividades pertenecen exclusivamente a una especialidad.

La revisión de Kuutila y colaboradores analiza presiones temporales en ingeniería de software y resultados que varían con el contexto [R2]. El mapeo de Behutiye y colaboradores trata dificultades en la gestión de requisitos de calidad en desarrollo ágil y rápido [R3]. Estos antecedentes justifican investigar; no proporcionan una estimación del estado de todas las empresas en 2026. La lectura inicial de ambos se limita a sus registros y resúmenes, y la revisión de texto completo está pendiente.

La motivación del proyecto surge de preguntas profesionales sobre la distancia entre funciones declaradas y prácticas reales. Experiencias personales, conversaciones previas y publicaciones de redes no son datos del estudio. No se publicarán empleadores ni incidentes identificables.

## 3. Objetivos

**General:** describir prácticas de aseguramiento de calidad reportadas por profesionales y explorar su relación con participación, recursos y presión de entrega.

**Específicos:** (a) medir la frecuencia de prácticas sistemáticas de prevención y seguimiento; (b) distinguir participación antes de implementar de participación antes de fijar la solución; (c) explorar diferencias entre enfoques declarados y prácticas observadas; (d) comprender mecanismos organizativos que facilitan o limitan el aseguramiento; (e) documentar casos que contradigan las expectativas iniciales; (f) producir materiales y análisis trazables sin exponer participantes.

## 4. Preguntas y expectativas previas

- **RQ1:** ¿con qué frecuencia se reportan P01-P08 y qué proporción de respuestas indica desconocimiento o falta de oportunidad para observarlas?
- **RQ2:** ¿cuándo se incorpora una perspectiva de calidad y qué decisiones puede cambiar? Se examinan contexto, A01-A03 y entrevistas.
- **RQ3:** ¿qué patrones descriptivos relacionan presión, capacidad e influencia con prácticas preventivas? Se contrastarán también ejemplos de presión alta con prevención sostenida.
- **RQ4:** ¿cómo difieren los relatos según rol y enfoque de trabajo declarado, sin redefinir a posteriori un equipo como no ágil porque sus resultados sean desfavorables?
- **RQ5:** ¿qué explicaciones y contraejemplos aportan las entrevistas para los patrones cuantitativos?

**H1, exploratoria y direccional:** mayor desajuste reportado entre trabajo y capacidad (T01) se asociaría con menor frecuencia de análisis temprano acordado (P01).

**H2, exploratoria y direccional:** mayor influencia de la revisión de calidad (A02) se asociaría con mayor frecuencia de requisitos de calidad verificables antes de implementar (P02).

Se admitirán relaciones nulas, inversas o heterogéneas. No se buscará demostrar una causa macroeconómica con estas variables. Presión comercial, incentivos y asignación de recursos son aproximaciones específicas, no mediciones de capitalismo o consumismo. No se pregunta orientación política.

## 5. Diseño y unidad de análisis

Estudio observacional transversal de métodos mixtos convergentes: encuesta estructurada y entrevistas semiestructuradas, en muestras reclutadas por separado. Los resultados se integrarán por temas y patrones, no mediante unión de registros individuales. No se presume que cada entrevistado haya respondido la encuesta.

La unidad de encuesta es una persona informando sobre un equipo. Distintas personas pueden describir el mismo equipo sin que podamos detectarlo; no habrá identificadores de empresa para agruparlas. Por ello, no se contabilizarán empresas únicas, no se extrapolarán porcentajes a empresas y se reconocerá la dependencia desconocida entre respuestas.

La evidencia principal es autorreportada. Una descripción de práctica no equivale a su observación independiente ni prueba que evitó un defecto. Una fase futura de auditoría requeriría un protocolo y permisos propios, sin utilizar este estudio para solicitar documentos internos.

## 6. Participantes y alcance

Alcance inicial propuesto: personas adultas capaces de responder en español que hayan trabajado al menos tres meses en un mismo equipo de software durante los últimos doce meses. Incluye QA/testing, desarrollo, producto/análisis de negocio y liderazgo, con o sin cargo especializado de calidad. El reclutamiento puede ser internacional; la lengua y los canales limitarán el alcance.

Cada participante elegirá el equipo en que acumuló más tiempo dentro de esa ventana; en empate, el más reciente. Describirá los últimos tres meses que trabajó en ese equipo. No se solicitarán las fechas ni el empleador. Una respuesta por persona.

Se excluyen menores, ausencia de consentimiento, experiencia no elegible, pruebas del instrumento y respuestas que no contengan ninguna observación válida de P01-P08. No se excluirán experiencias favorables, críticas, desacuerdos con definiciones ni desconocimiento de la terminología. Las respuestas DK/NA no se interpretarán como inexistencia de práctica.

## 7. Muestreo y reclutamiento

Muestreo no probabilístico, voluntario y multicanal. Se buscará diversidad de roles y experiencias mediante comunidades de QA, desarrollo, producto y liderazgo. LinkedIn será un canal posible, no el marco muestral completo. La invitación no utilizará un discurso de denuncia ni pedirá confirmar una conclusión.

Meta operativa propuesta: 200 encuestas evaluables en una ventana fija de ocho semanas después de completar las condiciones de lanzamiento. No es un cálculo de representatividad ni de potencia. La ventana no se cerrará por obtener un resultado esperado; se analizarán todas las respuestas elegibles recibidas dentro de ella. Las fechas exactas se fijarán antes de abrir. Un alcance menor se publicará con sus limitaciones, sin prolongación basada en resultados.

Se intentará invitar mediante al menos dos comunidades o canales diferentes por familia de rol. La composición se describirá, no se corregirá con ponderaciones inventadas. No habrá cuotas que obliguen a descartar respuestas ni pagos aprobados en esta fase.

Entrevistas: objetivo inicial de 15 y límite operativo de 24, con variación de rol, enfoque y experiencia positiva/mixta/negativa. Se revisará la suficiencia temática por lotes y se documentarán vacíos; alcanzar un número no prueba saturación. Nunca se seleccionará solo a personas insatisfechas. Las personas en relaciones de supervisión directa con el equipo investigador no serán reclutadas activamente.

## 8. Instrumentos y validación

La encuesta mide comportamientos en una ventana concreta y no pregunta simplemente si se hace QA. Combina ocho prácticas de aseguramiento, influencia, presión, control, resultados percibidos y formas de trabajo. Todas las preguntas analíticas permiten omisión, desconocimiento y, cuando corresponde, no aplicabilidad.

El instrumento es original, no una escala validada. Antes de campo: revisión por especialistas con perspectivas distintas, 5-8 entrevistas cognitivas y un piloto técnico propuesto de 15-20 respuestas. Los materiales del piloto no se mezclarán con la muestra principal. La recolección del piloto exige los mismos resguardos de consentimiento y privacidad. Cambios de redacción o definición requieren versión nueva y actualización conjunta del esquema y plan.

No se construirá un índice global de QA ni un corte que declare a empresas aptas o deficientes. La revisión de contenido y comprensión solo aportará evidencia inicial; no se anunciará validación psicométrica completa. [R4, R5]

## 9. Procedimiento

1. Revisar alcance, bibliografía y amenazas a validez; asignar responsables.
2. Obtener revisión ética independiente o determinación documentada aplicable y resolver obligaciones de datos.
3. Configurar un servicio privado de recolección; verificar metadatos, accesos y eliminación con datos sintéticos.
4. Realizar revisión cognitiva y piloto autorizado; documentar cambios.
5. Congelar instrumentos, hipótesis, reglas de exclusión y análisis. Depositar prerregistro externo antes de datos principales.
6. Publicar invitación neutral sin seguimiento individual ni contacto con empleadores.
7. Cerrar en la fecha declarada; conservar una copia privada íntegra, extraer datos permitidos y aplicar el plan registrado.
8. Analizar encuesta e entrevistas por separado; buscar explicaciones alternativas y casos discrepantes.
9. Revisar riesgo de divulgación; publicar solo agregados y síntesis autorizadas.
10. Completar el manuscrito y buscar revisión metodológica y editorial.

## 10. Ética, recursos y producto

Consultar [privacidad](../ethics/PRIVACY.md), [control de lanzamiento](../ethics/LAUNCH_CHECKLIST.md), [análisis](ANALYSIS_PLAN.md) y [hoja de ruta](ROADMAP.md). La investigación no ofrece protección legal absoluta ni garantiza ausencia de represalias. La encuesta evita identificadores directos; las entrevistas son confidenciales, no necesariamente anónimas frente al entrevistador.

Productos: protocolo versionado, instrumentos, plan de análisis, código probado con datos sintéticos, bibliografía, síntesis pública y manuscrito. No se generarán resultados antes de recolectar ni se afirmará publicación científica revisada por pares por estar en GitHub.

## 11. Amenazas principales

Autoselección, cobertura de canales y lengua, memoria, deseabilidad social, varianza de método común, diferencias entre roles, interpretación de frecuencia, confusión, causalidad inversa, dependencia entre personas del mismo equipo y reidentificación por contexto. Las decisiones de privacidad reducen detalle y capacidad de verificación. Se reportarán también los límites creados por esas decisiones, sin relajarlas para obtener resultados más llamativos.
