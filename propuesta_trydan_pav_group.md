# Propuesta Trydan Pro para Sotogrande: revisión técnica, esquema, presupuesto y calendario (PAV GROUP)

Preparado el 11/11/2026. Grados de certeza: **[SEGURO]** = texto oficial leído en esta sesión (BOE, manuales y web de V2C, e-distribución, Junta de Andalucía, anexo del Reglamento Delegado 2025/656); **[PROBABLE]** = criterio de ingeniería o práctica, sin cita directa; **[VERIFICAR]** = no pude comprobarlo, con quién hacerlo.

## Resumen
- **La Alva queda fuera.** Cristóbal, representante de V2C, lo confirma en el audio: V2C retira la Alva y la razón es la ISO 15118-20, sobre la que la marca aún no ha decidido. No pude oír el audio; lo tomo como me lo has contado. No hay mensaje escrito y la web de V2C todavía muestra la Alva a la venta. Para la clienta basta citar el texto oficial del anexo; si ella pide una prueba, pide un mensaje escrito a Cristóbal. No es condición para enviar.
- **Solución propuesta: dos V2C Trydan Pro**, cada uno con su línea independiente de 32 A desde el cuadro de la vivienda. Es lo que recomendaste el 13/10, y ahora está probado que cubre lo que pide la clienta: RFID/NFC y Ethernet (solo el Pro los tiene), e-Key Bluetooth con llaveros, y balanceo de potencia entre los dos cargadores con un ControlBox.
- **Precio: 5.897,06 € con IVA** (base 4.873,60 €), margen 30.2 % con costes minoristas. Sin el CIE de la vivienda: 5.546,16 €.
- **Fecha límite: 31/12/2026.** El anexo del Reglamento Delegado (UE) 2025/656 exige EN ISO 15118-20 a los puntos de recarga privados de modo 3 instalados o renovados desde el 1/1/2027. La Alva retirada no es un caso aislado: la norma se aplica al punto de recarga, sea del modelo que sea.
- **Corrección a mi análisis anterior:** los llaveros sí son posibles (e-Key Bluetooth de V2C SmartLock), y la web oficial lo dice para Alva, Trydan y Trydan Pro.

---

