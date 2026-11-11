# Verificación oficial: qué es posible y qué no (Alva Sotogrande)

Cada punto lleva su fuente oficial. Lo que no está en una fuente oficial figura como "no verificado".

## 1. Lo que pide la clienta y qué dice la fuente oficial
| Petición | Resultado | Fuente oficial |
|---|---|---|
| Alva doble, 2 cables Tipo 2 de 5 m, 7,4 kW por toma, monofásica | **Posible.** Existe la referencia ALV-X2-32-1-L5-ES (sin protecciones) y ALV-X2-32-1-L5-P-ES (con protecciones) | [Tienda V2C](https://v2charge.com/store/es/producto/alva/) |
| Tipo 2 de 32 A en garaje de edificio de viviendas | **Posible.** Tabla 3 de la ITC-BT-52 lo permite en "aparcamientos en edificios de viviendas" | [BOE, ITC-BT-52, apartado 5.4](https://www.boe.es/buscar/act.php?id=BOE-A-2014-13681) |
| Dos líneas de 32 A, una por toma | **Posible.** El manual de V2C (págs. 9 y 19) muestra la versión sin protecciones con dos entradas de cable. La ITC-BT-52 (6.1 y 6.3) exige protección individual de cada punto de conexión, no una línea única | [Manual V2C](https://v2charge.com/es/soporte/alva/manual-instalacion/), BOE |
| Una línea de 63 A a la versión con protecciones | **No se puede ofrecer todavía.** El manual (pág. 14) muestra una sola entrada, pero la documentación publicada no indica el calibre del seccionador de entrada ni la sección máxima de bornas. V2C recomienda un automático de 1,25 x la intensidad nominal | Manual V2C, pág. 24 |
| RFID para arrancar y bloquear | **Posible con tarjeta.** La Alva incluye 1 tarjeta RFID; V2C vende la tarjeta a 4,17 € con IVA. V2C Cloud permite dar de alta la tarjeta acercándola al cargador o escribiendo su código | [Ficha técnica Alva](https://v2charge.com/wp-content/uploads/2026/07/ficha-tecnica-alva.pdf), [V2C Cloud](https://v2charge.com/es/soporte/v2c-cloud/configuracion-v2c-cloud/) |
| RFID con **llavero** | **No documentado.** La documentación de V2C para Alva solo habla de tarjetas. Los e-Keys tipo llavero (Bluetooth) figuran para Trydan y Trydan Pro, no para Alva | V2C Cloud (enlace anterior) |
| ControlBox con pinza | **Incluidos en la Alva** (no hay que comprarlos). El ControlBox va al cargador con cable UTP de 8 hilos (RJ45, T-568A/B) y la pinza abraza la acometida general | [V2C ControlBox](https://v2charge.com/es/soporte/control-potencia/dinamico/medidores-cableados/v2c-controlbox/), manual pág. 30 |
| Ethernet por cable | **Posible.** El cable Ethernet entra por el prensaestopas M16 a la placa de la puerta. Requiere DHCP automático o IP estática | Manual V2C págs. 14 y 20, [soporte Alva](https://v2charge.com/es/soporte/alva/manual-instalacion/) |
| Cables de comunicación en tubo aparte, sin cajas ni tomas en el garaje | **Posible.** Ethernet y Modbus entran por prensaestopas del cargador | Manual V2C |
| Toma de garaje para bicis y patinetes, con llave | **Posible.** Tabla 3: base UNE 20315 con automático de 10 A (16 A solo si el fabricante de la base lo garantiza), diferencial de 30 mA clase A por punto de conexión | BOE, ITC-BT-52, 5.4 y 6.1 |
| Aumento de potencia a 14,49 kW | **Posible**, con trámite de e-distribución. Antes de pedirlo a la comercializadora hay que consultar a e-distribución si el suministro lo soporta. Solo se puede cambiar la potencia una vez al año | [e-distribución, potencia contratada](https://www.edistribucion.com/es/consumo-electrico/potencia-contratada.html) |
| CIE de la vivienda | **Solo si** 14,49 kW supera la potencia máxima del boletín actual, o han pasado más de 20 años desde la última verificación, o hubo cambio de tensión | [e-distribución, cambio de potencia](https://www.edistribucion.com/es/servicios/conexion-red/cambio-potencia.html) |
| Documentación de la estación | **MTD + CIE, sin proyecto**: "No será necesaria la elaboración de proyecto para las instalaciones de recarga ... existentes en edificios de viviendas". En Andalucía se tramita por TECI (recarga no modo 4, no exterior, hasta 50 kW) | BOE (ITC-BT-04 modificada), [Junta de Andalucía, TECI](https://www.juntadeandalucia.es/organismos/industriaenergiayminas/areas/industria/instalaciones/paginas/TECI.html) |

## 2. Correcciones a tu mensaje del 14/10
1. **"Dos líneas a una estación no se permite por ITC-BT-52"**: falso. La ITC-BT-52 no lo prohíbe. Exige protección individual de cada punto de conexión (6.1 y 6.3). V2C lo diseña así en la versión sin protecciones.
2. **"Solo hay una entrada de alimentación"**: falso para la versión sin protecciones (manual V2C, págs. 9 y 19).
3. **"Un límite de 40 A no existe"**: la ITC-BT-52, apartado 3.1, Tabla 1, fija para viviendas unifamiliares un máximo de 40 A y 9.200 W por circuito monofásico: "los circuitos C13 monofásicos no dispondrán de una potencia instalada superior a los 9.200 W". Para garajes de edificios (3.2) ese límite no se repite. El presupuesto A queda dentro de él (2 circuitos de 7.360 W).
4. **"CIE de la vivienda siempre"**: solo en los tres casos de e-distribución.
5. **Diferencial "tipo A + 6 mA CC"**: ni el BOE ni el manual de V2C lo exigen. V2C pide diferencial tipo A superinmunizado de 30 mA como máximo y uno propio por estación. El detector de fugas DC es un accesorio opcional de V2C, no incluido en el presupuesto.
6. **Automático**: V2C recomienda 1,25 x la intensidad nominal, o sea C40 para cada toma de 32 A, no C32.
7. **Sección**: tabla 1 del REBT (ITC-BT-19, cobre, tubo, 2 conductores XLPE, 40 °C): 6 mm² en tubo aguanta 44 A, suficiente para C40. Los 16 mm² (80 A) y 25 mm² (106 A) solo harían falta para la línea de 63 A.

## 3. Pendiente de V2C (envía esto antes de la carta)
> Buenos días. Vamos a instalar una Alva (ALV-X2-32-1-L5-ES y ALV-X2-32-1-L5-P-ES). 1) ¿Qué tipo de tag lee el lector RFID: aceptan llaveros o solo la tarjeta V2C? ¿Frecuencia y chip? 2) En la versión con protecciones, ¿cuál es el calibre del seccionador de entrada y la sección máxima de las bornas? ¿Se admite una línea única de 63 A para las dos tomas a 32 A? 3) ¿La versión sin protecciones necesita el detector de fugas DC para cumplir la ITC-BT-52 en España?

Con la respuesta 2 se puede preparar el presupuesto B (con protecciones, una línea de 63 A). Hoy no se envía.

## 4. Datos que faltan de la clienta
- Boletín (CIE) actual de la vivienda: potencia máxima autorizada y fecha.
- Foto del cuadro eléctrico de la vivienda.
- Distancia del cuadro al garaje y si se puede pasar tubo.
- Si su comunidad exige un esquema concreto (ITC-BT-52, apartado 3.2).

## 5. No verificado en fuente oficial
- Potencia distinta en P1 y P2 con el peaje 2.0TD (lo cita la CNMC; no abrí el documento primario). Confirmarlo con la comercializadora.
- Tasas administrativas del trámite TECI.
- Precios de instalador (Saltoki, Rexel, Sonepar) y los marcados ESTIMACIÓN en el Excel.
