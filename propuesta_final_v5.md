# Propuesta final para Sotogrande: revisión completa tras la confirmación de V2C (12/11/2026)

Certeza: **[SEGURO]** = leído en fuente oficial o en el chat; **[PROBABLE]** = criterio de ingeniería; **[VERIFICAR]** = pendiente, con quién.

## 0. Lo que cambia hoy
En el chat del 12/11 Cristóbal (representante de V2C) contesta a tu pregunta:
- "¿El Trydan Pro cumple la ISO?" → **"No"**.
- "Hasta feb/mar nada de ISO por parte de V2C" (reenviado).
- "¿La única opción viable es poner el cargador antes de 2027?" → **"Sí"**.

**Decisión:** dos V2C Trydan Pro, pedidos ya, instalados, certificados y en servicio **antes del 31/12/2026**. Es la única opción con V2C y es la que dijiste que propondrías.

Precio, con una corrección frente a la v4: añadí el cable Ethernet del router al cargador extra (+12 m de UTP) y una hora de obra, porque el extra necesita red para RFID, e-Keys y V2C Cloud mientras V2C no diga lo contrario.
| | v4 | **Final** |
|---|---:|---:|
| **B, llave en mano** (con IVA) | 5.805,82 € | **5.871,65 €** |
| **A, ella compra los cargadores** (con IVA) | 3.146,24 € | **3.212,07 €** |
| A más los dos Trydan Pro de la web (2.014,66 €) | 5.160,90 € | **5.226,73 €** |
Margen con costes minoristas: B 30.2 %, A 35.1 %. Se quitó la variante de la Alva.

---

## 1. Revisión desde el principio: lo que pidió la clienta y cómo queda cubierto
| # | Lo que pide o aceptó | Cómo se cubre | Línea B/A | Estado |
|---|---|---|---|---|
| 1 | Dos tomas monofásicas de 7,4 kW (32 A), sin MID, con **dos cables Type 2 de 5 m** (no tomas) | Dos Trydan Pro, TRYPRO32-1-L5-ES: cable liso de 5 m, sin MID | 1 / — | SEGURO (tienda V2C) |
| 2 | RFID con llavero, **sin móvil**; pidió 3 llaveros | 3 llaveros RFID 13,56 MHz (MIFARE) con prueba previa; cada Trydan Pro trae 1 tarjeta V2C de respaldo. e-Key Bluetooth solo como opción | 2 / 2 | Tarjeta: SEGURO · lectura de llaveros: **VERIFICAR** (V2C no la documenta; web: "RFID y NFC") |
| 3 | Internet por **Ethernet**, sin Wi-Fi | Cada Trydan Pro tiene RJ45 Ethernet (y otro RJ45 para el balanceador) | 11 / 10 | SEGURO |
| 4 | **Red aislada:** el cable termina dentro del cargador, sin rosetas, switches ni cajas; tubo separado de la fuerza | 31 m de UTP en 12 m de tubo aparte; cada cable termina en un cargador. Etiquetado y colores distintos para Ethernet y balanceador. Su router y su segmento, a cargo de ella | 11-12 / 10-11 | SEGURO |
| 5 | **Solo P2 a 14,49 kW**, P1 igual | IGA de 63 A, diferenciales, CIE de la vivienda **solo si hace falta** y gestión con comercializadora y e-distribución. El peaje 2.0TD no exige potencias crecientes | 8, 9, 17 / 7, 8, 16 | SEGURO (Circular 3/2020; e-distribución) |
| 6 | **Balanceo** con ControlBox y pinza; ~6,5 kW por coche | ControlBox y pinza incluidos; balanceo en serie. (14,49 kW − consumo nocturno) ÷ 2: 1,5 kW → 6,5 kW | 1 / — | SEGURO (V2C) |
| 7 | **Toma de garaje** con llave, línea y protección propias | 3G2,5, C10, diferencial de 30 mA tipo A, base en envolvente cerrada con llave. **C10, no C16** (Tabla 3 de la ITC-BT-52) | 13-14 / 12-13 | SEGURO (BOE) |
| 8 | **Dos líneas de 32 A** desde su cuadro; duda de los 40 A | Dos circuitos de 7,36 kW, 3G10, C40 y diferencial de 40 A cada uno. El límite de 40 A existe en el apartado 3.1 de la ITC-BT-52 (unifamiliares) y los circuitos lo cumplen | 3-6 / 3-5 | SEGURO |
| 9 | Lo que dio por incluido el 14/10 | Cargadores, ControlBox y pinza, cable y tubos, protecciones de línea y toma, IGA y diferenciales, montaje, **los dos CIE** y gestión de potencia. Lo que se cobra aparte está en las notas | todas | SEGURO |
| 10 | **Plazo: antes de Navidad** | Instalación y puesta en servicio antes del 31/12/2026; es fecha límite por la ISO (sección 2) | — | SEGURO |
| 11 | "¿Con o sin protecciones y cuántos cables?" | Sin protecciones integradas; protección en el cuadro. Dos cables Type 2, dos líneas de fuerza y cuatro tramos de cable de comunicación (ControlBox, Ethernet al maestro, Ethernet al extra y enlace A/B) en tubo aparte | — | SEGURO |
| 12 | Wi-Fi de 200 € | No se cobra | — | — |
| 13 | Mano de obra a 40 € + IVA/h | 22 h a 40 € | 15 / 14 | Horas: estimación |

