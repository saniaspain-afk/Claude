# ¿Nos sirve el Trydan? Análisis de la ISO 15118-20 (11/11/2026)

> **Actualización 12/11/2026:** Cristóbal (V2C) confirmó en el chat que el Trydan Pro **no cumple** la ISO 15118-20, que V2C no tendrá ISO hasta febrero o marzo de 2027, y que la única opción viable es instalarlo antes de 2027. Lo que sigue se mantiene; la duda sobre si el Trydan Pro la soporta ya está resuelta (no la soporta). Decisión y calendario en `propuesta_final_v5.md`.

## Respuesta
**Sí, con una condición: los dos Trydan Pro tienen que quedar instalados y en servicio en 2026.**
- **Para lo que pide la clienta, sirve:** RFID/NFC, Ethernet, cable Type 2 de 5 m, 32 A por cargador, ControlBox con balanceo en serie. [SEGURO, manuales y web de V2C]
- **Para la ISO 15118-20 no hay garantía:** V2C no dice en ningún sitio que el Trydan Pro la soporte. Su propia web escribe que la ISO 15118-20 es "donde queremos llegar", y que solo el Pole Pro soporta hoy Plug & Charge, con la ISO 15118-2. [SEGURO, web de V2C] El Trydan bidireccional con V2G y V2H, que sí necesita comunicación ISO 15118-20 con el coche, V2C lo anuncia para el primer trimestre de 2027.
- **Qué exige el texto oficial:** el punto 2.1.3 del anexo II del AFIR obliga a EN ISO 15118-20:2022 a los puntos de recarga privados de modo 3 "instalados o renovados a partir del 1 de enero de 2027". Una instalación terminada en 2026 no entra en esa frase. [SEGURO, texto de la Comisión]
- **Si la obra se va a 2027, el Trydan Pro no es una apuesta segura.** Habría que esperar a un cargador con la ISO o a una aclaración escrita de V2C y de Industria.

