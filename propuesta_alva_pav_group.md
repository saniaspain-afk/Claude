# Propuesta Alva Sotogrande: revisión técnica, esquema, presupuesto y mensaje (PAV GROUP)

Preparado el 11/11/2026. Grados de certeza: **[SEGURO]** = texto oficial leído en esta sesión (BOE, manual y web de V2C, e-distribución, Junta de Andalucía); **[PROBABLE]** = criterio de ingeniería o práctica habitual, sin cita directa; **[VERIFICAR]** = no pude comprobarlo, con quién hacerlo.

Fuentes principales: [ITC-BT-52 consolidada (BOE-A-2014-13681)](https://www.boe.es/buscar/act.php?id=BOE-A-2014-13681) · [REBT consolidado (BOE-A-2002-18099)](https://www.boe.es/buscar/act.php?id=BOE-A-2002-18099) · [Ley de Propiedad Horizontal (BOE-A-1960-10906)](https://www.boe.es/buscar/act.php?id=BOE-A-1960-10906) · [Circular 3/2020 CNMC (BOE-A-2020-1066)](https://www.boe.es/buscar/act.php?id=BOE-A-2020-1066) · [Manual V2C Alva](https://v2charge.com/es/soporte/alva/manual-instalacion/) · [Ficha técnica Alva](https://v2charge.com/wp-content/uploads/2026/07/ficha-tecnica-alva.pdf) · [Tienda V2C Alva](https://v2charge.com/store/es/producto/alva/) · [e-distribución, cambio de potencia](https://www.edistribucion.com/es/servicios/conexion-red/cambio-potencia.html) · [e-distribución, guía de suministros](https://www.edistribucion.com/content/dam/edistribucion/conexion-a-la-red/descargables/guia-gestion-suministros-es7.pdf) · [Junta de Andalucía, TECI](https://www.juntadeandalucia.es/organismos/industriaenergiayminas/areas/industria/instalaciones/paginas/TECI.html)

---

## 1. Revisión técnica priorizada

| # | Hallazgo | Certeza | Acción |
|---|---|---|---|
| 1 | **Tu mensaje del 14/10 sobre las dos líneas era incorrecto.** El manual de V2C (págs. 9 y 19) muestra la versión sin protecciones con dos entradas de cable; la versión con protecciones (págs. 5, 14, 23) tiene una. La ITC-BT-52 (6.1 y 6.3) no prohíbe dos líneas: exige proteger cada punto de conexión individualmente y con automático omnipolar curva C | SEGURO | Reconocerlo (párrafo en ruso, sección 7) |
| 2 | **El límite de 40 A sí existe en el texto** de la ITC-BT-52, apartado 3.1, tabla 1 (viviendas unifamiliares: 40 A / 9.200 W; "los circuitos C13 monofásicos no dispondrán de una potencia instalada superior a los 9.200 W"). El apartado 3.2 (garajes de edificios) no lo repite. Dos circuitos de 7.360 W cumplen en cualquier lectura | SEGURO | Decirles que tenían razón en el origen de su duda |
| 3 | **Una línea de 63 A a la Alva con protecciones no se puede ofrecer todavía.** La documentación publicada no da el calibre del seccionador de entrada ni la sección máxima de bornas. V2C recomienda automático de 1,25 × la intensidad nominal (manual pág. 24): para 2 × 32 A serían 80 A, por encima del IGA de 63 A | SEGURO (documentos) / VERIFICAR con V2C | Preguntar a V2C (texto en sección 9) |
| 4 | **Con la opción B, un C63 detrás de un IGA de 63 A no tiene selectividad**: una sobrecarga de la línea de coches puede tirar el IGA de toda la vivienda. Con A, los C40 quedan por debajo del IGA | PROBABLE (criterio de ingeniería) | Argumento a favor de A |
| 5 | **El CIE de la vivienda es condicional, no siempre.** Hace falta si 14,49 kW supera la potencia máxima del boletín actual, si han pasado más de 20 años desde la última verificación, o si hubo cambio de tensión (e-distribución y Endesa) | SEGURO | Partida "incluida, con descuento íntegro si no hace falta" |
| 6 | **Omisiones del presupuesto anterior, ya corregidas:** cartel reflectante en el punto de recarga (ITC-BT-52, apartado 5); iluminación mínima de 50 lux a nivel de suelo en estaciones de interior (apartado 5); punto de conexión junto a la plaza, en envolvente fija (5.4); protección contra sobretensiones temporales **y** transitorias (6.4); circuito dedicado (apartado 5) | SEGURO | Cartel en material auxiliar; iluminación como **exclusión a comprobar** |
| 7 | **Toma de garaje: C10, no C16.** Tabla 3 de la ITC-BT-52: base UNE 20315 con automático de 10 A; 16 A solo si el fabricante de la base garantiza que queda protegida en recarga lenta de 8 h diarias. Diferencial de 30 mA clase A | SEGURO | Cambiar a C10 y avisar (sección 7) |
| 8 | **Sección del cable.** Tabla 1 del REBT (ITC-BT-19, cobre, 2 conductores XLPE, en tubo, 40 °C): 6 mm² = 44 A, 10 mm² = 60 A, 16 mm² = 80 A, 25 mm² = 106 A. 3G6 cubre un C40 con un solo circuito por tubo. Dos circuitos agrupados exigen un factor de reducción (valor habitual 0,8: 44 A × 0,8 = 35 A < 40 A; 60 A × 0,8 = 48 A ≥ 40 A) | Tabla: SEGURO · factor 0,8: VERIFICAR (UNE 20460-5-523, no la pude abrir) | **3G10 en las dos líneas**; coste extra frente a 3G6 ≈ 82 € de coste (30 m × 2,72 €) |
| 9 | **Caída de tensión:** límite 5 % hasta el punto de recarga (ITC-BT-52, apartado 5). Cálculo mío con 3G10, 32 A, 15 m: 2,2 V = 0,9 %; con 30 m: 1,9 % | Límite: SEGURO · cálculo: mío | Recalcular con metros reales |
| 10 | **Corriente continua residual (6 mA):** la ITC-BT-52 solo exige diferencial clase A. La ficha de V2C dice "AC 30 mA / DC 6 mA según modelo" y vende un detector de fugas DC como accesorio opcional | BOE: SEGURO · si falta o no en la versión sin protecciones: VERIFICAR con V2C | Partida opcional de 2 × 80,82 € coste, fuera del total |
| 11 | **Doble alimentación en una estación:** no hay prohibición en el BOE. Falta confirmar si Industria/OCA piden señalización o aviso de dos fuentes en el cuadro | VERIFICAR con Delegación Territorial de Industria de Cádiz y tu OCA | Preguntar antes de ejecutar |
| 12 | **LGA y derivación individual del edificio:** el diseñador debe comprobar que no se supera su intensidad admisible (ITC-BT-52, apartado 5); e-distribución comprueba antes de ampliar potencia si el suministro lo soporta | SEGURO | Coste no incluido si hay que cambiarlas |
| 13 | **Comunidad:** punto de recarga privado en plaza individual solo exige comunicación previa a la comunidad; coste y consumo a cargo del interesado (LPH, art. 17.5) | SEGURO (texto consolidado) | Cliente comunica por escrito |
| 14 | **RFID:** la Alva incluye 1 tarjeta. Llaveros no figuran en la documentación de Alva | SEGURO | 2 tarjetas adicionales = 3; pregunta a V2C por llaveros |
| 15 | **Posición del cargador:** el punto de conexión debe estar junto a la plaza a alimentar (5.4). No sé cuántas plazas tienen ni dónde | SEGURO / dato que falta | Preguntar |
| 16 | **Costes minoristas:** todos mis costes son PVP (V2C, Obramat, Leroy). Con tarifa de instalador el margen real sube. El coste de la hora (26,67 €) es un supuesto mío | — | Pedir tarifas y tu coste/hora real |

### Auditoría de tu mensaje del 14/10, punto por punto
| Afirmación | Veredicto | Base |
|---|---|---|
| Alva tiene RFID y Ethernet separado del conector del ControlBox | **Correcto** | Manual págs. 14 y 20 (Ethernet y Modbus por prensaestopas M16) |
| Brelki RFID de serie | **Incorrecto**: viene 1 tarjeta | Ficha técnica |
| Cada toma 32 A, ambas a la vez, ControlBox reparte | **Correcto** | Ficha técnica y web V2C |
| "Dos líneas a una estación no se permiten por ITC-BT-52" | **Incorrecto** | ITC-BT-52, 6.1 y 6.3 |
| "Solo hay una entrada de alimentación" | **Incorrecto** para la versión sin protecciones | Manual págs. 9 y 19 |
| "La norma de 40 A no existe" | **Incorrecto** como regla general (existe en 3.1, tabla 1) | ITC-BT-52 |
| Una línea de 63 A en RZ1-K (AS), 16 mm² mínimo | Sección **correcta** (80 A en tabla); no encaja con la versión sin protecciones; con protecciones **sin confirmar** | REBT ITC-BT-19 tabla 1; manual |
| Un solo diferencial 63 A tipo A para la estación | **Dudoso**: cada punto de conexión va protegido individualmente | ITC-BT-52, 6.1 |
| ~6,5 kW por coche con contrato de 63 A | **Correcto** como orden de magnitud (sección 6, pregunta 6) | Cálculo |
| Subir solo P2 a 14,49 kW | **Posible** | Circular 3/2020: la exigencia de potencias crecientes está escrita para 3.0TD y superiores, no para 2.0TD |
| Dos CIE siempre | CIE de la estación **correcto**; CIE de la vivienda **condicional** | e-distribución; Junta (TECI) |
| Toma de garaje con automático de 16 A | **Dudoso**: C10, o C16 con garantía del fabricante de la base | ITC-BT-52, tabla 3 |
| Wi-Fi 200 € | **Obsoleto** | Van por Ethernet |

---

## 2. Recomendación de esquema: **A** (Alva sin protecciones, dos líneas de 32 A desde el cuadro de su vivienda)

La ITC-BT-52 (3.2) admite en garajes de edificios el esquema 4a: circuito desde el cuadro de la vivienda, con cables y conducciones de los tipos de una derivación individual (ITC-BT-15). Aplica también la sustitución del circuito C13 por los esquemas de la ITC-BT-52 en propiedad horizontal (ITC-BT-25).

| Criterio | **A**: sin protecciones, 2 × 32 A | **B**: con protecciones, 1 × 63 A | **C**: línea desde su contador (esquema 2 o 3a) |
|---|---|---|---|
| Documentación V2C | Oficial: dos entradas (págs. 9 y 19) | Una entrada; calibre del seccionador **no publicado** | No aplica |
| ITC-BT-52 | Protección individual por punto de conexión; 7.360 W por circuito, dentro del límite de 9.200 W de 3.1 | Un circuito monofásico de 14,49 kW: 3.2 no repite el límite, pero riesgo de interpretación | Esquemas 2/3a (apartado 4.2): obra en zonas comunes y centralización de contadores |
| Precio al cliente (IVA incl.) | **5.431,57 €** | 5.685,06 € | No calculado: depende de la distancia y de la comunidad |
| Selectividad con IGA 63 A | Sí (C40 < 63 A) | No (C63 = IGA) | Según instalación |
| Legalización | 1 CIE de la estación con 2 circuitos; VERIFICAR señalización de doble alimentación | 1 circuito | Mayor: centralización y comunidad |
| Riesgo de rechazo | Bajo a medio | Medio (V2C + Industria) | Medio (comunidad y distribuidora) |
| Ventaja para el cliente | Todo dentro de su vivienda, es lo que pidieron; cada toma con protección propia | Una sola línea | Línea directa |
| Margen (costes minoristas) | 30.2 % | 29.4 % con los mismos sobreprecios | No calculado |

**Conclusión:** A. Es la única opción con documentación oficial completa, es la que piden, cumple el límite de 9.200 W por circuito y es más barata que B.

---

## 3. Presupuesto del CLIENTE (español)
Supuestos de cantidades: línea 15 m (30 m en total), UTP 30 m, garaje 15 m, 2 diferenciales a sustituir, 24 h. Todo lo marcado "a confirmar" se cierra en la visita técnica.

| # | Descripción | Cant. | Ud | Precio unit. | Importe |
|---|---|---:|---|---:|---:|
| | **Equipo** | | | | |
| 1 | Cargador V2C Alva doble, 7,4 kW por toma (monofásico, 32 A), sin protecciones integradas y sin contador MID, 2 cables Type 2 de 5 m, lector RFID con 1 tarjeta, V2C ControlBox y pinza amperimétrica incluidos, Ethernet/Wi-Fi/4G, garantía del fabricante 3 años | 1 | ud | 1.684,00 € | 1.684,00 € |
| 2 | Tarjetas RFID V2C adicionales (con la incluida suman 3) | 2 | ud | 5,20 € | 10,40 € |
| | **Líneas y canalización** | | | | |
| 3 | Dos líneas de alimentación independientes, cable RZ1-K (AS) 0,6/1 kV 3G10 mm² (cobre, libre de halógenos), una por toma, del cuadro de la vivienda al cargador (m totales, a confirmar en visita) | 30 | m | 8,70 € | 261,00 € |
| 4 | Tubo y fijaciones para las dos líneas de fuerza (m, a confirmar en visita) | 15 | m | 6,00 € | 90,00 € |
| | **Protecciones y cuadro** | | | | |
| 5 | Magnetotérmico 2P C40 curva C, uno por línea (recomendación V2C: 1,25 × 32 A) | 2 | ud | 38,00 € | 76,00 € |
| 6 | Diferencial 2P 40 A, 30 mA, tipo A superinmunizado, uno por línea (uno propio por estación: manual V2C e ITC-BT-52, apartado 6.1) | 2 | ud | 59,00 € | 118,00 € |
| 7 | Protector contra sobretensiones permanentes y transitorias (ITC-BT-52, apartado 6.4) | 1 | ud | 112,00 € | 112,00 € |
| 8 | Sustitución del IGA por magnetotérmico 2P 63 A (para 14,49 kW) | 1 | ud | 70,00 € | 70,00 € |
| 9 | Sustitución de diferenciales del cuadro de la vivienda para la nueva potencia (uds, a confirmar con foto del cuadro) | 2 | ud | 59,00 € | 118,00 € |
| 10 | Material auxiliar y señalización (bornas, punteras cuadradas, cajas, cartel reflectante exigido por ITC-BT-52, apartado 5) | 1 | ud | 150,00 € | 150,00 € |
| | **Red y comunicaciones** | | | | |
| 11 | Cable de datos UTP Cat6: ControlBox-cargador y red del router-cargador; terminan dentro del cargador, sin rosetas ni cajas en el garaje (m totales) | 30 | m | 1,20 € | 36,00 € |
| 12 | Canalización independiente de la fuerza para los cables de comunicaciones (m, a confirmar en visita) | 15 | m | 3,80 € | 57,00 € |
| | **Toma de garaje** | | | | |
| 13 | Línea independiente para la toma de garaje: cable 3G2,5 mm² RZ1-K (AS) y canalización (m, a confirmar en visita) | 15 | m | 5,10 € | 76,50 € |
| 14 | Toma de garaje para bicicletas y patinetes: magnetotérmico C10, diferencial 30 mA tipo A y base de enchufe en envolvente cerrada con llave (ITC-BT-52, tabla 3) | 1 | ud | 105,00 € | 105,00 € |
| | **Mano de obra** | | | | |
| 15 | Mano de obra: instalación, conexionado, mediciones, configuración del ControlBox, RFID y V2C Cloud, y puesta en marcha (horas, a confirmar en visita) | 24 | h | 40,00 € | 960,00 € |
| | **Legalización y gestiones** | | | | |
| 16 | Memoria técnica de diseño y CIE de la estación de recarga (ITC-BT-52, ITC-BT-04), registro en Industria (TECI, Junta de Andalucía) | 1 | ud | 275,00 € | 275,00 € |
| 17 | CIE de la vivienda para 14,49 kW y gestión del aumento de potencia en periodo P2 con la comercializadora y e-distribución. Incluido en el precio total; si su boletín actual ya admite 14,49 kW, se descuenta íntegramente | 1 | ud | 290,00 € | 290,00 € |

Subtotales: Equipo 1.694,40 € · Líneas y canalización 351,00 € · Protecciones y cuadro 644,00 € · Red y comunicaciones 93,00 € · Toma de garaje 181,50 € · Mano de obra 960,00 € · Legalización y gestiones 565,00 €

Base imponible **4.488,90 €** · IVA 21 % 942,67 € · **TOTAL 5.431,57 €**

**Detector de fugas DC V2C (opcional, no incluido en el total):** 2 uds a 122 € cada una + IVA, solo si V2C confirma que la versión sin protecciones lo necesita.

### Versión en ruso (descripciones)
| # | Описание | Кол-во | Ед. | Цена за ед. | Сумма |
|---|---|---:|---|---:|---:|
| | **Equipo** | | | | |
| 1 | Зарядная станция V2C Alva, 2 розетки по 7,4 кВт (однофазная, 32 А), без встроенных защит и без счётчика MID, 2 кабеля Type 2 по 5 м, считыватель RFID с 1 картой, V2C ControlBox и токовые клещи в комплекте, Ethernet/Wi-Fi/4G, гарантия производителя 3 года | 1 | ud | 1.684,00 € | 1.684,00 € |
| 2 | Дополнительные RFID-карты V2C (вместе с комплектной — 3 шт.) | 2 | ud | 5,20 € | 10,40 € |
| | **Líneas y canalización** | | | | |
| 3 | Две независимые питающие линии, кабель RZ1-K (AS) 0,6/1 кВ 3G10 мм² (медь, без галогенов), по одной на розетку, от щитка квартиры до станции (всего м, уточняется на визите) | 30 | m | 8,70 € | 261,00 € |
| 4 | Труба и крепёж для двух силовых линий (м, уточняется на визите) | 15 | m | 6,00 € | 90,00 € |
| | **Protecciones y cuadro** | | | | |
| 5 | Автомат 2P C40 кривая C, по одному на линию (рекомендация V2C: 1,25 × 32 А) | 2 | ud | 38,00 € | 76,00 € |
| 6 | Дифференциальный выключатель 2P 40 А, 30 мА, тип A superinmunizado, по одному на линию (свой на каждую станцию: мануал V2C и ITC-BT-52, п. 6.1) | 2 | ud | 59,00 € | 118,00 € |
| 7 | Защита от временных и импульсных перенапряжений (ITC-BT-52, п. 6.4) | 1 | ud | 112,00 € | 112,00 € |
| 8 | Замена вводного автомата (IGA) на 2P 63 А (для 14,49 кВт) | 1 | ud | 70,00 € | 70,00 € |
| 9 | Замена дифференциальных выключателей в щитке квартиры под новую мощность (шт., уточняется по фото щитка) | 2 | ud | 59,00 € | 118,00 € |
| 10 | Вспомогательные материалы и маркировка (клеммы, наконечники, коробки, светоотражающая табличка по ITC-BT-52, п. 5) | 1 | ud | 150,00 € | 150,00 € |
| | **Red y comunicaciones** | | | | |
| 11 | Сетевой кабель UTP Cat6: ControlBox—станция и роутер—станция; заканчиваются внутри станции, без розеток и коробок в гараже (всего м) | 30 | m | 1,20 € | 36,00 € |
| 12 | Отдельная от силовых линий труба для кабелей связи (м, уточняется на визите) | 15 | m | 3,80 € | 57,00 € |
| | **Toma de garaje** | | | | |
| 13 | Отдельная линия для розетки в гараже: кабель 3G2,5 мм² RZ1-K (AS) и труба (м, уточняется на визите) | 15 | m | 5,10 € | 76,50 € |
| 14 | Розетка в гараже для велосипедов и самокатов: автомат C10, дифференциал 30 мА тип A и розетка в закрытом корпусе с ключом (ITC-BT-52, таблица 3) | 1 | ud | 105,00 € | 105,00 € |
| | **Mano de obra** | | | | |
| 15 | Работа: монтаж, подключение, измерения, настройка ControlBox, RFID и V2C Cloud, пусконаладка (часы, уточняется на визите) | 24 | h | 40,00 € | 960,00 € |
| | **Legalización y gestiones** | | | | |
| 16 | Техническая записка (MTD) и CIE зарядной станции (ITC-BT-52, ITC-BT-04), регистрация в Industria (TECI, Junta de Andalucía) | 1 | ud | 275,00 € | 275,00 € |
| 17 | CIE квартиры на 14,49 кВт и оформление увеличения мощности в периоде P2 через comercializadora и e-distribución. Включено в общую цену; если ваш текущий boletín уже допускает 14,49 кВт, сумма вычитается полностью | 1 | ud | 290,00 € | 290,00 € |

Subtotales: Equipo 1.694,40 € · Líneas y canalización 351,00 € · Protecciones y cuadro 644,00 € · Red y comunicaciones 93,00 € · Toma de garaje 181,50 € · Mano de obra 960,00 € · Legalización y gestiones 565,00 €

База **4.488,90 €** · IVA 21 % 942,67 € · **ИТОГО 5.431,57 €**

---

## 4. Tabla INTERNA (no enviar)
Costes a precios minoristas. El coste/hora de 26,67 € es un supuesto (venta 40 € ÷ 1,5); sustitúyelo por tu coste real.

| # | Concepto (abrev.) | Cant. | Coste unit. | Venta unit. | Venta | Coste | Margen € | Margen % | Origen | Certeza | Pedir precio real a |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | Cargador V2C Alva doble, 7,4 kW por toma (monofásico, 32 A),… | 1 | 1.295,00 | 1.684,00 | 1.684,00 | 1.295,00 | 389,00 | 23.1 % | Oficial V2C (PVP web) | Oficial (tienda V2C, ALV-X2-32-1-L5-ES, 1.566,95 € IVA incl.) | V2C / distribuidor V2C: tarifa de instalador |
| 2 | Tarjetas RFID V2C adicionales (con la incluida suman 3)… | 2 | 3,45 | 5,20 | 10,40 | 6,90 | 3,50 | 33.7 % | Oficial V2C (PVP web) | Oficial (tarjeta RFID 4,17 € IVA incl.) | V2C |
| 3 | Dos líneas de alimentación independientes, cable RZ1-K (AS) … | 30 | 5,78 | 8,70 | 261,00 | 173,40 | 87,60 | 33.6 % | Obramat/Leroy (PVP) | PVP minorista (Leroy 3G10 6,99 €/m IVA incl.) | Saltoki/Rexel/Sonepar: tarifa |
| 4 | Tubo y fijaciones para las dos líneas de fuerza (m, a confir… | 15 | 4,00 | 6,00 | 90,00 | 60,00 | 30,00 | 33.3 % | ESTIMACIÓN | ESTIMACIÓN | Saltoki/Rexel/Sonepar |
| 5 | Magnetotérmico 2P C40 curva C, uno por línea (recomendación … | 2 | 25,00 | 38,00 | 76,00 | 50,00 | 26,00 | 34.2 % | ESTIMACIÓN | ESTIMACIÓN (precio del presupuesto anterior) | Saltoki/Rexel/Sonepar |
| 6 | Diferencial 2P 40 A, 30 mA, tipo A superinmunizado, uno por … | 2 | 39,26 | 59,00 | 118,00 | 78,52 | 39,48 | 33.5 % | Obramat/Leroy (PVP) | PVP minorista (Obramat Schneider 47,50 € IVA incl.) | Saltoki/Rexel/Sonepar |
| 7 | Protector contra sobretensiones permanentes y transitorias (… | 1 | 74,02 | 112,00 | 112,00 | 74,02 | 37,98 | 33.9 % | Obramat/Leroy (PVP) | PVP minorista (Leroy Toscano COMBI 2P50T15 89,57 € IVA incl.); validar calibre | Saltoki/Rexel/Sonepar |
| 8 | Sustitución del IGA por magnetotérmico 2P 63 A (para 14,49 k… | 1 | 46,45 | 70,00 | 70,00 | 46,45 | 23,55 | 33.6 % | Obramat/Leroy (PVP) | PVP minorista (Obramat Hager 56,21 € IVA incl.) | Saltoki/Rexel/Sonepar |
| 9 | Sustitución de diferenciales del cuadro de la vivienda para … | 2 | 39,26 | 59,00 | 118,00 | 78,52 | 39,48 | 33.5 % | Obramat/Leroy (PVP) | PVP minorista (Obramat Schneider); unidades por confirmar | Saltoki/Rexel/Sonepar |
| 10 | Material auxiliar y señalización (bornas, punteras cuadradas… | 1 | 100,00 | 150,00 | 150,00 | 100,00 | 50,00 | 33.3 % | ESTIMACIÓN | ESTIMACIÓN | Tu histórico de obras |
| 11 | Cable de datos UTP Cat6: ControlBox-cargador y red del route… | 30 | 0,76 | 1,20 | 36,00 | 22,80 | 13,20 | 36.7 % | Obramat/Leroy (PVP) | PVP minorista (Obramat Cat6A 0,92 €/m IVA incl.) | Saltoki/Rexel/Sonepar |
| 12 | Canalización independiente de la fuerza para los cables de c… | 15 | 2,50 | 3,80 | 57,00 | 37,50 | 19,50 | 34.2 % | ESTIMACIÓN | ESTIMACIÓN | Saltoki/Rexel/Sonepar |
| 13 | Línea independiente para la toma de garaje: cable 3G2,5 mm² … | 15 | 3,40 | 5,10 | 76,50 | 51,00 | 25,50 | 33.3 % | Obramat/Leroy (PVP) | PVP minorista (cable Obramat 1,40 €/m sin IVA) + tubo estimado 2,00 | Saltoki/Rexel/Sonepar |
| 14 | Toma de garaje para bicicletas y patinetes: magnetotérmico C… | 1 | 70,00 | 105,00 | 105,00 | 70,00 | 35,00 | 33.3 % | ESTIMACIÓN | ESTIMACIÓN | Saltoki/Rexel/Sonepar |
| 15 | Mano de obra: instalación, conexionado, mediciones, configur… | 24 | 26,67 | 40,00 | 960,00 | 640,00 | 320,00 | 33.3 % | Tarifa 40 €/h | SUPUESTO: coste real/hora no conocido | Tu coste real por hora (salario + SS + furgoneta) |
| 16 | Memoria técnica de diseño y CIE de la estación de recarga (I… | 1 | 150,00 | 275,00 | 275,00 | 150,00 | 125,00 | 45.5 % | ESTIMACIÓN | ESTIMACIÓN (coste del presupuesto anterior) | Tu tramitador/ingeniería colaboradora |
| 17 | CIE de la vivienda para 14,49 kW y gestión del aumento de po… | 1 | 200,00 | 290,00 | 290,00 | 200,00 | 90,00 | 31.0 % | ESTIMACIÓN | ESTIMACIÓN | Tu tramitador/ingeniería colaboradora |

Venta base **4.488,90 €** · coste **3.134,11 €** · margen **1.354,79 €** (**30.2 %** sobre venta). Sin CIE de la vivienda: base 4.198,90 €, margen 30.1 %.

**Reglas de precio aplicadas:** materiales coste × 1,5; cargador coste × 1,3 (PVP web sin IVA 1.295,00 €); mano de obra 40 €/h; CIE de la estación 275 € y CIE de la vivienda 290 €. Precios unitarios redondeados al alza (a 1 € si ≥ 20 €, a 0,10 € si menos). El margen sale ≥ 30 % con y sin el CIE de la vivienda, con costes minoristas; con tarifa de instalador será mayor.

---

## 5. Opciones de precio y alcance
| Opción | Base | IVA 21 % | Total | Margen |
|---|---:|---:|---:|---:|
| **1. A llave en mano (recomendada)** | 4.488,90 € | 942,67 € | **5.431,57 €** | 30.2 % |
| 1b. Igual si el boletín ya admite 14,49 kW (sin CIE vivienda) | 4.198,90 € | 881,77 € | 5.080,67 € | 30.1 % |
| 2. A por fases: Fase 1 (equipo, líneas, protecciones, red, toma, mano de obra, CIE estación) | 4.010,90 € | 842,29 € | 4.853,19 € | — |
| 2. A por fases: Fase 2 (IGA, diferenciales, CIE vivienda y gestión) | 478,00 € | 100,38 € | 578,38 € | — |
| 3. A por medición (horas reales a 40 €/h): 20 h / 28 h | — | — | 5.237,97 € / 5.625,17 € | ≥ 30 % |
| 4. El cliente compra la Alva en la web de V2C (1.566,95 € IVA incl.); nosotros instalamos y legalizamos | 2.804,90 € | 589,03 € | 3.393,93 € | 34.4 % |
| 5. Referencia B: con protecciones, 1 × 63 A (**no ofrecer** hasta respuesta de V2C) | 4.698,40 € | 986,66 € | 5.685,06 € | 29.4 % |

**Recomendación:** ofrecer la **1 (llave en mano)** presentada **por fases (2)**: mismo importe, pero la Fase 1 se ejecuta y se legaliza sin depender de e-distribución, y responde a su pregunta sobre Navidad. Reservar la **4** como último recurso ante la objeción del precio del cargador: mantiene un margen del 34.4 %.

### Estrategia para el precio del cargador
- Tienda V2C: **1.566,95 € IVA incl.** (1.295,00 € sin IVA). Nuestra Alva: **1.684,00 € + IVA = 2.037,64 € con IVA**, es decir 470,69 € más que la web.
- Con costes minoristas, el suelo del 30 % de margen total está en una base de unos 4.477 € (5.418 € con IVA). Si el cargador se muestra al precio web, el resto de partidas tendría que subir mucho; no lo recomiendo.
- **Antes de enviar, pide la tarifa de instalador de V2C** (V2C tiene programa para instaladores). Si el descuento sobre PVP supera el 23 %, puedes mostrar el cargador al precio de la web y seguir en ≥ 30 % de margen. Con la tarifa real, repite el cálculo en la hoja `Interno`.
- Justificación del valor frente a la web: ControlBox y pinza configurados, RFID dado de alta en V2C Cloud, puesta en marcha y pruebas, CIE a nuestro nombre, garantía de 3 años del fabricante gestionada por PAV GROUP.

### Qué ha cambiado frente al presupuesto del 13/10 (para la carta)
El 13/10 enviaste la Alva a **4.883,89 € IVA incl.** (base 4.036,27 €). Ahora: **5.431,57 €** (+547,68 €). Desglose, **suponiendo** que las partidas siguientes no estaban en el presupuesto 00039 (confírmalo con el PDF, que no estaba en el zip):

| Concepto | IVA incl. |
|---|---:|
| Presupuesto del 13/10 | 4.883,89 € |
| Lo que ya estaba (equipo, línea, protecciones, mano de obra, legalización de la estación), ahora | 4.521,04 € (**-362,85 €**) |
| Nuevo por sus peticiones desde el 13/10: toma de garaje (219,62 €), IGA y diferenciales (227,48 €), red y tubo aparte (112,53 €), CIE de la vivienda (350,90 €) | 910,52 € |
| Total ahora | 5.431,57 € |
| Wi-Fi que ya no hace falta | 200 € + IVA de ahorro |

Si el CIE de la vivienda no hace falta, el total baja a **5.080,67 €**.

**Partidas dobles revisadas:** "fijaciones" estaba en tubo y en material auxiliar; ya solo está en tubo. Las horas incluyen mediciones y puesta en marcha; el CIE incluye la memoria y la tramitación, no horas de obra.

---

## 6. Condiciones y exclusiones
- **Validez:** 30 días; el precio del equipo sigue la tarifa de V2C.
- **Pago (propuesta tuya a decidir):** 40 % al aceptar (pedido del equipo), 40 % al terminar la instalación, 20 % al entregar los CIE registrados. La Fase 2 se factura al ejecutarse.
- **Ejecución:** unas 3 jornadas (24 h) desde que llega el equipo; los plazos de e-distribución y de la Junta no los controlamos.
- **Garantía:** equipo 3 años (V2C, oficial). Instalación: propuesta de 2 años, decisión tuya; no verifiqué el marco legal.
- **No incluido:** obra civil, albañilería y acabados · derivación individual, LGA o centralización del edificio si no admiten 14,49 kW · iluminación del garaje si no llega a 50 lux a nivel de suelo (ITC-BT-52, apartado 5) · comunicación a la comunidad (LPH, art. 17.5) · tasas administrativas, derechos de acceso o extensión y costes de e-distribución (los factura la comercializadora) · configuración del router y de la red del cliente · detector de fugas DC si V2C lo exige · ayudas y subvenciones.
- **Cambios tras la visita técnica:** metros, diferenciales y horas se liquidan a precio unitario; la hora sigue a 40 € + IVA.
- **Si el boletín ya admite 14,49 kW:** se descuenta el CIE de la vivienda (350,90 € con IVA).

---

## 7. Mensaje en ruso, corrección y objeciones
Ver `mensaje_clienta_ru.md`.

## 8. Preguntas técnicas (certeza)
1. **Corriente continua residual 6 mA:** el BOE solo exige clase A [SEGURO]; si la versión sin protecciones necesita el detector DC [VERIFICAR: V2C].
2. **Límite de 40 A:** existe en 3.1 tabla 1 para unifamiliares; no se repite en 3.2 [SEGURO]. IGA máximo de 63 A: 14,49 kW es potencia contratable en 2.0TD (≤ 15 kW, Circular 3/2020) [SEGURO]; ITC-BT-10 no la abrí [VERIFICAR].
3. **Un CIE para una estación con dos entradas:** el procedimiento TECI cubre la recarga de interior hasta 50 kW sin modo 4 [SEGURO]; práctica de Industria/OCA con doble alimentación [VERIFICAR: Delegación de Industria de Cádiz, tu OCA].
4. **Derivación individual para 14,49 kW:** la comprueba e-distribución antes de ampliar potencia [SEGURO]; si hay que cambiarla es coste no incluido [SEGURO]. Dato: foto de la derivación y boletín.
5. **Solo P2:** el peaje 2.0TD no exige potencias crecientes, tope 15 kW [SEGURO, Circular 3/2020]; compatible con el equipo de medida (RD 1110/2007 citado por la circular) [VERIFICAR: comercializadora]. El **titular pide el aumento a su comercializadora** (potencia final ≤ 15 kW); **e-distribución hace los trabajos** y **la comercializadora cobra el coste** [SEGURO]. Solo se cambia una vez al año [SEGURO]. "Registro del aumento en Endesa" = preparar el CIE y la documentación; la solicitud la firma el titular.
6. **Potencia por coche** = (14,49 kW − consumo de la vivienda) ÷ 2, con tope de 7,36 kW: consumo 0,5 kW → 7,0 kW · 1 kW → 6,7 kW · **1,5 kW → 6,5 kW** · 2 kW → 6,2 kW · 3 kW → 5,7 kW [cálculo]. El ControlBox lo ajusta en tiempo real.
7. **Red:** Cat6 hasta 100 m [SEGURO como norma general de cableado, no de V2C]. Longitud máxima del cable ControlBox-Alva [VERIFICAR: V2C]. Ethernet y Modbus entran por prensaestopas M16 y terminan en la placa [SEGURO]. **Riesgo no visto:** la Alva trae también Wi-Fi, Bluetooth y 4G, y por defecto se conecta por 4G (manual V2C). Para su exigencia de aislamiento hay que preguntar a V2C cómo desactivar esas radios [VERIFICAR].
8. **Plazo hasta Navidad:** ver calendario.

## 9. Calendario realista desde hoy (miércoles 11/11/2026)
| Semana | Qué pasa | Quién lo controla |
|---|---|---|
| 11–13/11 | Enviar presupuesto y mensaje. Enviar la pregunta a V2C. Pedir tarifas | Tú |
| 16–20/11 | Decisión del cliente. **Visita técnica martes 17/11 o jueves 19/11.** Boletín, foto del cuadro y datos de la comunidad. Borrador de la memoria técnica | Tú y cliente |
| 23–27/11 | Pedido de la Alva al aceptar. La web de V2C dice que Alva tiene "un plazo de preparación y envío superior al habitual", **sin cifra**. Cliente comunica a la comunidad. Cliente consulta a e-distribución si el suministro admite la potencia | V2C, cliente |
| 30/11–4/12 | **Fecha límite para tener la Alva en mano** si se quiere instalar antes de Navidad | V2C |
| 7–11/12 | Ejecución (≈ 3 jornadas) y pruebas | Tú |
| 14–18/12 | CIE de la estación por TECI; puesta en servicio. Solicitud del aumento de potencia con el CIE de la vivienda si hace falta | Tú, cliente |
| 21–24/12 | e-distribución: para potencia final ≤ 15 kW aplica tratamiento abreviado y los plazos de respuesta se reducen a la mitad (guía de e-distribución); no publica plazo de ejecución para un simple cambio de potencia | e-distribución |

**Lo que puedes prometer:** estación instalada, certificada y en servicio antes de Navidad **si V2C entrega antes del 4/12**. **Lo que no puedes prometer:** el aumento a 14,49 kW antes de Navidad. Mientras tanto el ControlBox reparte la potencia contratada actual.

## 10. Datos que faltan y preguntas
**Para el cliente:** boletín actual (potencia máxima y fecha) · potencia contratada en P1 y P2 · foto del cuadro · número de plazas, si son individuales y su posición respecto al cargador · distancia del cuadro al garaje y recorrido · ¿hay iluminación suficiente en el garaje? · ubicación del router · nombre del administrador de la comunidad.

**Para ti:** tarifa de instalador de V2C y de Saltoki, Rexel o Sonepar · tu coste real por hora · precio real de la memoria técnica y de los dos CIE con tu tramitador · respuesta de V2C (llaveros, seccionador de la versión con protecciones, detector DC, desactivar Wi-Fi/Bluetooth/4G) · respuesta de Industria/OCA (doble alimentación) · el PDF 00039 del 13/10 para confirmar el desglose · qué garantía de instalación quieres dar.

**Pregunta a V2C (envíala antes del mensaje):**
> Buenos días. Vamos a instalar una Alva (ALV-X2-32-1-L5-ES y ALV-X2-32-1-L5-P-ES). 1) ¿Qué frecuencia y tipo de chip lee el lector RFID? ¿Aceptan llaveros o solo la tarjeta V2C? 2) En la versión con protecciones, ¿cuál es el calibre del seccionador de entrada y la sección máxima de bornas? ¿Se admite una línea única de 63 A para las dos tomas de 32 A? 3) ¿La versión sin protecciones necesita el detector de fugas DC para cumplir la ITC-BT-52 en España? 4) ¿Longitud máxima del cable UTP entre el ControlBox y la Alva? 5) ¿Cómo se desactivan Wi-Fi, Bluetooth y 4G para dejar solo Ethernet?