### Diseño eléctrico, revisado
- **Circuitos:** cada Trydan Pro con su línea: RZ1-K (AS) 0,6/1 kV 3G10, C40 curva C bipolar y diferencial 2P 40 A, 30 mA, tipo A superinmunizado, exclusivo. ITC-BT-52 6.1 y 6.3 (protección individual del punto de conexión, corte omnipolar curva C) y manual del Trydan Pro (diferencial propio por cargador). [SEGURO]
- **Sección:** REBT ITC-BT-19, Tabla 1: 10 mm² en tubo, 2 conductores XLPE = 60 A. Con dos circuitos agrupados vale mientras el factor sea ≥ 0,67 (el habitual 0,8 da 48 A). Los dos cables comparten tubo solo los 7 m hasta el maestro. [Tabla: SEGURO · factor: **VERIFICAR** en la UNE 20460-5-523]
- **Caída de tensión** (límite 5 %): 7 m → 0,44 %; 12 m → 0,75 %. [límite SEGURO · cálculo mío]
- **Selectividad:** los C40 quedan por debajo del IGA de 63 A. [PROBABLE]
- **Sobretensiones:** protector permanente y transitorio en el cuadro (ITC-BT-52, 6.4). Según la distancia puede hacer falta otro junto a los cargadores; a 7 m [VERIFICAR con V2C].
- **Corriente continua residual:** el BOE solo exige diferencial clase A. La ficha del Trydan Pro da el detector DC como opcional. [VERIFICAR con V2C si es necesario]
- **Tierra y pruebas finales:** conductor de protección en todos los circuitos (ITC-BT-52, 6.1), continuidad del PE, medida de aislamiento y de bucle, disparo de los diferenciales, prueba del balanceo y de los llaveros. [PROBABLE: práctica habitual; entra en las 22 h]
- **Documentación:** MTD y CIE por TECI (la recarga de interior hasta 50 kW, no modo 4, figura en la lista de la Junta). Sin proyecto ni inspección de OCA (ITC-BT-04 e ITC-BT-05, 4.1.h). [SEGURO]
- **Cartel reflectante** en el punto de recarga y **iluminación mínima de 50 lux** a nivel de suelo: ITC-BT-52, apartado 5. La iluminación queda como exclusión a comprobar. [SEGURO]

---

## 2. ISO 15118-20: lo definitivo
- **Texto oficial** (anexo II del AFIR, punto 2.1.3, versión de la Comisión del 2/4/2025): los puntos de recarga privados de modo 3 y 4 "instalados o renovados a partir del 1 de enero de 2027" cumplirán al menos la EN ISO 15118-20:2022. [SEGURO]
- **Confirmado por V2C (Cristóbal, 12/11):** el Trydan Pro no cumple, y V2C no tendrá ISO hasta febrero o marzo de 2027. [SEGURO, chat]
- **Consecuencias:**
  1. El **31/12/2026** es una fecha límite dura. Un Trydan Pro instalado en 2027 no cumpliría la letra del punto 2.1.3.
  2. "Instalado" no está definido. **Fecha de referencia prudente:** obra terminada, CIE registrado en TECI y puesta en servicio, todo dentro de 2026. Guarda factura, albarán de entrega, fecha del CIE y fotos. [VERIFICAR con Industria de Cádiz el significado exacto]
  3. Una **sustitución o renovación posterior** del cargador (por avería o mejora) cae en la obligación: el nuevo debería cumplir. Hay que decírselo a la clienta.
  4. Si los equipos no llegan a tiempo no se puede instalar un Trydan Pro: la alternativa sería otro modelo con ISO declarada (por ejemplo, el Wallbox Pulsar Max, "preparado para ISO 15118"; sin confirmar potencia, disponibilidad ni cumplimiento). Presupuesto nuevo. [VERIFICAR]
  5. No encontré norma española que desarrolle el régimen de los puntos privados ni sanciones; no he podido abrir el texto final del DOUE; CharIN pidió aplazar a 2028 y no consta decisión. Planifica con el 1/1/2027. [VERIFICAR]
  6. Cargar los coches de hoy no cambia: los cargadores de modo 3 con señal PWM siguen funcionando; la norma añade comunicación de alto nivel (Plug & Charge, V2G). El RFID sigue siendo válido porque el reglamento no obliga a usar Plug & Charge. [PROBABLE + considerandos 21 y 24]