## Lo que dice Cristóbal, contra el texto oficial
| Afirmación de Cristóbal | Veredicto | Base |
|---|---|---|
| El Reglamento Delegado (UE) 2025/656 hace obligatoria la EN ISO 15118-20:2022 para los puntos de recarga **públicos y privados** nuevos o renovados desde el 1/1/2027 | **Casi exacto.** Públicos de CA y CC: punto 2.1.2. Privados: solo **modo 3 y 4** (punto 2.1.3.b). Los privados de **modo 2** solo deben cumplir la EN IEC 61851-1 (2.1.3.a) | Texto de la Comisión, [anexo](https://data.consilium.europa.eu/doc/document/ST-7773-2025-ADD-1/es/pdf) |
| Plug & Charge permite identificarse y pagar sin tarjetas RFID, QR o aplicaciones | Es lo que permite la norma, pero **el reglamento no obliga a usarlo**. Para los públicos dice que los operadores "pueden decidir voluntariamente" ofrecer Plug & Charge. El RFID seguirá siendo válido en un cargador con ISO | Considerandos 24 y 25, [texto completo](https://data.consilium.europa.eu/doc/document/ST-7773-2025-INIT/es/pdf) |
| Comunicación bidireccional (V2G, V2H) | La norma la hace posible. El reglamento pide aplicar la norma "según las funcionalidades obligatorias y opcionales" de cada caso de uso, no activar la bidireccionalidad | Considerando 23 |
| Protocolos cifrados contra ciberataques | Es conocimiento general de la norma; el reglamento no lo desarrolla | [PROBABLE] |
| "V2C no sabe qué hará todavía; no sabe si sacará la Alva con la ISO" | **Coherente con la web de V2C**: la ISO 15118-20 es un objetivo, no algo ya anunciado para la Alva ni para el Trydan Pro | Web de V2C |

## Cuándo se aplica: lo que está claro y lo que no
- **Claro:** el Reglamento es "directamente aplicable en cada Estado miembro" (artículo 2). Entra en vigor a los 20 días de su publicación en el DOUE y se aplica seis meses después. [SEGURO, texto de la Comisión]
- **Claro:** el considerando 22 da a los puntos privados de modo 3 y 4 un período transitorio hasta el 1/1/2027. [SEGURO]
- **Sin definir en el texto:** qué es "instalado o renovado" (compra, entrega, obra terminada, puesta en servicio o fecha del CIE). [VERIFICAR con Industria de Cádiz y V2C]
- **No encontré:** ninguna norma española que desarrolle esto para puntos privados, ni el régimen sancionador. La ITC-BT-52 consolidada que leí no menciona la ISO 15118. [VERIFICAR con Industria y MITECO]
- **No pude abrir** el texto final del DOUE (EUR-Lex bloquea el acceso automático); trabajo con el texto de la Comisión del 2/4/2025.

## ¿Se va a aplazar la fecha?
- **Petición, sin resolver:** según fuentes del sector, CharIN pidió en abril de 2026 trasladar la fecha al 1/1/2028 y escalonar el despliegue, porque los ensayos de conformidad todavía no están completos. Su [documento de posición](https://www.charin.global/media/pages/technology/knowledge-base/06a76f7571-1777821309/20260428_position-paper-clarifying-iso-15118-implementation-under-afir.pdf) lleva fecha del 28/4/2026. Una fuente secundaria dice que a octubre de 2026 no se había adoptado ningún aplazamiento. [No verificado en fuente oficial; no cuentes con él]
- **Planifica con el 1/1/2027** y trata un aplazamiento como una posibilidad, no como un dato.

## Alternativas con la ISO ya preparada
- **Wallbox Pulsar Max (anunciado en octubre de 2026):** versión residencial y compartida, 7,4 kW y 22 kW, RFID, Ethernet, Bluetooth, Wi-Fi y una capa PLC integrada "preparada para ISO 15118". Disponible en Europa a partir de noviembre de 2026, con despliegue escalonado. [Según prensa del fabricante; falta confirmar potencia monofásica, balanceo, precio y disponibilidad en España, y que **declare cumplir la EN ISO 15118-20:2022**. "Preparado" no es lo mismo que "cumple".] [VERIFICAR con Wallbox]
- **V2C:** pregunta si el Trydan Pro o un modelo nuevo llevará la ISO 15118-20, y cuándo.
- **Por qué no cambiar de marca ya:** la clienta quiere RFID y Ethernet con balanceo en serie; un cambio exige repasar todo el presupuesto y la línea de plazos, y el modelo nuevo aún no tiene stock confirmado.

## Qué hacer ahora
1. **Asegura el calendario de 2026:** equipos en obra el 4/12 como máximo, CIE de la instalación y puesta en servicio antes del 31/12. Es lo único que depende de ti.
2. **Pregunta a V2C por escrito** (añadido al mensaje de la v3, sección 9): si el Trydan Pro cumple la EN ISO 15118-20, con qué firmware o fecha, y qué considera "instalado".
3. **Opción A (la clienta compra):** dile que compre y reciba el equipo a tiempo, y que el modelo debe indicar su estado de la ISO. Sin entrega confirmada antes del 4/12, no prometas el plazo.
4. **Documenta las fechas:** factura de compra, fecha de entrega y fecha del CIE en TECI. Si hay una aclaración sobre "instalado", esas fechas serán tu prueba.
5. **Cláusula de desistimiento** por equipos no entregados el 15/12 (ya está en la opción B); no la vincules a la ISO.
6. **Carta a la clienta:** ya dice lo que se sabe, sin presión. Añadí que V2C declara la ISO 15118-20 como objetivo y que no hay confirmación de que el Trydan Pro la soporte.

## Fuentes
[Anexo del Reglamento Delegado 2025/656, texto de la Comisión](https://data.consilium.europa.eu/doc/document/ST-7773-2025-ADD-1/es/pdf) · [Texto completo con considerandos y artículos](https://data.consilium.europa.eu/doc/document/ST-7773-2025-INIT/es/pdf) · [V2C, laboratorio de pruebas ISO 15118](https://v2charge.com/v2c-advances-iso-15118-testing-lab/) · [V2C, Pole Pro con Plug & Charge ISO 15118-2](https://v2charge.com/pole-pro-plug-charge/) · [V2C, Trydan bidireccional en Power2Drive 2026](https://v2charge.com/v2c-presents-trydan-bidirectional-at-power2drive-2026-v2l-island-mode-v2g-and-v2h/) · [Documento de posición de CharIN](https://www.charin.global/media/pages/technology/knowledge-base/06a76f7571-1777821309/20260428_position-paper-clarifying-iso-15118-implementation-under-afir.pdf) · [Wallbox Pulsar Max, nota de prensa](https://www.globenewswire.com/news-release/2026/10/09/3378195/0/fr/wallbox-lance-le-nouveau-pulsar-max-avec-une-connectivit%C3%A9-renforc%C3%A9e-et-une-recharge-pens%C3%A9e-pour-les-%C3%A9volutions-futures.html)
