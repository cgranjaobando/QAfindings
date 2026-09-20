# Encuesta QAFindings

**v0.1.0 · borrador no validado · NO ACTIVA.** No usar para recolectar mientras existan pendientes en [consentimiento](../ethics/consent-survey.es.md) y [control de lanzamiento](../ethics/LAUNCH_CHECKLIST.md).

## Instrucciones

Nos interesan prácticas que ocurren, no la aplicación ideal de una metodología. No hay respuestas correctas. Incluye lo que realiza cualquier integrante del equipo, tenga o no un cargo de QA. No compartas nombres, documentos, tickets ni datos de empresas o personas.

Elige el equipo de software en el que acumulaste más tiempo durante los últimos doce meses, siempre que hayas trabajado allí al menos tres meses. En empate, el más reciente. Responde sobre tus últimos tres meses en ese equipo; no sobre toda tu carrera.

## 0. Elegibilidad y consentimiento

Confirmar 18 años o más (`adult`), tres meses en el equipo dentro de la ventana (`eligible_experience`) y aceptación del consentimiento final (`consent`). Si alguna respuesta es no, finalizar sin guardar respuestas para investigación. No solicitar fecha de nacimiento ni firma. Los campos `protocol_version` e `is_synthetic` son metadatos del sistema/importador, no preguntas al participante.

## 1. Contexto mínimo, opcional

| Campo | Pregunta | Opciones y códigos |
| --- | --- | --- |
| role | ¿Cuál fue tu función principal en ese equipo? | QA/testing (QA); desarrollo/ingeniería (DEV); producto/análisis de negocio (PRODUCT); liderazgo/gestión (LEAD); otra (OTHER); prefiero no responder (SKIP) |
| experience | ¿Cuánta experiencia total tienes en trabajo de software? | Menos de 2 años (LT2); 2-5 (2_5); 6-10 (6_10); más de 10 (GT10); SKIP |
| company_size | Aproximadamente, ¿cuántas personas tenía la organización para la que trabajabas? | 1-49 (1_49); 50-249 (50_249); 250-999 (250_999); 1000 o más (1000_PLUS); no sé (DK); SKIP |
| framework | ¿Qué enfoque describía mejor la forma de trabajo declarada de ese equipo? | Scrum (SCRUM); Kanban (KANBAN); híbrido (HYBRID); secuencial (SEQUENTIAL); ninguno definido (NONE); otro (OTHER); DK; SKIP |
| qa_role_present | ¿Había al menos una persona con una función explícitamente dedicada a QA o testing? | Sí (YES); no (NO); DK; SKIP |
| release_cadence | ¿Con qué frecuencia se entregaban cambios utilizables a usuarios? | Diariamente o más (DAILY); semanalmente (WEEKLY); mensualmente (MONTHLY); menos de una vez al mes (LESS); sin frecuencia regular (IRREGULAR); DK; SKIP |
| earliest_quality | Habitualmente, ¿en qué momento se incorporaba una perspectiva de calidad con posibilidad de influir? | Al definir problema/necesidad (PROBLEM); al refinar antes de programar (REFINEMENT); durante implementación (IMPLEMENTATION); antes de liberar (PRERELEASE); después de liberar (POSTRELEASE); no observé esa participación (NOTOBSERVED); DK; SKIP |
| ticket_state | Cuando se discutían los tickets o unidades de trabajo, ¿qué situación era más frecuente? | Problema abierto, solución por construir (OPEN); solución propuesta pero modificable (CHANGEABLE); solución fijada, discusión centrada en implementarla (FIXED); variaba sin patrón claro (MIXED); DK; SKIP |

Las categorías se revisarán en piloto. No pedir organización, cliente, país concreto ni descripción libre de OTHER. No interpretar solution FIXED como prueba de ausencia de una revisión previa.

## 2. Frecuencia de prácticas

En las ocasiones pertinentes de esos tres meses: **0 Nunca; 1 Rara vez; 2 Algunas veces; 3 Frecuentemente; 4 Siempre; DK No sé/no pude observarlo; NA No hubo ocasión aplicable; SKIP Prefiero no responder.** Todas son opcionales. NA es útil, por ejemplo, si no hubo incidentes que analizar.

### Procesos de aseguramiento

| ID | Durante el periodo de referencia... |
| --- | --- |
| P01 | Antes de implementar cambios, el equipo aplicó una práctica acordada para identificar riesgos de calidad. |
| P02 | Los requisitos de calidad relevantes, por ejemplo fiabilidad, accesibilidad o rendimiento, se hicieron verificables antes de implementar. |
| P03 | Antes de modificar componentes compartidos, se aplicó un análisis acordado de sus posibles efectos en otras partes. |
| P04 | El equipo comprobó que las revisiones técnicas acordadas se realizaron. |
| P05 | Las acciones destinadas a evitar que un problema se repitiera tuvieron responsable y seguimiento. |
| P06 | Después de una mejora del proceso, se comprobó si disminuyó el problema que la motivó. |
| P07 | Los cambios en requisitos llevaron a reevaluar los riesgos antes de implementar esos cambios. |
| P08 | Se revisó si los criterios acordados para considerar terminado el trabajo se cumplieron en la práctica. |

### Influencia y capacidad

| ID | Durante el periodo de referencia... |
| --- | --- |
| A01 | Las personas que aportaron una perspectiva de calidad pudieron proponer alternativas antes de fijar la solución. |
| A02 | Los hallazgos de revisiones de calidad pudieron modificar el diseño, el alcance o el plan de entrega. |
| A03 | Se reservó capacidad explícita para actividades preventivas de calidad. |

### Presión y criterios de evaluación

| ID | Durante el periodo de referencia... |
| --- | --- |
| T01 | El trabajo comprometido superó la capacidad disponible del equipo. |
| T02 | Se postergaron actividades de análisis o mejora del proceso para cumplir fechas de entrega. |
| T03 | Entraron cambios por compromisos con clientes o comerciales sin retirar otro trabajo comprometido. |
| T04 | Los indicadores usados para evaluar al equipo se centraron en cantidad o rapidez de entregas. |

### Control y resultados percibidos

| ID | Durante el periodo de referencia... |
| --- | --- |
| C01 | Se ejecutaron pruebas del software implementado antes de liberarlo. |
| C02 | Los defectos reportados después de una entrega se registraron y atendieron. |
| O01 | Se repitieron defectos atribuidos a causas que el equipo ya conocía. |
| O02 | Fue necesario rehacer trabajo por reglas o requisitos aclarados después de implementar. |

### Forma de trabajo observada

| ID | Durante el periodo de referencia... |
| --- | --- |
| F01 | Se entregaron incrementos pequeños y utilizables del producto. |
| F02 | La retroalimentación de usuarios o interesados modificó el trabajo siguiente. |
| F03 | El equipo revisó su manera de trabajar y acordó ajustes. |

## 3. Cierre

Gracias por aportar tu experiencia. Revisa tus respuestas antes de enviar. No hay campo para nombre, correo, comentarios libres ni enlace a perfiles. La invitación a una entrevista, cuando se active, se ofrecerá por un canal general separado, sin transmitir un identificador de esta encuesta.

## Notas de implementación para investigadores

Treinta preguntas analíticas: ocho de contexto y veintidós de frecuencia, más tres confirmaciones de elegibilidad/consentimiento. Dividir en pantallas accesibles; evitar matrices anchas en móvil. No aleatorizar sin revisar el protocolo. Conservar orden y redacción final en prerregistro. No mostrar un puntaje de QA ni recomendaciones basadas en respuestas. La duración deberá medirse en piloto. [Esquema](survey.schema.json).
