# Plan de análisis previo a datos

**v0.1.0 · borrador para prerregistro.** Este documento distingue análisis planificados de ampliaciones exploratorias. No hay datos reales del estudio.

## 1. Entradas y trazabilidad

Instrumento y esquema de la misma versión; exportación privada sin identificadores; registro privado de inclusión/exclusión; bitácora pública solo de decisiones metodológicas. Mantener originales, datos depurados y salidas en almacenamiento cifrado fuera del repositorio. El código de análisis público no recibirá microdatos a través de GitHub Actions, issues o artefactos.

La exportación para análisis usa JSONL, una persona por línea, conforme a [survey.schema.json](../instruments/survey.schema.json). La adaptación desde el proveedor aún debe implementarse y probarse; el esquema no es un formulario desplegado.

## 2. Inclusión, exclusión y faltantes

Exigir consentimiento, mayoría de edad y experiencia elegible. Excluir pruebas/piloto y al menos documentar la ausencia total de observaciones válidas en P01-P08. Conservar para análisis por ítem a quienes contesten una o más P válidas; no exigir completar todo el cuestionario. No analizar datos sin consentimiento.

Frecuencias válidas: enteros 0-4. DK, NA y SKIP se describen separadamente. Un campo analítico omitido se trata como SKIP, no como ausencia de práctica. No se hará imputación en el análisis principal. Cada porcentaje tendrá su denominador explícito.

Duplicados: solicitar una respuesta por persona. Eliminar únicamente duplicaciones técnicas del mismo envío demostradas por el sistema privado. No eliminar patrones iguales de respuestas porque pueden corresponder a personas distintas. Sin IP, fingerprinting ni cuenta obligatoria no puede garantizarse unicidad. No se usarán detectores de texto generado por IA ni duración como criterios automáticos; la encuesta no solicita texto libre. Documentar límites y desviaciones frente a recomendaciones de referencia [R4, R5].

No consultar resultados para decidir exclusiones, ampliar fechas o reclutar solo casos favorables a una hipótesis. Cualquier regla nueva debe quedar fechada como desviación, con motivación y análisis de sensibilidad cuando sea viable.

## 3. Análisis principal descriptivo

Para cada P01-P08: distribución completa 0-4/DK/NA/SKIP; denominador de respuestas válidas; proporción 3-4 entre respuestas 0-4, siempre junto a la distribución original. También describir A, T, C, O y F y la composición de contexto.

No llamar a estos resultados porcentaje de empresas que hacen QA. Son proporciones de respuestas de una muestra voluntaria. No presentar un margen de error poblacional: no existe diseño probabilístico ni independencia verificable entre equipos.

El código inicial calcula marginales y tablas exploratorias preespecificadas. No implementa estimación causal, ponderación, validación de escalas, modelos multinivel ni análisis temático automático.

## 4. Asociaciones exploratorias preespecificadas

H1: T01 frente a P01. H2: A02 frente a P02. Agrupar el predictor en 0-1, 2 y 3-4; el resultado en 0-2 y 3-4. Usar solo pares con respuestas 0-4 en ambos. Reportar frecuencias y proporciones descriptivas si las reglas de divulgación lo permiten.

No se calcularán p-valores ni se declarará confirmación de hipótesis con estas tablas. No se interpretará la etiqueta ágil como tratamiento experimental. Un estudio analítico posterior necesitaría justificar tamaño de muestra, confusores, modelos y estructura de dependencia antes de ejecutarlo.

Comparaciones por rol, framework y qa_role_present son secundarias, descriptivas y sujetas a suficiente tamaño y privacidad. No crear cruces detallados de rol, antigüedad y tamaño empresarial. Los ítems F permiten contrastar etiqueta y prácticas sin reclasificar equipos a conveniencia.

## 5. Sensibilidad

Comparar las distribuciones principales: (a) todas las personas elegibles con al menos una P válida; (b) quienes contestaron al menos seis P con valores 0-4; (c) composición por rol cuando no genere celdas pequeñas. Una discrepancia se discute, no se oculta. Diferencias DK/NA por rol pueden revelar visibilidad desigual, no diferencias reales del proceso.

Las tablas secundarias y sensibilidades todavía requieren implementación o revisión adicional; no se afirmará que las ejecuta el programa inicial.

## 6. Entrevistas

Análisis temático con libro de códigos inicialmente deductivo y espacio inductivo. Códigos iniciales: momento de decisión, riesgos examinados, capacidad reservada, autoridad distribuida, presión contractual, incentivos, mejora de proceso, prevención de escape, recurrencia, casos contradictorios y explicaciones alternativas.

Trabajar sobre notas/transcripciones seudonimizadas en entorno privado. Registrar extracto privado, código, interpretación, alternativas y decisiones. Una segunda persona revisará un subconjunto propuesto del 20% y todos los contraejemplos relevantes, si existe colaboración autorizada; sin ella se declarará análisis de un solo investigador. No inventar acuerdo entre codificadores ni confundir consenso con verdad.

Buscar casos con prevención sostenida bajo presión, fallas sin presión comercial clara, prácticas realizadas sin cargo QA y casos donde un ticket definido sí pasó por revisión previa. No contar menciones de entrevistas como prevalencia poblacional. La suficiencia se discute según diversidad y contenido, no por un número mágico de entrevistas. [R6]

## 7. Integración

Construir una matriz: patrón de encuesta; tema de entrevistas; convergencia, divergencia o ausencia de evidencia; explicación alternativa; alcance permitido de la conclusión. Las muestras no están vinculadas persona a persona y la coincidencia no prueba triangulación independiente de un mismo evento.

## 8. Divulgación y revisiones

Aplicar revisión humana a todo resultado. Regla operativa conservadora inicial: no publicar una tabla con menos de 20 observaciones o con alguna celda no nula menor de 5. Si la regla falla, omitir la tabla completa; no publicar complementos, denominadores ni porcentajes que permitan reconstruir celdas pequeñas. Estos umbrales son decisiones de protección del proyecto, no garantías matemáticas de anonimato.

Revisar conjuntamente tablas, texto, versiones anteriores y citas para prevenir reconstrucción por diferencias. No publicar microdatos aunque se eliminen nombres. Una síntesis cualitativa se presenta como paráfrasis analítica; no inventar citas textuales o combinar voces como si fueran una sola. Las citas literales exigen autorización específica, revisión de identificabilidad y, cuando sea posible, aprobación del fragmento.

## 9. Reproducibilidad y afirmaciones

Publicar código, versión del instrumento, reglas, ambiente probado, resultados agregados autorizados y desviaciones. Un tercero puede ejecutar el código con datos sintéticos; no podrá verificar completamente el análisis real sin acceso controlado a los microdatos. Declarar esa limitación. El acceso adicional, si se considera, exige evaluación ética, base autorizada y acuerdo específico; no es una promesa de datos disponibles a solicitud.

Cada afirmación del artículo se etiquetará en el registro de evidencia como descriptiva, interpretativa, exploratoria o sustentada en literatura. No se inferirán pérdidas, culpabilidad, intenciones ni causas sistémicas sin datos adecuados.
