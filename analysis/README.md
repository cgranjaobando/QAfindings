# Análisis reproducible: código inicial

**v0.1.0 · solo probado con datos completamente sintéticos. No hay resultados del estudio.**

`analyze.py` utiliza únicamente la biblioteca estándar de Python y está escrito para Python 3.10 o superior. Se ejecutaron las pruebas en Python 3.13.5. No se ha comprobado cada versión de Python ni configurado GitHub Actions.

## Ejecutar las pruebas

Desde la raíz del repositorio:

```bash
python3 -m unittest discover -s tests -v
```

Las 21 pruebas utilizan ejemplos artificiales. No necesitan participantes, credenciales, red ni archivos de empresas.

## Demostración, no hallazgos

Elige un destino privado fuera del repositorio. Las rutas siguientes son ejemplos y deben adaptarse a tu equipo:

```bash
python3 analysis/analyze.py --demo --out /ruta/privada/fuera-del-repositorio/demo.json
```

Se generan 80 registros ficticios en memoria solo para probar la lógica. Sus distribuciones fueron construidas artificialmente y no describen ninguna población. La salida lleva una advertencia de demostración y nunca debe usarse en Resultados del manuscrito.

## Uso futuro con exportación real autorizada

Solo después de cumplir el protocolo y el control de lanzamiento:

```bash
python3 analysis/analyze.py --input /ruta/privada/exportacion.jsonl --out /ruta/privada/resumen.json
```

Una fila JSON por línea, conforme a [survey.schema.json](../instruments/survey.schema.json). El importador específico del futuro servicio de encuesta **no está implementado**. Debe eliminar metadatos e identificadores en un entorno privado, respetando consentimiento y reglas de inclusión. Nunca subir un archivo real para pedir ayuda con su formato.

El programa rechaza campos ajenos al esquema, versiones incorrectas, mezcla de origen sintético/real y entradas/salidas dentro del checkout. No sobrescribe destinos existentes. Límite operativo inicial: 10 MB de entrada y 50 000 registros. No imprime contenidos ni valores inválidos. El verificador implementa las reglas necesarias para este esquema; **no es un motor general de JSON Schema**.

## Qué calcula

Distribuciones marginales de ocho campos de contexto y veintidós frecuencias, faltantes separados y proporciones 3-4 con denominadores numéricos válidos. Incluye dos tablas exploratorias preespecificadas: T01/P01 y A02/P02. Selecciona únicamente registros con consentimiento y elegibilidad, y al menos una observación P válida. No elimina patrones iguales como si necesariamente fueran duplicados.

## Protección de salidas

Se omite una tabla completa si su total es menor de 20 o alguna celda no nula es menor de 5. Las frecuencias requieren además 20 respuestas numéricas válidas; las tablas de pares requieren al menos 20 pares por grupo no vacío. Una tabla omitida no incluye su denominador ni porcentajes para intentar ocultar solo una celda. Estas reglas conservadoras pueden impedir publicar muchos desgloses.

**Todo resultado requiere revisión humana antes de publicación.** El código no detecta todas las combinaciones identificables, diferencias entre versiones, dependencias entre equipos ni riesgos contextuales. No certifica anonimato ni cumplimiento legal. Que una salida esté fuera del checkout tampoco demuestra que su carpeta sea segura, cifrada o no esté sincronizada públicamente: hay que configurarlo por separado.

## Lo que todavía no implementa

Formulario, proveedor, enlace de reclutamiento, consentimiento interactivo, gestión privada de entrevistas, adaptación de exportaciones, secundarios por rol/metodología y análisis de sensibilidad del plan. No estima efectos causales, margen de error poblacional, significación estadística ni un índice validado de QA. No realiza análisis temático automático ni publica archivos.

La [validación técnica](VALIDATION.md) describe el alcance de las pruebas. El [plan de análisis](../research/ANALYSIS_PLAN.md) controla la interpretación, no la existencia de código.
