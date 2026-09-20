# Privacidad, consentimiento y protección de participantes

**Borrador; no constituye asesoría jurídica ni certificación de cumplimiento. Recolección deshabilitada hasta completar LAUNCH_CHECKLIST.md.** Referencias [R4, R9, R10](../references/REFERENCES.md).

## 1. Modelo de riesgo

El riesgo incluye reidentificación y consecuencias laborales por opiniones sobre prácticas internas. Pueden identificar a alguien una combinación de rol y antigüedad, una voz, un incidente singular, un horario o un texto buscable. Quitar el nombre no basta. Considerar también accesos del proveedor, administradores, respaldos, dispositivos laborales y posibles requerimientos legales.

No prometer anonimato absoluto, secreto profesional que no exista ni inmunidad frente a represalias. Explicar el riesgo residual con lenguaje comprensible. No solicitar documentos, nombres, secretos, datos de clientes ni hechos que el participante no pueda compartir legítimamente.

## 2. Tres espacios separados

| Espacio | Contenido | Acceso/publicación |
| --- | --- | --- |
| Repositorio público | Protocolo, instrumentos, código, síntesis y agregados revisados | Público; historial copiable |
| Almacenamiento privado de investigación | Encuestas sin identificadores directos y notas de entrevistas seudonimizadas | Personas autorizadas; cifrado; fuera de GitHub |
| Agenda/consentimientos de entrevistas | Contacto mínimo, alias, consentimientos y código interno | Separado, cifrado, acceso más restringido |

No unir respuestas de encuesta con agenda de entrevistas mediante códigos, cookies, marcas horarias o enlaces individuales. La invitación a entrevista será un enlace general independiente, sin transmitir identificadores de encuesta. Una entrevista puede ser de alguien que no respondió la encuesta.

## 3. Encuesta: diseño de minimización

No solicitar nombre, correo, empresa, dominio, perfil, país concreto, edad exacta, fecha de incidente, tickets ni texto libre. Solo confirmar mayoría de edad y experiencia elegible. No requerir inicio de sesión, carga de archivos, correo corporativo ni cuenta GitHub.

Antes de usar un proveedor, comprobar si recopila IP, geolocalización, user-agent, cookies, analytics, identificadores de dispositivo o tiempos exactos, y quién puede acceder. Desactivar lo que no sea necesario y eliminar metadatos innecesarios de la exportación analítica. No decir que el proveedor no conserva registros sin verificarlo; explicar sus límites en el consentimiento real. El proyecto todavía no ha elegido proveedor.

No utilizar fingerprinting ni IP para deduplicar. Solicitar un solo envío y aceptar la limitación. No almacenar respuestas rechazadas por falta de consentimiento. No recoger respuestas parciales antes de enviar, salvo cambio autorizado y explicado; por defecto el cierre sin envío no guarda respuestas para investigación.

Después del envío, una encuesta sin identificador de recuperación no puede localizarse por nombre para retirar una fila. Debe informarse antes de aceptar. El ejercicio de derechos aplicables y casos en que sí sea identificable se evaluarán con el responsable; no se usarán las limitaciones técnicas como renuncia general de derechos.

## 4. Entrevistas: confidencialidad, no anonimato garantizado

Aceptar alias y formato escrito; no exigir nombre real. El entrevistador o proveedor puede conocer datos de contacto o reconocer una voz, por lo que se describe como confidencial y seudonimizada. Grabación desactivada por defecto; autorización separada si fuese necesaria. No grabar video.

Asignar un código aleatorio no basado en nombre, empresa o correo. Mantener cualquier relación código-contacto en la agenda separada. Interrumpir y reformular cuando aparezcan identificadores. Redactar notas desidentificadas y conservar el mínimo contenido. No enviar audios, transcripciones o encuestas reales a servicios de IA generalistas; cualquier excepción exige revisión específica, permisos y transparencia previa.

Retiro propuesto: hasta 14 días después de la entrevista, usando el canal privado y código. No anonimizar de forma irreversible ni publicar fragmentos antes de vencer ese plazo. Después, explicar qué datos aún pueden localizarse y qué agregados ya no pueden desagregarse. Esto no sustituye derechos legales aplicables.

Participar no implica autorizar citas literales. El permiso de cita es independiente; el rechazo no impide participar. Por defecto publicar temas y paráfrasis no identificables. No publicar seudónimos persistentes que permitan reconstruir perfiles mediante varias citas. Un agradecimiento nominal, si alguien lo solicita, exige opt-in separado y no se vincula con respuestas; por defecto no hay lista pública de participantes.

## 5. Retención propuesta y revisión legal

Propuesta a confirmar antes del consentimiento final: contactos hasta 30 días después del cierre del plazo de retiro; audios autorizados hasta verificar notas/transcripción y, como máximo, 30 días tras la entrevista; encuestas y notas seudonimizadas hasta 12 meses después del cierre del campo; después eliminar originales y respaldos en su ciclo documentado. Si una obligación legal/editorial exige otro plazo, resolverlo antes de reclutar y comunicar el plazo real. No conservar indefinidamente por si acaso.

Asignar responsable de tratamiento y canal privado con identificación y datos de contacto que correspondan. En Colombia revisar Ley 1581 de 2012 y reglamentación aplicable, proveedores y transmisiones/transferencias internacionales; la finalidad científica no autoriza cualquier uso ni publicación. La aplicabilidad de otras jurisdicciones depende del alcance y tratamiento, no se presupone ni se descarta. Solicitar evaluación competente antes de abrir.

## 6. Seguridad técnica y organizativa

Cifrado en tránsito y reposo, credenciales individuales, autenticación multifactor, acceso mínimo, respaldos cifrados, registro de accesos y procedimiento de eliminación. No usar cuentas o dispositivos de empleadores para almacenar datos de investigación. No conceder a empleadores acceso a respuestas ni listas de participación.

Git no es un almacén privado de datos. .gitignore, hooks y pruebas solo reducen errores: no impiden todos los envíos ni borran el historial. Si hay una exposición, detener publicación, limitar acceso, conservar únicamente evidencia mínima segura y aplicar SECURITY.md. Una eliminación del último commit no retira forks ni copias.

## 7. Publicación y revisión

Solo agregados revisados y síntesis temática. Regla inicial N>=20 y ninguna celda no nula<5 para una tabla; si falla, omitir la tabla completa. Evaluar además combinaciones, diferencias entre versiones y texto. Los umbrales no garantizan anonimato. No proporcionar tablas a medida que permitan reconstrucción.

Revisión ética y revisión de privacidad son necesarias también para el piloto. No declarar riesgo mínimo o exención por cuenta propia cuando corresponda una determinación independiente. Si no se resuelven los resguardos, el repositorio seguirá como protocolo sin recoger datos.
