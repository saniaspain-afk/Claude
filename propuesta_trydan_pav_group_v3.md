# Propuesta Trydan Pro para Sotogrande, versión 3 (auditoría y mejora de la v2)

Preparada el 11/11/2026. Certeza: **[SEGURO]** = texto oficial leído en esta sesión (BOE, texto del Reglamento Delegado 2025/656 en la versión de la Comisión, manuales y web de V2C, e-distribución, Junta de Andalucía); **[PROBABLE]** = criterio de ingeniería o práctica; **[VERIFICAR]** = no pude comprobarlo, con quién hacerlo.

Resultado v3: base **4.798,20 €**, total **5.805,82 € con IVA**, margen 30.1 % con costes minoristas (sin CIE de la vivienda: 5.454,92 €, 30.1 %). La v2 daba 5.897,06 €.

## 0. Qué cambia respecto a la v2 y por qué
| # | Cambio | Motivo | Efecto |
|---|---|---|---|
| 1 | La comparación de precio ya no es con los dos Trydan (5.500,19 €) sino con la **Alva (4.883,89 €)**, que es la oferta que eligieron | La v2 comparaba con la oferta equivocada | Puente en la sección 5 |
| 2 | **Llaveros: RFID de 13,56 MHz (MIFARE) con prueba previa y tarjeta V2C de respaldo**; el e-Key Bluetooth pasa a opción | Piden RFID para no usar móvil ni radios; el e-Key obliga a Bluetooth activo y a otro modo de uso | Llaveros 3 × 3,00 € en vez de 3 × 12,00 € (−27,00 € base) |
| 3 | **Red:** un solo cable Ethernet hasta el cargador maestro; el extra va por el enlace de dos hilos A/B. UTP 26 m → 19 m | La documentación de V2C no exige red en el cargador extra para el balanceo en serie | −8,40 € base; menos superficie de red |
| 4 | Horas 22 → 21 | Un cable de red menos | −40,00 € base |
| 5 | ISO 15118-20: texto prudente, sin argumento de presión | Sin verificar aplicación en España ni cumplimiento del Trydan Pro | Carta reescrita |
| 6 | La carta **no se apoya en el audio** de Cristóbal | No verificado | Carta reescrita; mensaje a V2C pidiendo texto escrito |
| 7 | Escenarios con tarifa de instalador y estructura de precio | Competir con la web de V2C | Sección 5 |
| 8 | Condiciones revisadas con el TRLGDCU (desistimiento 14 días, nulidad de penalizaciones, garantía legal de 3 años en bienes), ITC-BT-05 (sin inspección de OCA) y e-distribución | Contratos con consumidores | Sección 6 |
| 9 | Opción nueva: **un Trydan Pro hoy y el segundo después** | Acercar el precio a la Alva | Sección 5 |

Total v2 → v3: 5.897,06 € → 5.805,82 € (-91,24 €): llaveros −32,67 €, UTP −10,16 €, horas −48,40 € (todo con IVA).

---