## 1. Revisión técnica priorizada
| # | Hallazgo | Certeza | Acción |
|---|---|---|---|
| 1 | **Tu mensaje del 14/10 era incorrecto en tres puntos.** (a) El manual de la Alva (págs. 9 y 19) muestra dos entradas de cable en la versión sin protecciones. (b) La ITC-BT-52 (6.1 y 6.3) no prohíbe dos líneas: exige proteger cada punto de conexión por separado. (c) El límite de 40 A existe en 3.1, tabla 1 (viviendas unifamiliares: 40 A / 9.200 W por circuito monofásico) | SEGURO | Reconocerlo (carta). Con dos cargadores, dos circuitos de 7.360 W cumplen en cualquier lectura |
| 2 | **Alva retirada por V2C, confirmado por Cristóbal en el audio** (motivo: ISO 15118-20). La web de V2C aún la vende (30 variantes en stock, con aviso de plazo de envío superior al habitual) | Audio: según me cuentas · web: SEGURO | Guardar el audio. Pedir un mensaje escrito solo si la clienta lo reclama |
| 3 | **ISO 15118-20.** Anexo II del AFIR, punto 2.1.3 (texto del anexo transmitido al Consejo el 2/4/2025): los puntos de recarga **privados** de CA y CC "instalados o renovados a partir del 1 de enero de 2027 cumplirán ... EN ISO 15118-20:2022 (para el modo 3 o el modo 4)". La obligación depende de la fecha de instalación | SEGURO (texto del anexo) · DOUE final y aplicación en España: VERIFICAR | **Instalar y poner en servicio antes del 31/12/2026**; preguntar a V2C si el Trydan Pro cumple |
| 4 | **Balanceo entre dos Trydan Pro: es posible.** V2C documenta el balanceo dinámico entre varios Trydan y Trydan Pro: conexión en serie (la recomendada, hasta 10 cargadores): ControlBox 2.0 al cargador maestro con cable UTP Cat6 y dos hilos (azul y blanco/azul) a los terminales A y B de cada cargador extra, activando las resistencias de polarización; o por router común (Wi-Fi o Ethernet, Ethernet solo en Pro) con todos en la misma subred | SEGURO ([V2C, balanceo entre e-Chargers](https://v2charge.com/es/soporte/control-potencia/dinamico/balanceo-echargers/)) | Conexión en serie en el presupuesto |
| 5 | **ControlBox y pinza vienen incluidos** con Trydan, Trydan Pro y Alva. Con dos cargadores solo hace falta uno | SEGURO | No hay línea de ControlBox |
| 6 | **Trydan normal no sirve; hace falta el Pro.** La web oficial dice que el Trydan normal no tiene RFID ni gestión de varios usuarios. El Pro sí (RFID y NFC; Wi-Fi, 4G o Ethernet) | SEGURO | Dos Trydan Pro |
| 7 | **Llaveros: sí, como e-Key Bluetooth.** SmartLock (Trydan, Trydan Pro y Alva) acepta llaveros, mandos, relojes y tarjetas BLE con **MAC fija**: el cargador se desbloquea al detectar el e-Key cerca y se bloquea al alejarse. En Trydan y Trydan Pro necesita firmware 1.7 o posterior. Cada Trydan Pro trae además 1 tarjeta RFID (manual). Llaveros **RFID** (no Bluetooth): sin dato | SEGURO ([V2C SmartLock](https://v2charge.com/es/soporte/trydan/configuracion-smartlock/), manual Trydan Pro) | 3 llaveros BLE en el presupuesto; probar un modelo antes de pedir |
| 8 | **El CIE de la vivienda es condicional.** Hace falta si 14,49 kW supera la potencia máxima del boletín, si han pasado más de 20 años desde la última verificación, o si hubo cambio de tensión | SEGURO (e-distribución, Endesa) | Partida incluida, con descuento íntegro si no hace falta |
| 9 | **Omisiones del presupuesto anterior, ya corregidas:** cartel reflectante (ITC-BT-52, apartado 5); iluminación de 50 lux a nivel de suelo en estaciones de interior (apartado 5, exclusión a comprobar); punto de conexión junto a la plaza, en envolvente fija (5.4); sobretensiones temporales **y** transitorias (6.4); circuito dedicado | SEGURO | Cartel en material auxiliar |
| 10 | **Toma de garaje: C10, no C16.** Tabla 3: base UNE 20315 con automático de 10 A; 16 A solo con garantía del fabricante de la base. Diferencial de 30 mA clase A | SEGURO | Cambiar y avisar |
| 11 | **Automático C40 vs C32.** El manual de la Alva recomendaba 1,25 × la intensidad (C40). El manual del Trydan Pro deja el calibre al instalador ("según la placa de características y la línea"). La ITC-BT-52 (6.3) permite que supere la intensidad del cargador por tolerancias y consumo propio | SEGURO (textos) · calibre exacto: VERIFICAR con V2C | C40 con cable 3G10 |
| 12 | **Sección:** tabla 1 del REBT (ITC-BT-19, cobre, tubo, 2 conductores XLPE, 40 °C): 6 mm² = 44 A, 10 mm² = 60 A, 16 mm² = 80 A. Dos circuitos agrupados llevan un factor de reducción (valor habitual 0,8): 6 mm² → 35 A < 40 A; 10 mm² → 48 A ≥ 40 A | Tabla: SEGURO · factor 0,8: VERIFICAR (UNE 20460-5-523, no la abrí) | 3G10 |
| 13 | **Caída de tensión:** límite 5 % hasta el punto de recarga (ITC-BT-52, apartado 5). Mi cálculo con 3G10 y 32 A: 7 m → 0,4 %; 12 m → 0,7 %; 15 m → 0,9 % | Límite: SEGURO · cálculo: mío | Recalcular con metros reales |
| 14 | **Corriente continua residual (6 mA):** el BOE solo exige diferencial clase A. La web de V2C vende un detector de fugas DC como accesorio opcional también para el Trydan Pro | BOE: SEGURO · necesidad: VERIFICAR con V2C | Partida opcional, fuera del total |
| 15 | **Sobretensiones:** el manual del Trydan Pro no menciona un protector integrado. La ITC-BT-52 (6.4) pide protector transitorio cerca del origen o en el cuadro principal; según la distancia puede hacer falta otro junto a la estación | SEGURO (BOE) · distancia: VERIFICAR | Protector en el cuadro, incluido |
| 16 | **LGA y derivación individual del edificio:** el diseñador debe comprobar que no se supera su intensidad admisible (ITC-BT-52, apartado 5); e-distribución comprueba antes de ampliar potencia si el suministro lo soporta | SEGURO | Coste no incluido si hay que cambiarlas |
| 17 | **Comunidad:** punto de recarga privado en plaza individual solo exige comunicación previa a la comunidad; coste y consumo a cargo del interesado (LPH, art. 17.5) | SEGURO | Cliente comunica por escrito |
| 18 | **Posición de los cargadores:** cada punto de conexión va junto a su plaza (5.4). Dos cargadores separados encajan mejor con dos plazas. No sé si las plazas son contiguas ni cuántas hay | SEGURO / dato que falta | Preguntar |
| 19 | **Costes minoristas:** mis costes son PVP (V2C, Obramat, Leroy). Con tarifa de instalador el margen real sube. El coste/hora (26,67 €) es un supuesto mío | — | Pedir tarifas y tu coste/hora |

### Auditoría de tu mensaje del 14/10
| Afirmación | Veredicto | Base |
|---|---|---|
| RFID y Ethernet separados del ControlBox en Alva | Correcto | Manual Alva págs. 14 y 20 |
| "Брелки" RFID de serie | Incorrecto: viene 1 tarjeta por cargador | Ficha Alva, manual Trydan Pro |
| Dos líneas a una estación no se permiten | Incorrecto | ITC-BT-52, 6.1 y 6.3 |
| Alva solo tiene una entrada | Incorrecto para la versión sin protecciones | Manual Alva págs. 9 y 19 |
| "La norma de 40 A no existe" | Incorrecto como regla general | ITC-BT-52, 3.1, tabla 1 |
| Una línea de 63 A, 16 mm² mínimo | Sección correcta (80 A en tabla); ya no aplica con dos cargadores | REBT ITC-BT-19 |
| ~6,5 kW por coche con contrato de 63 A | Correcto como orden de magnitud | Cálculo |
| Subir solo P2 a 14,49 kW | Posible | Circular 3/2020: potencias crecientes solo para 3.0TD y superiores |
| Dos CIE siempre | Estación: correcto; vivienda: condicional | e-distribución; Junta (TECI) |
| Toma de garaje con automático de 16 A | Dudoso: C10 | ITC-BT-52, tabla 3 |
| Wi-Fi 200 € | Obsoleto | Van por Ethernet |

---

## 2. Esquema recomendado: dos Trydan Pro, dos circuitos independientes (esquema 4a de la ITC-BT-52)
La ITC-BT-52 (3.2) admite en garajes de edificios el esquema 4a: circuito desde el cuadro de la vivienda con cables y conducciones de los tipos de una derivación individual (ITC-BT-15).

| Criterio | **Dos Trydan Pro, 2 × 32 A** | Alva sin protecciones, 2 × 32 A | Una línea de 63 A (Alva con protecciones) |
|---|---|---|---|
| Disponibilidad | Web V2C: en stock; plazo sin dato | **Retirada por V2C (audio)** | Retirada |
| Documentación V2C | Oficial: RFID/NFC, Ethernet, balanceo entre cargadores, e-Key | Oficial | Calibre del seccionador no publicado |
| ITC-BT-52 | Un punto de conexión por circuito; 7.360 W por circuito, dentro del límite de 9.200 W de 3.1 | Dos entradas en un equipo: sin prohibición, señalización por verificar | Circuito de 14,49 kW: riesgo de interpretación |
| Precio al cliente (IVA incl.) | **5.897,06 €** | 5.012,67 € | 5.365,87 € |
| Verificación pendiente | Balanceo en serie, ISO | Doble alimentación, ISO | Todo lo anterior |

**Conclusión:** dos Trydan Pro. Ventajas: cada cargador y cada línea son independientes (una avería no afecta al otro), cada punto de conexión queda junto a su plaza, desaparece la duda de la doble alimentación en un solo equipo. Desventajas: más caro que la Alva, y hay un cable más entre cargadores.

---

## 3. Presupuesto del CLIENTE (español)
Supuestos de cantidades: cuadro a 7 m del cargador maestro (dato tuyo), 5 m entre los dos cargadores (estimación), 19 m de línea de fuerza en total, 12 m de tubo, 26 m de UTP, toma de garaje 15 m (sin dato), 2 diferenciales a sustituir, 22 h (sección 11). Todo lo marcado "a confirmar" se cierra en la visita técnica.

| # | Descripción | Cant. | Ud | Precio unit. | Importe |
|---|---|---:|---|---:|---:|
| | **Equipos** | | | | |
| 1 | Dos cargadores V2C Trydan Pro monofásicos, 7,4 kW (32 A) cada uno, cable liso Tipo 2 de 5 m, sin protecciones integradas y sin contador MID, lector RFID/NFC, Ethernet/Wi-Fi/4G, con V2C ControlBox y pinza amperimétrica incluidos (un cargador hace de maestro del balanceo de potencia) | 2 | ud | 1.099,00 € | 2.198,00 € |
| 2 | Llaveros e-Key Bluetooth (BLE, dirección MAC fija) para bloquear y desbloquear por proximidad con V2C SmartLock (3 uds) | 3 | ud | 12,00 € | 36,00 € |
| | **Líneas y canalización** | | | | |
| 3 | Dos líneas de alimentación independientes, cable RZ1-K (AS) 0,6/1 kV 3G10 mm² (cobre, libre de halógenos), una por cargador, del cuadro de la vivienda a cada cargador (m totales, a confirmar en visita) | 19 | m | 8,70 € | 165,30 € |
| 4 | Tubo y fijaciones para las líneas de fuerza (m, a confirmar en visita) | 12 | m | 6,00 € | 72,00 € |
| | **Protecciones y cuadro** | | | | |
| 5 | Magnetotérmico 2P C40 curva C, uno por línea (ITC-BT-52, apartado 6.3: el calibre puede superar la intensidad del cargador por tolerancias y consumo propio) | 2 | ud | 38,00 € | 76,00 € |
| 6 | Diferencial 2P 40 A, 30 mA, tipo A superinmunizado, uno por línea (uno propio por cargador: ITC-BT-52, apartado 6.1) | 2 | ud | 59,00 € | 118,00 € |
| 7 | Protector contra sobretensiones permanentes y transitorias (ITC-BT-52, apartado 6.4) | 1 | ud | 112,00 € | 112,00 € |
| 8 | Sustitución del IGA por magnetotérmico 2P 63 A (para 14,49 kW) | 1 | ud | 70,00 € | 70,00 € |
| 9 | Sustitución de diferenciales del cuadro de la vivienda para la nueva potencia (uds, a confirmar con foto del cuadro) | 2 | ud | 59,00 € | 118,00 € |
| 10 | Material auxiliar y señalización (bornas, punteras, cajas, cartel reflectante exigido por ITC-BT-52, apartado 5) | 1 | ud | 180,00 € | 180,00 € |
| | **Red y comunicaciones** | | | | |
| 11 | Cable UTP Cat6: ControlBox-cargador maestro, router-cada cargador y enlace maestro-extra para el balanceo. Terminan dentro de los cargadores, sin rosetas ni cajas en el garaje (m totales) | 26 | m | 1,20 € | 31,20 € |
| 12 | Canalización independiente de la fuerza para los cables de comunicaciones (m, a confirmar en visita) | 12 | m | 3,80 € | 45,60 € |
| | **Toma de garaje** | | | | |
| 13 | Línea independiente para la toma de garaje: cable 3G2,5 mm² RZ1-K (AS) y canalización (m, a confirmar en visita) | 15 | m | 5,10 € | 76,50 € |
| 14 | Toma de garaje para bicicletas y patinetes: magnetotérmico C10, diferencial 30 mA tipo A y base de enchufe en envolvente cerrada con llave (ITC-BT-52, tabla 3) | 1 | ud | 105,00 € | 105,00 € |
| | **Mano de obra** | | | | |
| 15 | Mano de obra: instalación de los dos cargadores, conexionado, mediciones, configuración del balanceo, e-Keys y V2C Cloud, y puesta en marcha (horas, a confirmar en visita) | 22 | h | 40,00 € | 880,00 € |
| | **Legalización y gestiones** | | | | |
| 16 | Memoria técnica de diseño y CIE de la instalación de recarga, dos cargadores (ITC-BT-52, ITC-BT-04), registro en Industria (TECI, Junta de Andalucía) | 1 | ud | 300,00 € | 300,00 € |
| 17 | CIE de la vivienda para 14,49 kW y gestión del aumento de potencia en periodo P2 con la comercializadora y e-distribución. Incluido en el precio total; si su boletín actual ya admite 14,49 kW, se descuenta íntegramente | 1 | ud | 290,00 € | 290,00 € |

Subtotales: Equipos 2.234,00 € · Líneas y canalización 237,30 € · Protecciones y cuadro 674,00 € · Red y comunicaciones 76,80 € · Toma de garaje 181,50 € · Mano de obra 880,00 € · Legalización y gestiones 590,00 €

Base imponible **4.873,60 €** · IVA 21 % 1.023,46 € · **TOTAL 5.897,06 €**

**Detector de fugas DC V2C (opcional, no incluido en el total):** 2 uds a 122 € cada una + IVA, solo si V2C confirma que hace falta.

### Versión en ruso (descripciones)
| # | Описание | Кол-во | Ед. | Цена за ед. | Сумма |
|---|---|---:|---|---:|---:|
| | **Equipos** | | | | |
| 1 | Две зарядные станции V2C Trydan Pro, однофазные, по 7,4 кВт (32 А), кабель Type 2 длиной 5 м, без встроенных защит и без счётчика MID, считыватель RFID/NFC, Ethernet/Wi-Fi/4G, V2C ControlBox и токовые клещи в комплекте (одна станция — ведущая в балансировке мощности) | 2 | ud | 1.099,00 € | 2.198,00 € |
| 2 | Брелки e-Key Bluetooth (BLE, фиксированный MAC) для блокировки и разблокировки по приближению, V2C SmartLock (3 шт.) | 3 | ud | 12,00 € | 36,00 € |
| | **Líneas y canalización** | | | | |
| 3 | Две независимые питающие линии, кабель RZ1-K (AS) 0,6/1 кВ 3G10 мм² (медь, без галогенов), по одной на станцию, от щитка квартиры до каждой станции (всего м, уточняется на визите) | 19 | m | 8,70 € | 165,30 € |
| 4 | Труба и крепёж для силовых линий (м, уточняется на визите) | 12 | m | 6,00 € | 72,00 € |
| | **Protecciones y cuadro** | | | | |
| 5 | Автомат 2P C40 кривая C, по одному на линию (ITC-BT-52, п. 6.3: номинал может превышать ток станции из-за допусков и собственного потребления) | 2 | ud | 38,00 € | 76,00 € |
| 6 | Дифференциальный выключатель 2P 40 А, 30 мА, тип A superinmunizado, по одному на линию (свой на каждую станцию: ITC-BT-52, п. 6.1) | 2 | ud | 59,00 € | 118,00 € |
| 7 | Защита от временных и импульсных перенапряжений (ITC-BT-52, п. 6.4) | 1 | ud | 112,00 € | 112,00 € |
| 8 | Замена вводного автомата (IGA) на 2P 63 А (для 14,49 кВт) | 1 | ud | 70,00 € | 70,00 € |
| 9 | Замена дифференциальных выключателей в щитке квартиры под новую мощность (шт., уточняется по фото щитка) | 2 | ud | 59,00 € | 118,00 € |
| 10 | Вспомогательные материалы и маркировка (клеммы, наконечники, коробки, светоотражающая табличка по ITC-BT-52, п. 5) | 1 | ud | 180,00 € | 180,00 € |
| | **Red y comunicaciones** | | | | |
| 11 | Кабель UTP Cat6: ControlBox—ведущая станция, роутер—каждая станция и связь ведущая—ведомая для балансировки. Заканчиваются внутри станций, без розеток и коробок в гараже (всего м) | 26 | m | 1,20 € | 31,20 € |
| 12 | Отдельная от силовых линий труба для кабелей связи (м, уточняется на визите) | 12 | m | 3,80 € | 45,60 € |
| | **Toma de garaje** | | | | |
| 13 | Отдельная линия для розетки в гараже: кабель 3G2,5 мм² RZ1-K (AS) и труба (м, уточняется на визите) | 15 | m | 5,10 € | 76,50 € |
| 14 | Розетка в гараже для велосипедов и самокатов: автомат C10, дифференциал 30 мА тип A и розетка в закрытом корпусе с ключом (ITC-BT-52, таблица 3) | 1 | ud | 105,00 € | 105,00 € |
| | **Mano de obra** | | | | |
| 15 | Работа: монтаж двух станций, подключение, измерения, настройка балансировки, e-Key и V2C Cloud, пусконаладка (часы, уточняется на визите) | 22 | h | 40,00 € | 880,00 € |
| | **Legalización y gestiones** | | | | |
| 16 | Техническая записка (MTD) и CIE установки зарядки, две станции (ITC-BT-52, ITC-BT-04), регистрация в Industria (TECI, Junta de Andalucía) | 1 | ud | 300,00 € | 300,00 € |
| 17 | CIE квартиры на 14,49 кВт и оформление увеличения мощности в периоде P2 через comercializadora и e-distribución. Включено в общую цену; если ваш текущий boletín уже допускает 14,49 кВт, сумма вычитается полностью | 1 | ud | 290,00 € | 290,00 € |

Subtotales: Equipos 2.234,00 € · Líneas y canalización 237,30 € · Protecciones y cuadro 674,00 € · Red y comunicaciones 76,80 € · Toma de garaje 181,50 € · Mano de obra 880,00 € · Legalización y gestiones 590,00 €

База **4.873,60 €** · IVA 21 % 1.023,46 € · **ИТОГО 5.897,06 €**

---

## 4. Tabla INTERNA (no enviar)
El coste/hora de 26,67 € es un supuesto (venta 40 € ÷ 1,5); sustitúyelo por tu coste real. Precios unitarios redondeados al alza.

| # | Concepto (abrev.) | Cant. | Coste unit. | Venta unit. | Venta | Coste | Margen € | Margen % | Origen | Pedir precio real a |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Dos cargadores V2C Trydan Pro monofásicos, 7,4 kW (32 A… | 2 | 832,50 | 1.099,00 | 2.198,00 | 1.665,00 | 533,00 | 24.2 % | Oficial V2C (PVP web) | V2C / distribuidor V2C: tarifa de instalador |
| 2 | Llaveros e-Key Bluetooth (BLE, dirección MAC fija) para… | 3 | 8,00 | 12,00 | 36,00 | 24,00 | 12,00 | 33.3 % | ESTIMACIÓN | Proveedor de llaveros BLE con MAC fija; comprar 1 para probar |
| 3 | Dos líneas de alimentación independientes, cable RZ1-K … | 19 | 5,78 | 8,70 | 165,30 | 109,82 | 55,48 | 33.6 % | Obramat/Leroy (PVP) | Saltoki/Rexel/Sonepar: tarifa |
| 4 | Tubo y fijaciones para las líneas de fuerza (m, a confi… | 12 | 4,00 | 6,00 | 72,00 | 48,00 | 24,00 | 33.3 % | ESTIMACIÓN | Saltoki/Rexel/Sonepar |
| 5 | Magnetotérmico 2P C40 curva C, uno por línea (ITC-BT-52… | 2 | 25,00 | 38,00 | 76,00 | 50,00 | 26,00 | 34.2 % | ESTIMACIÓN | Saltoki/Rexel/Sonepar |
| 6 | Diferencial 2P 40 A, 30 mA, tipo A superinmunizado, uno… | 2 | 39,26 | 59,00 | 118,00 | 78,52 | 39,48 | 33.5 % | Obramat/Leroy (PVP) | Saltoki/Rexel/Sonepar |
| 7 | Protector contra sobretensiones permanentes y transitor… | 1 | 74,02 | 112,00 | 112,00 | 74,02 | 37,98 | 33.9 % | Obramat/Leroy (PVP) | Saltoki/Rexel/Sonepar |
| 8 | Sustitución del IGA por magnetotérmico 2P 63 A (para 14… | 1 | 46,45 | 70,00 | 70,00 | 46,45 | 23,55 | 33.6 % | Obramat/Leroy (PVP) | Saltoki/Rexel/Sonepar |
| 9 | Sustitución de diferenciales del cuadro de la vivienda … | 2 | 39,26 | 59,00 | 118,00 | 78,52 | 39,48 | 33.5 % | Obramat/Leroy (PVP) | Saltoki/Rexel/Sonepar |
| 10 | Material auxiliar y señalización (bornas, punteras, caj… | 1 | 120,00 | 180,00 | 180,00 | 120,00 | 60,00 | 33.3 % | ESTIMACIÓN | Tu histórico de obras |
| 11 | Cable UTP Cat6: ControlBox-cargador maestro, router-cad… | 26 | 0,76 | 1,20 | 31,20 | 19,76 | 11,44 | 36.7 % | Obramat/Leroy (PVP) | Saltoki/Rexel/Sonepar |
| 12 | Canalización independiente de la fuerza para los cables… | 12 | 2,50 | 3,80 | 45,60 | 30,00 | 15,60 | 34.2 % | ESTIMACIÓN | Saltoki/Rexel/Sonepar |
| 13 | Línea independiente para la toma de garaje: cable 3G2,5… | 15 | 3,40 | 5,10 | 76,50 | 51,00 | 25,50 | 33.3 % | Obramat/Leroy (PVP) | Saltoki/Rexel/Sonepar |
| 14 | Toma de garaje para bicicletas y patinetes: magnetotérm… | 1 | 70,00 | 105,00 | 105,00 | 70,00 | 35,00 | 33.3 % | ESTIMACIÓN | Saltoki/Rexel/Sonepar |
| 15 | Mano de obra: instalación de los dos cargadores, conexi… | 22 | 26,67 | 40,00 | 880,00 | 586,67 | 293,33 | 33.3 % | Tarifa 40 €/h | Tu coste real por hora (salario + SS + furgoneta) |
| 16 | Memoria técnica de diseño y CIE de la instalación de re… | 1 | 150,00 | 300,00 | 300,00 | 150,00 | 150,00 | 50.0 % | ESTIMACIÓN | Tu tramitador/ingeniería colaboradora |
| 17 | CIE de la vivienda para 14,49 kW y gestión del aumento … | 1 | 200,00 | 290,00 | 290,00 | 200,00 | 90,00 | 31.0 % | ESTIMACIÓN | Tu tramitador/ingeniería colaboradora |

Venta base **4.873,60 €** · coste **3.401,76 €** · margen **1.471,84 €** (**30.2 %**). Sin CIE de la vivienda: base 4.583,60 €, margen 30.1 %.

**Reglas de precio:** materiales coste × 1,5 · cargadores coste × 1,32 (PVP web sin IVA 832,50 € cada uno) · mano de obra 40 €/h · CIE de la instalación 300 € y CIE de la vivienda 290 €. El margen sale ≥ 30 % con y sin el CIE de la vivienda, con costes minoristas; con tarifa de instalador será mayor.

---

## 5. Opciones de precio y alcance
| Opción | Base | IVA 21 % | Total | Margen |
|---|---:|---:|---:|---:|
| **1. Llave en mano: dos Trydan Pro (recomendada)** | 4.873,60 € | 1.023,46 € | **5.897,06 €** | 30.2 % |
| 1b. Si el boletín ya admite 14,49 kW (sin CIE vivienda) | 4.583,60 € | 962,56 € | 5.546,16 € | 30.1 % |
| 2. Por fases: Fase 1 (cargadores, líneas, protecciones, red, toma, mano de obra, CIE instalación) | 4.395,60 € | 923,08 € | 5.318,68 € | — |
| 2. Por fases: Fase 2 (IGA, diferenciales, CIE vivienda y gestión) | 478,00 € | 100,38 € | 578,38 € | — |
| 3. Por medición (horas reales a 40 €/h): 18 h / 26 h | — | — | 5.703,46 € / 6.090,66 € | ≥ 30 % |
| 4. El cliente compra los dos Trydan Pro en la web V2C (2.014,66 € IVA incl.); nosotros instalamos y legalizamos | 2.675,60 € | 561,88 € | 3.237,48 € | 35.1 % |

**Recomendación:** ofrecer la **1 presentada por fases (2)**: mismo importe; la Fase 1 se ejecuta y legaliza sin depender de e-distribución y responde a su pregunta sobre Navidad. La **4** queda como último recurso ante la objeción del precio de los cargadores; mantiene un 35.1 % de margen.

### Estrategia para el precio de los cargadores
- Tienda V2C: **1.007,33 € IVA incl.** cada uno (2.014,66 € los dos). Nuestros dos Trydan Pro: **2.659,58 € con IVA**, es decir 644,92 € más que la web.
- Con costes minoristas, el suelo del 30 % de margen total está en una base de unos 4.860 € (5.880 € con IVA).
- **Antes de enviar, pide la tarifa de instalador de V2C.** Si el descuento sobre PVP supera el 21,8 %, puedes mostrar los cargadores al precio de la web y seguir en ≥ 30 % de margen.
- Valor frente a la web: ControlBox y balanceo configurados, e-Keys dados de alta en V2C Cloud, puesta en marcha y pruebas, CIE a nuestro nombre y gestión de la garantía del fabricante (plazo de garantía del Trydan Pro: [VERIFICAR con V2C]).

### Qué ha cambiado frente al presupuesto de dos Trydan del 13/10
El 13/10 enviaste los dos Trydan a **5.500,19 € IVA incl.** (PDF 00040, que no tengo). Ahora **5.897,06 €** (+396,87 €). Desglose, **suponiendo** que las partidas nuevas no estaban en ese PDF (confírmalo):

| Concepto | IVA incl. |
|---|---:|
| Presupuesto del 13/10 | 5.500,19 € |
| Lo que ya estaba, ahora | 4.962,57 € (**-537,62 €**) |
| Nuevo por sus peticiones: llaveros e-Key (43,56 €), toma de garaje (219,62 €), IGA y diferenciales (227,48 €), red y tubo aparte (92,93 €), CIE de la vivienda (350,90 €) | 934,48 € |
| Total ahora | 5.897,06 € |
| Wi-Fi que ya no hace falta | 200 € + IVA de ahorro |

Si el CIE de la vivienda no hace falta, el total baja a **5.546,16 €**. Partidas dobles revisadas: las fijaciones solo aparecen en el tubo; las horas incluyen mediciones y puesta en marcha, el CIE incluye memoria y tramitación.

---

## 6. Condiciones y exclusiones
- **Validez:** 30 días; el precio de los equipos sigue la tarifa de V2C.
- **Pago (propuesta tuya a decidir):** 40 % al aceptar (pedido de los equipos), 40 % al terminar la instalación, 20 % al entregar los CIE registrados. La Fase 2 se factura al ejecutarse.
- **Ejecución:** unas 3 jornadas (22 h) desde que llegan los equipos; los plazos de e-distribución y de la Junta no los controlamos.
- **Garantía:** equipos, la del fabricante (plazo del Trydan Pro por confirmar con V2C). Instalación: propuesta de 2 años, decisión tuya; no verifiqué el marco legal.
- **No incluido:** obra civil y acabados · derivación individual, LGA o centralización del edificio si no admiten 14,49 kW · iluminación del garaje si no llega a 50 lux a nivel de suelo (ITC-BT-52, apartado 5) · comunicación a la comunidad (LPH, art. 17.5) · tasas administrativas, derechos de acceso o extensión y costes de e-distribución (los factura la comercializadora) · configuración del router y de la red del cliente · detector de fugas DC si V2C lo exige · ayudas y subvenciones.
- **Cambios tras la visita:** metros, diferenciales y horas se liquidan a precio unitario; la hora sigue a 40 € + IVA.
- **Si el boletín ya admite 14,49 kW:** se descuenta el CIE de la vivienda (350,90 € con IVA).
- **Fecha tope de entrega:** si los equipos no están en obra antes del 15/12/2026 y la instalación pasa a 2027, la clienta puede desistir con devolución de lo pagado (propuesta tuya a decidir).

---

## 7. Preguntas técnicas (certeza)
1. **Corriente continua residual 6 mA:** el BOE solo exige clase A [SEGURO]; si el Trydan Pro necesita el detector DC [VERIFICAR: V2C].
2. **Límite de 40 A:** existe en 3.1 tabla 1 para unifamiliares; no se repite en 3.2 [SEGURO]. Dos circuitos de 32 A cumplen en cualquier lectura.
3. **CIE de la instalación de recarga:** el procedimiento TECI cubre la recarga de interior hasta 50 kW sin modo 4 [SEGURO]. Con dos cargadores independientes ya no hay doble alimentación en un equipo.
4. **Derivación individual para 14,49 kW:** la comprueba e-distribución antes de ampliar potencia [SEGURO]; si hay que cambiarla es coste no incluido. Dato: boletín y foto de la derivación.
5. **Solo P2:** el peaje 2.0TD no exige potencias crecientes y tiene tope de 15 kW [SEGURO, Circular 3/2020]; compatibilidad con el equipo de medida (RD 1110/2007) [VERIFICAR: comercializadora]. El titular pide el aumento a su comercializadora (potencia final ≤ 15 kW); e-distribución hace los trabajos y la comercializadora cobra el coste; solo se cambia una vez al año [SEGURO].
6. **Potencia por coche** = (14,49 kW − consumo de la vivienda) ÷ 2, con tope de 7,36 kW: 0,5 kW → 7,0 kW · 1 kW → 6,7 kW · **1,5 kW → 6,5 kW** · 2 kW → 6,2 kW · 3 kW → 5,7 kW [cálculo]. El balanceo de V2C lo ajusta en tiempo real.
7. **Red:** Ethernet solo en Trydan Pro, DHCP automático o IP estática, cable al puerto de la placa de control [SEGURO, manual]. Cat6 hasta 100 m [norma general de cableado]. Longitud máxima del enlace A/B entre cargadores [VERIFICAR: V2C]. **Riesgo para su exigencia de aislamiento:** el Trydan Pro trae Wi-Fi, Bluetooth y 4G; hay que preguntar a V2C cómo desactivar las radios que no usen. Los e-Keys necesitan Bluetooth [VERIFICAR].
8. **Un e-Key para dos cargadores:** la página de SmartLock dice que se asigna a un e-Charger al darlo de alta; no dice si un mismo llavero puede darse de alta en los dos [VERIFICAR: V2C].

## 8. Calendario realista desde hoy (miércoles 11/11/2026)
| Semana | Qué pasa | Quién lo controla |
|---|---|---|
| 11–13/11 | Pedir a Cristóbal disponibilidad, plazo y precio de los dos Trydan Pro. Enviar el presupuesto y el mensaje. Preguntas a V2C | Tú |
| 16–20/11 | Decisión del cliente. **Visita técnica martes 17/11 o jueves 19/11.** Boletín, foto del cuadro y datos de la comunidad. Borrador de la memoria técnica | Tú y cliente |
| 23–27/11 | Pedido de los dos Trydan Pro al aceptar. Cliente comunica a la comunidad y consulta a e-distribución si el suministro admite la potencia. Probar un llavero BLE | V2C, cliente |
| 30/11–4/12 | **Fecha límite para tener los equipos en mano** si se quiere instalar antes de Navidad | V2C |
| 7–11/12 | Ejecución (≈ 3 jornadas) y pruebas | Tú |
| 14–18/12 | CIE de la instalación por TECI y puesta en servicio. Solicitud del aumento de potencia con el CIE de la vivienda si hace falta | Tú, cliente |
| 21–24/12 | e-distribución: para potencia final ≤ 15 kW aplica tratamiento abreviado y los plazos de respuesta se reducen a la mitad (guía de e-distribución); no publica plazo de ejecución para un cambio de potencia | e-distribución |

**Fecha límite legal que no estaba en el calendario: 31/12/2026** (ISO 15118-20). **Puedes prometer** instalación, CIE y puesta en servicio antes del 31/12 **si V2C entrega antes del 4/12**. **No puedes prometer** el aumento a 14,49 kW antes de Navidad. Mientras tanto el balanceo reparte la potencia contratada actual.

## 9. Desglose de las 22 horas
Fijación y conexionado de dos cargadores, 4 h · cuadro (2 C40, 2 diferenciales, protector, IGA, 2 diferenciales), 4 h · tubo y cables de fuerza (19 m), 3 h · UTP, tubo de comunicaciones y balanceo en serie con el ControlBox, 3 h · toma de garaje, 3 h · configuración V2C Cloud, e-Keys, mediciones y pruebas, 3 h · preparación de la memoria y el CIE, 2 h. Estimación mía; tu experiencia manda.

## 10. Datos que faltan y preguntas
**Para el cliente:** boletín actual (potencia máxima y fecha) · potencia contratada en P1 y P2 · foto del cuadro · número de plazas, si son individuales, su posición y la distancia entre ellas · recorrido del cuadro al garaje · ¿hay iluminación suficiente en el garaje? · ubicación del router · nombre del administrador de la comunidad.

**Para ti:** (opcional) mensaje escrito de V2C sobre la retirada de la Alva, por si la clienta lo pide · tarifa de instalador de V2C y de Saltoki, Rexel o Sonepar · tu coste real por hora · precio real de la memoria técnica y de los dos CIE con tu tramitador · precios de Activacar (imágenes del 19/10) · el PDF 00040 del 13/10 · garantía de instalación que quieres dar · respuesta de Industria/OCA sobre qué significa "instalado" en la ISO 15118-20.

**Pregunta a V2C (envíala antes del mensaje):**
> Buenos días. Vamos a instalar dos Trydan Pro monofásicos (TRYPRO32-1-L5-ES) en un garaje comunitario, cada uno con su línea de 32 A, con balanceo en serie y un ControlBox. 1) ¿Cumple el Trydan Pro la EN ISO 15118-20 exigida por el punto 2.1.3 del anexo II del AFIR (Reglamento Delegado 2025/656) a los puntos privados de modo 3 instalados desde el 1/1/2027? 2) ¿Plazo de entrega y garantía del Trydan Pro? 3) ¿Puede dar de alta un mismo llavero e-Key en los dos cargadores? ¿Hay modelos de llavero BLE probados? 4) ¿Qué calibre de magnetotérmico recomendáis para una línea de 32 A, y hace falta el detector de fugas DC en España? 5) ¿Cómo se desactivan Wi-Fi, 4G y Bluetooth que no se usen? 6) ¿Longitud máxima del enlace A/B entre el cargador maestro y el extra? 7) ¿Hace falta un protector de sobretensiones junto a cada cargador?