## 3. Calendario real desde el jueves 12/11/2026
| Fecha | Qué | Quién |
|---|---|---|
| Jue 12/11 | Enviar a la clienta el mensaje en ruso y los dos presupuestos. Pedir a Cristóbal stock, plazo y precio de 2 Trydan Pro (TRYPRO32-1-L5-ES) y que los **reserve** | Tú |
| Vie 13/11 | Comprar un llavero MIFARE 13,56 MHz de prueba; respuestas de V2C a las dudas técnicas | Tú |
| **Mar 17/11 o jue 19/11** | Visita técnica; boletín, foto del cuadro, plazas | Tú y clienta |
| **Vie 20/11** | **Último día para que acepte** y puedas pedir los equipos a tiempo | Clienta |
| 23–27/11 | Pedido de los equipos, MTD, comunicación de la clienta a la comunidad, consulta a e-distribución | Tú, clienta |
| 30/11–4/12 | **Equipos en obra, fecha límite** | V2C |
| 7–11/12 | Instalación (≈ 3 jornadas) y pruebas | Tú |
| 14–18/12 | CIE de la instalación en TECI y puesta en servicio. **15/12: si no hay equipos, la clienta puede desistir** | Tú |
| 21–23/12 | Margen para el CIE y la puesta en servicio | Tú |
| 24–31/12 | **Colchón final.** Fecha límite 31/12 | — |
El aumento a 14,49 kW depende de e-distribución (plazos de respuesta reducidos a la mitad para ≤ 15 kW; sin plazo publicado de ejecución): no lo prometas. Mientras tanto el balanceo reparte la potencia contratada actual.

## 4. Precio y margen
- **B:** base 4.852,60 €, **5.871,65 € con IVA**, margen 30.2 %, beneficio 1.465,04 €. Sin CIE de la vivienda: 5.520,75 €.
- **A:** base 2.654,60 €, **3.212,07 € con IVA**, margen 35.1 %, beneficio 932,04 €. Sin CIE de la vivienda: 2.861,17 €.
- **Comparación con la Alva** (4.883,89 € + Wi-Fi 242,00 € = 5.125,89 €): A más los cargadores de la web = 5.226,73 € (**+100,84 €**); B = 5.871,65 € (+745,76 €). Lo comparable que ya incluía cuesta 4.962,58 € y lo nuevo que ella pidió suma 909,07 €. Esto supone que esas partidas no estaban en el PDF 00039.
- **Si consigues tarifa de instalador** (descuentos supuestos, no datos): con V2C −10 % y materiales −20 %, B deja 35,5 % sin tocar el precio.
| Dto. V2C | Dto. materiales | Margen B | Beneficio B |
|---|---|---:|---:|
| 0 % | 0 % | 30.2 % | 1.465,04 € |
| 10 % | 20 % | 35.5 % | 1.723,92 € |
| 15 % | 25 % | 37.7 % | 1.830,27 € |
| 20 % | 30 % | 39.9 % | 1.936,61 € |
| 25 % | 35 % | 42.1 % | 2.042,95 € |

## 5. Pendientes
- **V2C (Cristóbal):** stock y plazo de 2 Trydan Pro; tarifa de instalador; las dudas técnicas del mensaje a Cristóbal (extra con Internet, longitud A/B, radios, RFID, e-Key, C32/C40, detector DC, protector, garantía).
- **Tú:** PDF 00039 y 00040; coste real por hora; precio real de la memoria técnica y de los dos CIE; garantía de instalación y pagos (propuestas mías a decidir); asesor para el desistimiento.
- **La clienta:** boletín (potencia máxima y fecha), P1 y P2, foto del cuadro, número y posición de las plazas y distancia entre ellas, iluminación del garaje, ubicación del router, administrador de la comunidad.