## 1. Revisión técnica y normativa priorizada
| # | Hallazgo | Certeza | Fuente |
|---|---|---|---|
| 1 | **Comparación de precio de la v2 errónea** (ver sección 5) | — | Cálculo |
| 2 | **RFID del Trydan Pro.** La web oficial dice "RFID y NFC: acerca la tarjeta o el móvil al cargador y la carga arranca" e incluye 1 tarjeta RFID (también el manual). **V2C no documenta qué tarjetas o llaveros lee** (ni frecuencia ni chip). V2C Cloud permite dar de alta un RFID acercándolo o escribiendo su "Código / MAC" | Tarjeta incluida y NFC: SEGURO · lectura de llaveros 13,56 MHz: **VERIFICAR** | [Tienda V2C](https://v2charge.com/store/es/producto/trydan-pro/), [manual Trydan Pro](https://v2charge.com/es/soporte/trydan-pro/manual-instalacion/), [V2C Cloud](https://v2charge.com/es/soporte/v2c-cloud/configuracion-v2c-cloud/) |
| 3 | **Llaveros RFID: solución propuesta.** Comprar 3 llaveros MIFARE 13,56 MHz (ISO 14443A, el estándar de las etiquetas NFC) y probar uno en el cargador antes de pedir los demás; si no se lee, tarjetas V2C (4,17 € IVA incl. cada una). El e-Key Bluetooth queda como opción, con la advertencia de que requiere Bluetooth activo | PROBABLE (la web anuncia NFC; falta prueba) | Tienda V2C |
| 4 | **Topología de red.** Balanceo en serie: ControlBox 2.0 al cargador maestro por UTP Cat6 (puerto RJ45) y dos hilos (azul y blanco/azul) a los terminales A y B del extra, con resistencias de polarización activadas en un dispositivo; máximo 10 cargadores. En este modo el balanceo no usa la red IP. Internet es "recomendable" para supervisión; todos en la misma red local solo hace falta si se quiere optimizar el rendimiento por Internet | SEGURO | [V2C, balanceo entre e-Chargers](https://v2charge.com/es/soporte/control-potencia/dinamico/balanceo-echargers/) |
| 5 | **Qué no sé de la red:** si el cargador extra necesita Internet para RFID, e-Keys o V2C Cloud; si el puerto RJ45 del ControlBox y el puerto Ethernet son físicamente distintos en el Trydan Pro; longitud máxima del enlace A/B; qué dominios y puertos usa V2C Cloud (por si el segmento aislado los filtra) | VERIFICAR con V2C | Mensaje a V2C |
| 6 | **Radios.** Ficha técnica: Wi-Fi / Bluetooth / Ethernet / 4G (SIM incluida). **No encontré en la documentación ninguna forma de desactivar Bluetooth, Wi-Fi o 4G.** Wi-Fi: basta no configurarlo y elegir Ethernet; Bluetooth se usa para la configuración inicial y para e-Keys. Función que se perdería sin Bluetooth: configuración local desde el móvil y e-Keys | Documentado: SEGURO · desactivación: **VERIFICAR** | [Ficha técnica Trydan Pro](https://v2charge.com/wp-content/uploads/2025/11/trydanpro-ficha-tecnica.pdf), manual |
| 7 | **ISO 15118-20 (texto de la Comisión de 2/4/2025, doc. del Consejo ST 7773/25).** Anexo II del AFIR, punto 2.1.3: los puntos de recarga **privados** de CA y CC "instalados o renovados a partir del 1 de enero de 2027" cumplirán al menos EN ISO 15118-20:2022 para el modo 3 o 4. Considerando 22: período transitorio hasta el 1/1/2027 para los privados de modo 3 y 4. El artículo 2 dice que el Reglamento es "directamente aplicable en cada Estado miembro". **Entrada en vigor: 20 días tras su publicación en el DOUE; aplicable seis meses después.** Una búsqueda secundaria sitúa la publicación el 18/6/2025 | Texto de la Comisión: SEGURO · **texto final del DOUE: VERIFICAR** (EUR-Lex bloquea el acceso automático) | [Anexo](https://data.consilium.europa.eu/doc/document/ST-7773-2025-ADD-1/es/pdf), [texto completo](https://data.consilium.europa.eu/doc/document/ST-7773-2025-INIT/es/pdf) |
| 8 | **ISO: lo que no está definido.** El texto no define "instalado o renovado" (compra, entrega, obra terminada, puesta en servicio, fecha del CIE). La ITC-BT-52 consolidada que leí no menciona la ISO 15118. No encontré el régimen sancionador español para puntos privados. La ficha técnica del Trydan Pro no cita la ISO 15118 | VERIFICAR con V2C, Delegación de Industria de Cádiz y MITECO | Mensaje a V2C |
| 9 | **Redacción prudente de la ISO:** citar el texto, decir que se está confirmando con el fabricante y la administración y que el objetivo es entregar la instalación en servicio en 2026. Evitar "es ilegal" y "te corre prisa" | — | Carta |
| 10 | **Alva y el audio.** La web de V2C muestra la Alva en venta con "plazo de preparación y envío superior al habitual" [SEGURO]. La retirada solo consta en el audio de Cristóbal [no verificado] | — | Mensaje a V2C |
| 11 | **Toma de garaje C10: correcto.** Tabla 3 de la ITC-BT-52: bases UNE 20315-1-2 (fig. C2a) y UNE 20315-2-11 (fig. C7a) con automático de 10 A, permitidas en "viviendas unifamiliares" y "aparcamientos en edificios de viviendas"; 16 A solo si el fabricante de la base garantiza que queda protegida en recarga lenta de 8 h diarias. Punto de conexión junto a la plaza, en envolvente fija, a 60 cm mínimo del suelo; diferencial de 30 mA clase A por punto de conexión; circuito dedicado | SEGURO | [BOE, ITC-BT-52](https://www.boe.es/buscar/act.php?id=BOE-A-2014-13681), apartados 5, 5.4, 6.1, 6.3 |
| 12 | **Caída de tensión** (límite 5 %, ITC-BT-52 apartado 5), 3G10, 32 A, ρ = 0,0225 Ω·mm²/m: 7 m → 1,0 V (0,44 %); 12 m (maestro+extra) → 1,7 V (0,75 %); 15 m → 0,9 %. Toma de garaje 3G2,5 con 10 A y 15 m: 2,7 V (1,2 %) | Límite: SEGURO · cálculo: mío | BOE |
| 13 | **Sección y agrupamiento.** Tabla 1 del REBT (ITC-BT-19, cobre, tubo, 2 conductores XLPE, 40 °C): 6 mm² = 44 A, 10 mm² = 60 A, 16 mm² = 80 A. Con dos circuitos agrupados hace falta un factor de reducción: 3G10 cubre un C40 mientras el factor sea ≥ 0,67 (60 A × 0,67 = 40 A); el valor habitual de 0,8 da 48 A. 3G6 con C40 solo vale sin agrupar. Los dos cables comparten tubo únicamente los 7 m hasta el maestro | Tabla: SEGURO · factor: **VERIFICAR** (UNE 20460-5-523, de pago) | BOE, REBT |
| 14 | **Calibre del automático:** el manual del Trydan Pro no fija el calibre ("según la placa y la línea"); la ITC-BT-52 (6.3) permite que supere la intensidad del cargador por tolerancias. C40 con 3G10 es la opción robusta; C32 con 3G6 también cumpliría sobre el papel, con riesgo de disparos intempestivos | SEGURO (textos) · calibre ideal: VERIFICAR con V2C | Manual, BOE |
| 15 | **Corriente continua residual:** la ficha del Trydan Pro dice "DC 6 mA, opcional" (detector V2C-F). El BOE solo exige diferencial clase A | SEGURO | Ficha técnica, BOE |
| 16 | **TECI:** la Junta de Andalucía lista como instalaciones que se tramitan por TECI "recarga de vehículo eléctrico que no sea de modo 4, no situadas en el exterior y de potencia ≤ 50 kW" y "viviendas consideradas de forma individual con previsión de cargas ≤ 50 kW". Dos Trydan Pro de 7,4 kW → TECI. La ITC-BT-04 exime de proyecto a las recargas en garajes ya existentes de edificios de viviendas; basta memoria técnica de diseño (MTD) y CIE | SEGURO | [Junta, TECI](https://www.juntadeandalucia.es/organismos/industriaenergiayminas/areas/industria/instalaciones/paginas/TECI.html), BOE |
| 17 | **Sin inspección de OCA:** la ITC-BT-05, 4.1.h) exige inspección inicial solo a las estaciones de recarga que requieren proyecto. Esta no | SEGURO | BOE (texto modificado por el RD 1053/2014) |
| 18 | **CIE de la vivienda: NO es obligatorio siempre.** Hace falta si 14,49 kW supera la potencia máxima de su boletín, si pasaron más de 20 años desde la última verificación, o si hubo cambio de tensión. Antes de pedir el aumento, e-distribución verifica que el suministro lo soporta. Solo se cambia la potencia una vez al año | SEGURO | [e-distribución](https://www.edistribucion.com/es/servicios/conexion-red/cambio-potencia.html) |
| 19 | **Trámite de potencia ≤ 15 kW:** el titular lo pide a su comercializadora; e-distribución hace los trabajos; la comercializadora informa y cobra el coste. Tratamiento abreviado: los plazos de respuesta del RD 1183/2020 se reducen a la mitad (los plazos generales de la guía: < 3 semanas hasta 100 kW). La guía menciona derechos de extensión de 17,37 €/kW para acometidas a baremo en nuevos suministros; **no he podido confirmar si se aplican a un simple aumento de potencia** | Trámite: SEGURO · derechos aplicables: **VERIFICAR con tu comercializadora o e-distribución** | [Guía e-distribución](https://www.edistribucion.com/content/dam/edistribucion/conexion-a-la-red/descargables/guia-gestion-suministros-es7.pdf) |
| 20 | **Potencia solo en P2:** el peaje 2.0TD tiene tope de 15 kW y la exigencia de potencias crecientes está escrita para 3.0TD y superiores, no para 2.0TD | SEGURO | [Circular 3/2020](https://www.boe.es/buscar/act.php?id=BOE-A-2020-1066) |
| 21 | **Garantía legal:** en bienes, el vendedor responde de las faltas de conformidad que se manifiesten en 3 años desde la entrega (TRLGDCU, art. 120). PAV GROUP como vendedor de los cargadores responde ante la clienta aunque V2C dé menos años | SEGURO | [TRLGDCU](https://www.boe.es/buscar/act.php?id=BOE-A-2007-20555) |
| 22 | **Desistimiento:** contratos a distancia o fuera del establecimiento (WhatsApp, visita): 14 días naturales sin motivo (arts. 92, 102 y 104); **son nulas las cláusulas que penalicen el desistimiento o renuncien a él** (art. 102.2). Excepciones en el art. 103 (por ejemplo, servicio completamente ejecutado con consentimiento expreso previo). Art. 79: no se puede exigir anticipo de pago o garantías para el caso de que se ejercite un desistimiento contractual | SEGURO (texto) · aplicación a tu contrato: **VERIFICAR con tu asesor** | TRLGDCU |
| 23 | **Comunidad:** punto de recarga privado en plaza individual solo requiere comunicación previa a la comunidad; coste y consumo a cargo del interesado | SEGURO | [LPH art. 17.5](https://www.boe.es/buscar/act.php?id=BOE-A-1960-10906) |
| 24 | **LGA y derivación individual:** el diseñador debe comprobar que no se supera su intensidad admisible (ITC-BT-52, apartado 5). Coste no incluido si hay que cambiarlas | SEGURO | BOE |
| 25 | **Errores detectados en la v2:** (a) comparación con la oferta equivocada; (b) afirmaba "garantía del fabricante" para los equipos sin citar la garantía legal de 3 años; (c) la condición de desistimiento no citaba el derecho legal de 14 días; (d) proponía e-Key BLE como solución al RFID | — | — |

---

## 2. Esquema final recomendado
```
 CUADRO DE LA VIVIENDA (7 m)                                   GARAJE COMUNITARIO
 ┌──────────────────────────────────────────────┐
 │ IGA 63 A · protector sobretensiones          │   tubo FUERZA (RZ1-K AS 3G10, 2 cables, 7 m)
 │ C40 + dif. 40A/30mA tipo A  (línea 1) ───────┼──────────────────────────────►  TRYDAN PRO 1  (maestro)
 │ C40 + dif. 40A/30mA tipo A  (línea 2) ───────┼──────────────┐ (+5 m, 1 cable)      │  ▲  ▲
 │ C10 + dif. 30mA tipo A (toma garaje) ────────┼─► tubo 3G2,5 (15 m) ► base con llave │  │  │
 │ V2C ControlBox + pinza (en la acometida)     │                                      │  │  │
 └───────┬──────────────────────────────────────┘                                      │  │  │
         │  tubo COMUNICACIONES, separado de la fuerza (12 m)                          │  │  │
         ├─ UTP Cat6 ControlBox ► RJ45 del maestro ────────────────────────────────────┘  │  │
         ├─ UTP Cat6 router ► Ethernet del maestro ───────────────────────────────────────┘  │
         └─ UTP 2 hilos (A/B) maestro ► extra ────────────────────────────────────────────►  TRYDAN PRO 2 (extra)
 Router/MikroTik (vivienda): segmento aislado, solo salida a Internet.  Sin rosetas, switches ni cajas en el garaje.
```
- **Cables de comunicación:** ControlBox–maestro 7 m, router–maestro 7 m y enlace A/B de 5 m: **19 m** de UTP, todo en **12 m** de tubo aparte. Cada cable termina dentro de un cargador.
- **Opción si V2C exige red en el extra:** un segundo cable router–extra (+12 m de UTP, unos 14 € con IVA) [VERIFICAR].
- **Alternativas descartadas:** Alva con dos líneas (retirada o sin suministro confirmado, y ya no hay doble alimentación en un equipo); línea única de 63 A (calibre del seccionador de la Alva con protecciones no publicado); un solo Trydan Pro con un enchufe (no cubre dos coches).
- **Por qué dos cargadores independientes:** cada punto de conexión queda junto a su plaza (ITC-BT-52, 5.4), cada circuito de 7,4 kW queda dentro del límite de 9,2 kW de la tabla 1 de 3.1, y una avería no deja sin carga al otro coche.

---

## 3. Presupuesto del CLIENTE v3 (español)
Cantidades supuestas: cuadro a 7 m del maestro (dato tuyo), 5 m entre cargadores (estimación), 19 m de fuerza, 12 m de tubo, 19 m de UTP, toma de garaje 15 m (sin dato), 2 diferenciales, 21 h. Todo "a confirmar en visita".

| # | Descripción | Cant. | Ud | Precio unit. | Importe |
|---|---|---:|---|---:|---:|
| | **Equipos** | | | | |
| 1 | Dos cargadores V2C Trydan Pro monofásicos, 7,4 kW (32 A) cada uno, cable liso Tipo 2 de 5 m, sin protecciones integradas y sin contador MID, lector RFID/NFC, Ethernet/Wi-Fi/4G, con V2C ControlBox y pinza amperimétrica incluidos (un cargador hace de maestro del balanceo de potencia) | 2 | ud | 1.099,00 € | 2.198,00 € |
| 2 | Llaveros RFID de 13,56 MHz (MIFARE, ISO 14443A) para arrancar y bloquear la carga acercándolos al cargador (3 uds). Se prueban con los cargadores antes de la entrega; si alguno no se lee, se sustituye por una tarjeta RFID original V2C | 3 | ud | 3,00 € | 9,00 € |
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
| 11 | Cable UTP Cat6: ControlBox-cargador maestro, router-cargador maestro y enlace de dos hilos maestro-extra para el balanceo. Terminan dentro de los cargadores, sin rosetas, switches ni cajas en el garaje (m totales) | 19 | m | 1,20 € | 22,80 € |
| 12 | Canalización independiente de la fuerza para los cables de comunicaciones (m, a confirmar en visita) | 12 | m | 3,80 € | 45,60 € |
| | **Toma de garaje** | | | | |
| 13 | Línea independiente para la toma de garaje: cable 3G2,5 mm² RZ1-K (AS) y canalización (m, a confirmar en visita) | 15 | m | 5,10 € | 76,50 € |
| 14 | Toma de garaje para bicicletas y patinetes: magnetotérmico C10, diferencial 30 mA tipo A y base de enchufe en envolvente cerrada con llave (ITC-BT-52, tabla 3) | 1 | ud | 105,00 € | 105,00 € |
| | **Mano de obra** | | | | |
| 15 | Mano de obra: instalación de los dos cargadores, conexionado, mediciones, configuración del balanceo, e-Keys y V2C Cloud, y puesta en marcha (horas, a confirmar en visita) | 21 | h | 40,00 € | 840,00 € |
| | **Legalización y gestiones** | | | | |
| 16 | Memoria técnica de diseño y CIE de la instalación de recarga, dos cargadores (ITC-BT-52, ITC-BT-04), registro en Industria (TECI, Junta de Andalucía) | 1 | ud | 300,00 € | 300,00 € |
| 17 | CIE de la vivienda para 14,49 kW y gestión del aumento de potencia en periodo P2 con la comercializadora y e-distribución. Incluido en el precio total; si su boletín actual ya admite 14,49 kW, se descuenta íntegramente | 1 | ud | 290,00 € | 290,00 € |

Subtotales: Equipos 2.207,00 € · Líneas y canalización 237,30 € · Protecciones y cuadro 674,00 € · Red y comunicaciones 68,40 € · Toma de garaje 181,50 € · Mano de obra 840,00 € · Legalización y gestiones 590,00 €

Base imponible **4.798,20 €** · IVA 21 % 1.007,62 € · **TOTAL 5.805,82 €**

**Opcionales (no incluidos en el total):** detector de fugas DC V2C, 2 uds a 122 € + IVA, solo si V2C lo exige · segundo cable de red router–extra, 15 m de UTP y tubo: unos 14 € con IVA · llaveros e-Key Bluetooth en lugar de RFID, 3 × 12 € + IVA.

### Versión en ruso (descripciones)
| # | Описание | Кол-во | Ед. | Цена за ед. | Сумма |
|---|---|---:|---|---:|---:|
| | **Equipos** | | | | |
| 1 | Две зарядные станции V2C Trydan Pro, однофазные, по 7,4 кВт (32 А), кабель Type 2 длиной 5 м, без встроенных защит и без счётчика MID, считыватель RFID/NFC, Ethernet/Wi-Fi/4G, V2C ControlBox и токовые клещи в комплекте (одна станция — ведущая в балансировке мощности) | 2 | ud | 1.099,00 € | 2.198,00 € |
| 2 | RFID-брелки 13,56 МГц (MIFARE, ISO 14443A) для запуска и блокировки зарядки при поднесении к станции (3 шт.). Проверяются на станциях до сдачи; если какой-либо не читается, заменяется оригинальной RFID-картой V2C | 3 | ud | 3,00 € | 9,00 € |
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
| 11 | Кабель UTP Cat6: ControlBox—ведущая станция, роутер—ведущая станция и двухпроводная связь ведущая—ведомая для балансировки. Заканчиваются внутри станций, без розеток, коммутаторов и коробок в гараже (всего м) | 19 | m | 1,20 € | 22,80 € |
| 12 | Отдельная от силовых линий труба для кабелей связи (м, уточняется на визите) | 12 | m | 3,80 € | 45,60 € |
| | **Toma de garaje** | | | | |
| 13 | Отдельная линия для розетки в гараже: кабель 3G2,5 мм² RZ1-K (AS) и труба (м, уточняется на визите) | 15 | m | 5,10 € | 76,50 € |
| 14 | Розетка в гараже для велосипедов и самокатов: автомат C10, дифференциал 30 мА тип A и розетка в закрытом корпусе с ключом (ITC-BT-52, таблица 3) | 1 | ud | 105,00 € | 105,00 € |
| | **Mano de obra** | | | | |
| 15 | Работа: монтаж двух станций, подключение, измерения, настройка балансировки, e-Key и V2C Cloud, пусконаладка (часы, уточняется на визите) | 21 | h | 40,00 € | 840,00 € |
| | **Legalización y gestiones** | | | | |
| 16 | Техническая записка (MTD) и CIE установки зарядки, две станции (ITC-BT-52, ITC-BT-04), регистрация в Industria (TECI, Junta de Andalucía) | 1 | ud | 300,00 € | 300,00 € |
| 17 | CIE квартиры на 14,49 кВт и оформление увеличения мощности в периоде P2 через comercializadora и e-distribución. Включено в общую цену; если ваш текущий boletín уже допускает 14,49 кВт, сумма вычитается полностью | 1 | ud | 290,00 € | 290,00 € |

Subtotales: Equipos 2.207,00 € · Líneas y canalización 237,30 € · Protecciones y cuadro 674,00 € · Red y comunicaciones 68,40 € · Toma de garaje 181,50 € · Mano de obra 840,00 € · Legalización y gestiones 590,00 €

База **4.798,20 €** · IVA 21 % 1.007,62 € · **ИТОГО 5.805,82 €**

---

## 4. Tabla INTERNA v3
Costes minoristas. El coste/hora de 26,67 € es un supuesto (venta ÷ 1,5); sustitúyelo por tu coste real.

| # | Concepto (abrev.) | Cant. | Coste unit. | Venta unit. | Venta | Coste | Margen € | Margen % | Origen | Pedir precio real a |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Dos cargadores V2C Trydan Pro monofásicos, 7,4 kW (32 A… | 2 | 832,50 | 1.099,00 | 2.198,00 | 1.665,00 | 533,00 | 24.2 % | Oficial V2C (PVP web) | V2C / distribuidor V2C: tarifa de instalador |
| 2 | Llaveros RFID de 13,56 MHz (MIFARE, ISO 14443A) para ar… | 3 | 2,00 | 3,00 | 9,00 | 6,00 | 3,00 | 33.3 % | ESTIMACIÓN | Proveedor de llaveros 13,56 MHz; comprar 1 para probar; preguntar a V2C |
| 3 | Dos líneas de alimentación independientes, cable RZ1-K … | 19 | 5,78 | 8,70 | 165,30 | 109,82 | 55,48 | 33.6 % | Obramat/Leroy (PVP) | Saltoki/Rexel/Sonepar: tarifa |
| 4 | Tubo y fijaciones para las líneas de fuerza (m, a confi… | 12 | 4,00 | 6,00 | 72,00 | 48,00 | 24,00 | 33.3 % | ESTIMACIÓN | Saltoki/Rexel/Sonepar |
| 5 | Magnetotérmico 2P C40 curva C, uno por línea (ITC-BT-52… | 2 | 25,00 | 38,00 | 76,00 | 50,00 | 26,00 | 34.2 % | ESTIMACIÓN | Saltoki/Rexel/Sonepar |
| 6 | Diferencial 2P 40 A, 30 mA, tipo A superinmunizado, uno… | 2 | 39,26 | 59,00 | 118,00 | 78,52 | 39,48 | 33.5 % | Obramat/Leroy (PVP) | Saltoki/Rexel/Sonepar |
| 7 | Protector contra sobretensiones permanentes y transitor… | 1 | 74,02 | 112,00 | 112,00 | 74,02 | 37,98 | 33.9 % | Obramat/Leroy (PVP) | Saltoki/Rexel/Sonepar |
| 8 | Sustitución del IGA por magnetotérmico 2P 63 A (para 14… | 1 | 46,45 | 70,00 | 70,00 | 46,45 | 23,55 | 33.6 % | Obramat/Leroy (PVP) | Saltoki/Rexel/Sonepar |
| 9 | Sustitución de diferenciales del cuadro de la vivienda … | 2 | 39,26 | 59,00 | 118,00 | 78,52 | 39,48 | 33.5 % | Obramat/Leroy (PVP) | Saltoki/Rexel/Sonepar |
| 10 | Material auxiliar y señalización (bornas, punteras, caj… | 1 | 120,00 | 180,00 | 180,00 | 120,00 | 60,00 | 33.3 % | ESTIMACIÓN | Tu histórico de obras |
| 11 | Cable UTP Cat6: ControlBox-cargador maestro, router-car… | 19 | 0,76 | 1,20 | 22,80 | 14,44 | 8,36 | 36.7 % | Obramat/Leroy (PVP) | Saltoki/Rexel/Sonepar |
| 12 | Canalización independiente de la fuerza para los cables… | 12 | 2,50 | 3,80 | 45,60 | 30,00 | 15,60 | 34.2 % | ESTIMACIÓN | Saltoki/Rexel/Sonepar |
| 13 | Línea independiente para la toma de garaje: cable 3G2,5… | 15 | 3,40 | 5,10 | 76,50 | 51,00 | 25,50 | 33.3 % | Obramat/Leroy (PVP) | Saltoki/Rexel/Sonepar |
| 14 | Toma de garaje para bicicletas y patinetes: magnetotérm… | 1 | 70,00 | 105,00 | 105,00 | 70,00 | 35,00 | 33.3 % | ESTIMACIÓN | Saltoki/Rexel/Sonepar |
| 15 | Mano de obra: instalación de los dos cargadores, conexi… | 21 | 26,67 | 40,00 | 840,00 | 560,00 | 280,00 | 33.3 % | Tarifa 40 €/h | Tu coste real por hora (salario + SS + furgoneta) |
| 16 | Memoria técnica de diseño y CIE de la instalación de re… | 1 | 150,00 | 300,00 | 300,00 | 150,00 | 150,00 | 50.0 % | ESTIMACIÓN | Tu tramitador/ingeniería colaboradora |
| 17 | CIE de la vivienda para 14,49 kW y gestión del aumento … | 1 | 200,00 | 290,00 | 290,00 | 200,00 | 90,00 | 31.0 % | ESTIMACIÓN | Tu tramitador/ingeniería colaboradora |

Venta base **4.798,20 €** · coste **3.351,77 €** · margen **1.446,43 €** (**30.1 %**). Sin CIE de la vivienda: base 4.508,20 €, margen 30.1 %.

**Escenarios con tarifa de instalador (los descuentos son supuestos míos, no datos):**
| Dto. V2C sobre PVP | Dto. materiales | Margen con el precio actual | Rebaja posible manteniendo 30 % (con IVA) | Margen con los cargadores a PVP web | Total con los cargadores a PVP web |
|---|---|---:|---:|---:|---:|
| 0 % | 0 % | 30.1 % | 12,05 € | 21.4 % | 5.160,89 € |
| 10 % | 20 % | 35.5 % | 456,38 € | 27.4 % | 5.160,89 € |
| 15 % | 25 % | 37.7 % | 639,42 € | 29.9 % | 5.160,89 € |
| 20 % | 30 % | 39.9 % | 822,45 € | 32.4 % | 5.160,89 € |
| 25 % | 35 % | 42.1 % | 1.005,49 € | 34.9 % | 5.160,89 € |

**Lectura:** con costes minoristas el margen ya está en el suelo del 30 %, sin hueco para bajar precio. Con un descuento de V2C de al menos ≈ 16 % y de materiales de ≈ 26 % (supuestos), puedes mostrar los **cargadores al precio de la web** y seguir en ≥ 30 %. Con 20 %/30 % puedes bajar el precio actual unos 822,45 € con IVA.

---

## 5. Opciones de precio y explicación frente a la Alva
### Puente frente a la oferta de la Alva (4.883,89 € del 13/10)
| Concepto | IVA incl. |
|---|---:|
| Alva, presupuesto 00039 | 4.883,89 € |
| Lo que ya incluía, ahora (con dos Trydan Pro en vez de la Alva) | 4.914,17 € (+30,28 €) |
| Nuevo por sus peticiones: llaveros RFID (10,89 €), toma de garaje (219,62 €), IGA y diferenciales (227,48 €), red y tubo aparte (82,76 €), CIE de la vivienda (350,90 €) | 891,65 € |
| **Total v3** | **5.805,82 €** (+921,93 €) |
| Wi-Fi que ya no hace falta (200 € + IVA) | −242,00 € |

**Lectura:** el 97 % de la subida son cosas que ellos pidieron después del 13/10; el cambio de equipo pesa 30,28 €. Frente a lo que habrían pagado con la Alva más el Wi-Fi (5.125,89 €) la diferencia es de 679,93 €. **Supuesto a confirmar con el PDF 00039:** que esas partidas no estaban en el presupuesto de la Alva.

### Cómo evitar que parezca arbitrario
1. **Causas externas verificables:** la Alva no tiene suministro confirmado ni plazo (la web de V2C avisa de un "plazo de preparación y envío superior al habitual").
2. **Lo nuevo es suyo:** cada partida nueva responde a una petición de su chat (RFID sin móvil, red aislada en tubo aparte, toma de garaje, aumento de potencia con IGA y diferenciales, ambos CIE).
3. **Mejoras reales:** dos cargadores independientes (una avería no afecta al otro), cada uno junto a su plaza, dos circuitos de 7,4 kW dentro del límite de 9,2 kW.
4. **Desglose transparente:** la tabla de arriba y el descuento íntegro del CIE de la vivienda si no hace falta.

### Opciones
| Opción | Base | IVA 21 % | Total | Margen |
|---|---:|---:|---:|---:|
| **1. Llave en mano: dos Trydan Pro (recomendada)** | 4.798,20 € | 1.007,62 € | **5.805,82 €** | 30.1 % |
| 1b. Igual si el boletín ya admite 14,49 kW (sin CIE vivienda) | 4.508,20 € | 946,72 € | 5.454,92 € | 30.1 % |
| 2. Por fases: Fase 1 (cargadores, líneas, protecciones, red, toma, mano de obra, CIE instalación) | 4.320,20 € | 907,24 € | 5.227,44 € | — |
| 2. Por fases: Fase 2 (IGA, diferenciales, CIE vivienda y gestión de potencia) | 478,00 € | 100,38 € | 578,38 € | — |
| 3. Por horas (17 h / 25 h a 40 €/h) | — | — | 5.612,22 € / 5.999,42 € | ≥ 30 % |
| 4. El cliente compra los dos Trydan Pro en la web V2C (2.014,66 € IVA incl.); nosotros instalamos y legalizamos | 2.600,20 € | 546,04 € | 3.146,24 € | 35.1 % |
| 5. **Reducida:** un Trydan Pro hoy; la línea y el cargador del segundo, después | 3.282,80 € | 689,39 € | 3.972,19 € | 31.7 % |

**Recomendación:** presentar la **1 por fases (2)**, con la **5** como alternativa para quien quiera acercarse al precio de la Alva (3.972,19 € frente a 4.883,89 €) y la **4** como último recurso ante la objeción del precio de los cargadores. Si consigues la tarifa de instalador, pasa a mostrar los cargadores al precio de la web (sección 4).
La opción 5 no tiene en cuenta que los dos coches necesitan carga a la vez: el segundo cargador, su línea y su protección se presupuestan después y no están incluidos.

---

## 6. Condiciones y exclusiones (revisadas)
- **Validez:** 15 días (antes 30), para limitar el riesgo de cambio de tarifa de V2C. Una vez aceptado, el precio no varía.
- **Pagos (tu decisión):** 40 % a cuenta al aceptar, 40 % al terminar la instalación, 20 % al entregar los CIE registrados. Redacta los pagos como **pagos a cuenta, devolvibles** si la clienta ejerce el desistimiento legal o si no se cumple la fecha tope. No uses "no reembolsable" ni cláusulas de penalización: son nulas (TRLGDCU, art. 102.2).
- **Desistimiento:** informar por escrito del derecho legal de 14 días naturales y entregar un formulario; si empiezas la obra dentro de ese plazo, pide su solicitud expresa por escrito y consulta con tu asesor cómo se liquida lo ya ejecutado (arts. 103 a y 107-108, **no leídos**). La omisión de esta información alarga el plazo (art. 105, titular visto, texto no leído). [VERIFICAR con asesor]
- **Fecha tope de entrega (derecho añadido a favor de la clienta):** si los equipos no están en obra el 15/12/2026, la clienta puede desistir con devolución íntegra de lo pagado. No lo vincules a la ISO.
- **Garantía:** equipos, 3 años legales desde la entrega (TRLGDCU, art. 120), con repetición contra V2C [VERIFICAR garantía comercial de V2C para el Trydan Pro]. Instalación: 2 años, compromiso comercial tuyo; no verifiqué un plazo legal para servicios.
- **Ejecución:** unas 3 jornadas (21 h) desde que llegan los equipos; los plazos de e-distribución y de la Junta no los controlas.
- **No incluido:** obra civil y acabados · derivación individual, LGA o centralización del edificio si no admiten 14,49 kW · iluminación del garaje si no llega a 50 lux a nivel de suelo (ITC-BT-52, apartado 5) · comunicación a la comunidad (LPH, art. 17.5) · tasas administrativas, derechos de acceso o extensión y costes de e-distribución (los factura la comercializadora; ver hallazgo 19) · configuración del router y de la red del cliente · detector de fugas DC si V2C lo exige · ayudas.
- **Cambios tras la visita:** metros, diferenciales y horas se liquidan a precio unitario; la hora sigue a 40 € + IVA.
- **Partida 17 (CIE de la vivienda):** redactada como incluida en el precio total, con descuento íntegro de 350,90 € si el boletín actual ya admite 14,49 kW; en el desglose figura como "se descuenta si no hace falta", nunca como cargo adicional.
- **Corregido respecto a la v2:** garantía de equipos 3 años por ley, desistimiento legal, validez 15 días, pagos como pagos a cuenta.

---

## 7. Mensaje en ruso y objeciones
Ver `mensaje_clienta_trydan_ru_v3.md`.

## 8. Calendario realista desde hoy (miércoles 11/11/2026)
| Semana | Qué pasa | Lo controlas tú | Depende de terceros |
|---|---|:--:|:--:|
| 11–13/11 | Enviar el mensaje a V2C (sección 9) y la carta a la clienta. Pedir tarifa de instalador | ✔ | |
| 16–20/11 | **Visita técnica martes 17 o jueves 19.** Foto del cuadro, boletín, plazas. Comprar 1 llavero MIFARE de prueba y una tarjeta V2C. Borrador de MTD | ✔ | Clienta (datos) |
| 23–27/11 | Pedido de los dos Trydan Pro al aceptar. Clienta comunica a la comunidad y consulta a e-distribución | ✔ | V2C (plazo), clienta, e-distribución |
| 30/11–4/12 | **Fecha límite para tener los equipos en mano** | | V2C |
| 7–11/12 | Ejecución (≈ 3 jornadas) y pruebas, incluida la prueba de los llaveros | ✔ | |
| 14–18/12 | CIE de la instalación por TECI y puesta en servicio. Solicitud del aumento de potencia con el CIE de la vivienda si hace falta | ✔ (CIE) | Clienta (solicitud), comercializadora |
| 21–24/12 | e-distribución ejecuta el cambio de potencia; plazos de respuesta reducidos a la mitad para ≤ 15 kW. No publica plazo de ejecución | | e-distribución |

**Puedes prometer:** visita técnica, MTD, instalación y CIE de la instalación dentro de diciembre **si los equipos llegan antes del 4/12**; devolución íntegra si no están en obra el 15/12. **No puedes prometer:** la fecha de llegada de V2C, la del aumento a 14,49 kW, ni nada sobre cómo se aplica la ISO a la fecha de instalación.

## 9. Mensaje a V2C (español, listo para enviar)
> Asunto: Disponibilidad y aspectos técnicos del Trydan Pro monofásico y estado de la Alva
>
> Buenos días. Vamos a instalar en un garaje comunitario (Sotogrande, Cádiz) dos Trydan Pro monofásicos (TRYPRO32-1-L5-ES) con balanceo en serie. Os agradecemos respuesta por escrito a lo siguiente:
> 1. **Alva:** ¿Está retirada, descatalogada o en revisión? ¿Desde cuándo y por qué motivo? ¿Hay stock y plazo para pedidos ahora?
> 2. **Trydan Pro:** ¿Stock y plazo de entrega de 2 unidades? ¿Garantía comercial? ¿Tarifa de instalador?
> 3. **ISO 15118-20:** el anexo II del AFIR (Reglamento Delegado (UE) 2025/656, punto 2.1.3) exige EN ISO 15118-20:2022 a los puntos privados de modo 3 instalados o renovados desde el 1/1/2027. ¿Cumple el Trydan Pro? ¿Con qué firmware o fecha? ¿Qué considera V2C "instalado" a estos efectos?
> 4. **RFID:** ¿qué frecuencia y tipo de chip lee el lector? ¿Acepta llaveros MIFARE Classic de 13,56 MHz? ¿Funciona sin Internet? ¿Se puede dar de alta una tarjeta por su UID?
> 5. **e-Key:** ¿un mismo llavero BLE puede darse de alta en dos cargadores?
> 6. **Balanceo en serie:** ¿el puerto RJ45 del ControlBox es distinto del puerto Ethernet? ¿El cargador extra necesita conexión a Internet para RFID, e-Keys y V2C Cloud? ¿Longitud máxima del enlace A/B y tipo de cable? ¿Dónde se activan las resistencias de polarización?
> 7. **Radios:** ¿cómo se desactivan Wi-Fi, Bluetooth y 4G si solo se usa Ethernet? ¿Qué se pierde? ¿Qué dominios y puertos salientes usa V2C Cloud?
> 8. **Protecciones:** ¿calibre de magnetotérmico recomendado para una línea de 32 A (C32 o C40)? ¿Es necesario el detector de fugas DC en España? ¿Hace falta un protector de sobretensiones junto al cargador?
> Gracias. Dmitri, PAV GROUP.

## 10. Pendientes y verificaciones
**Verificar (con quién):** respuesta de V2C a las 8 preguntas · texto final del DOUE del 2025/656 (EUR-Lex en navegador; yo no pude abrirlo) · significado de "instalado" y régimen sancionador (Delegación de Industria de Cádiz, MITECO) · factor de agrupamiento (UNE 20460-5-523, AENOR) · derechos de extensión en un aumento de potencia (tu comercializadora o e-distribución) · aplicación del desistimiento a tu contrato y tasas del TECI (tu asesor y la Junta).
**Datos de la clienta:** boletín (potencia máxima y fecha) · P1 y P2 actuales · foto del cuadro · derivación individual y LGA · número y posición de las plazas, y distancia entre ellas · recorrido cuadro-garaje · iluminación del garaje · ubicación del router · administrador de la comunidad.
**Datos tuyos:** PDF 00039 y 00040 · imágenes de Activacar del 19/10 · manual de la Alva · tu coste real por hora · tarifas de V2C, Saltoki, Rexel o Sonepar · precio real de la memoria técnica y de los dos CIE con tu tramitador.
