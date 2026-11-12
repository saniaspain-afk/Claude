# Mensajes para Cristóbal (V2C), listos para copiar en WhatsApp

> **Actualización 12/11/2026:** Cristóbal ya contestó que el Trydan Pro no cumple la ISO y que V2C no tendrá ISO hasta feb/mar de 2027. De este mensaje siguen pendientes: stock, plazo y reserva de 2 Trydan Pro (pregunta 3 del mensaje 1), tarifa de instalador (pregunta 6) y todas las dudas técnicas del mensaje 2. Las preguntas 1, 2 y 5 del mensaje 1 ya no hacen falta.

Sin datos personales de la clienta. Se mandan en dos mensajes: el primero resume el caso y pide lo esencial; el segundo trae las dudas técnicas. Pídele que conteste por escrito.

## Mensaje 1: resumen y opción viable

Hola Cristóbal, gracias por la info de la ISO. Te resumo el caso para ver qué opción viable tenemos con el Trydan Pro.

**La clienta** (apartamento con garaje comunitario en Sotogrande) quiere cargar 2 coches a la vez por la noche, ~7,4 kW cada uno (hoy híbridos enchufables, después eléctricos):
• 2 puntos monofásicos de 32 A con cable Type 2 de 5 m.
• Arranque y bloqueo con llavero o tarjeta RFID, sin móvil (en el garaje no hay cobertura).
• Internet solo por Ethernet, sin Wi-Fi. El cable de red termina dentro del cargador, sin rosetas ni cajas, y va en tubo aparte de la fuerza.
• Balanceo con ControlBox y pinza. Contrato de 14,49 kW solo en el periodo nocturno.
• Cada cargador con su línea de 32 A desde el cuadro de la vivienda (unos 7 m).

Pidió la Alva sin protecciones con dos líneas, pero por lo que nos cuentas V2C aún no sabe si la sacará con la ISO. **Propuesta:** 2 Trydan Pro monofásicos (TRYPRO32-1-L5-ES), cada uno con su línea de 32 A, balanceo en serie con un solo ControlBox (uno maestro y otro extra por los terminales A y B).

**Sobre la norma:** según el anexo II del AFIR (Reglamento Delegado 2025/656, punto 2.1.3), los puntos de recarga privados de modo 3 instalados o renovados desde el 1/1/2027 deben cumplir la EN ISO 15118-20. Mi plan es dejar los dos Trydan Pro instalados, certificados y en servicio antes del 31/12/2026. ¿Lo veis viable desde V2C? Necesito que me confirmes por escrito:

1. ¿El Trydan Pro cumple hoy la EN ISO 15118-20? Si no, ¿habrá actualización de firmware o versión nueva, y para cuándo?
2. ¿Qué considera V2C "instalado" a efectos del 1/1/2027: entrega, instalación, CIE o puesta en servicio?
3. ¿Stock y plazo de entrega de 2 Trydan Pro monofásicos? Los necesito en obra antes del 4/12.
4. ¿Qué pasa con la Alva: retirada, en revisión o saldrá con ISO? ¿Hay fecha?
5. ¿Habrá algún modelo V2C con ISO 15118-20 en 2027 (el Trydan bidireccional con V2G/V2H)? ¿Cuándo y a qué precio?
6. ¿Tarifa de instalador para el Trydan Pro?

Si prefieres lo hablamos por teléfono. Gracias por la ayuda.

## Mensaje 2: dudas técnicas del Trydan Pro

Y estas son las dudas técnicas, por si me las puedes resolver tú o pasarlas al técnico:

1. **Puertos.** El Trydan Pro tiene un RJ45 para Ethernet y otro RJ45 para el balanceador (ControlBox). ¿Confirmas que el del ControlBox es RS485/Modbus y no Ethernet, y que no se pueden mezclar? ¿Qué cable recomendáis (Cat6 UTP, T-568A o B)?
2. **Balanceo en serie.** ControlBox al maestro por RJ45 y el extra por los terminales A y B. ¿Qué cable usar para el A/B? ¿Longitud máxima del enlace A/B (tendremos unos 5 m) y del cable ControlBox–maestro (unos 7 m)? ¿Dónde se activan las resistencias de polarización?
3. **Internet en el extra.** ¿El cargador extra necesita Internet (Ethernet o Wi-Fi) para RFID, e-Keys y V2C Cloud, o le basta el enlace A/B con el maestro?
4. **Radios.** ¿Se pueden desactivar Wi-Fi, Bluetooth y 4G dejando solo Ethernet? ¿Qué se pierde sin Bluetooth (e-Keys, configuración local)? La clienta es muy estricta con la seguridad de red.
5. **Red.** ¿Qué dominios, puertos y protocolos salientes usa el cargador con V2C Cloud? Lo preguntamos porque el segmento de red estará filtrado. ¿Va con DHCP o con IP fija?
6. **RFID.** ¿Qué frecuencia y tipo de chip lee? ¿Acepta llaveros MIFARE Classic de 13,56 MHz? ¿Funciona sin Internet? ¿Se puede dar de alta una tarjeta por su código UID? Cada Trydan Pro trae 1 tarjeta: ¿se pueden usar las mismas tarjetas en los dos cargadores?
7. **e-Key Bluetooth.** ¿Un mismo llavero BLE se puede dar de alta en los dos cargadores?
8. **Protecciones.** ¿Calibre de magnetotérmico recomendado para 32 A (C32 o C40) y sección de cable? ¿Hace falta el detector de fugas DC (V2C-F) en España? ¿Hace falta protector de sobretensiones junto al cargador, estando a unos 7 m del cuadro?
9. **Garantía.** ¿Garantía comercial del Trydan Pro y cómo es el proceso de reparación o cambio?

Muchas gracias, Cristóbal. Cuanto antes me contestes, antes puedo cerrar con la clienta.
