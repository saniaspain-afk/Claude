# Alva (Sotogrande) – presupuesto nuevo: qué hay que cerrar antes de enviarlo

Fichero: `presupuestos_v3_alva_stel_order.xlsx` (misma estructura que el v2c: Concepto / Cantidad / Precio unit. / Importe).
Hay 2 hojas, porque la clienta plantea dos caminos válidos según su lectura del manual:
1. **Alva CON protecciones**: 1 línea de 63 A (RZ1-K 3G25).
2. **Alva SIN protecciones**: 2 líneas de 32 A, una por toma.

En ambas: 2 mangueras Tipo 2 de 5 m fijas (no tomas), 3 llaveros RFID, ControlBox con pinzas, UTP aparte de la fuerza, toma de garaje con llave, IGA 63 A + diferenciales, 2 CIE y gestión Endesa.

## Celdas amarillas = dato que yo no tengo (no lo invento)
Precio = coste × 1,5 (tu criterio). Solo hay que rellenar el coste (col. E) y las cantidades. Hasta entonces la celda ESTADO dice INCOMPLETO.
- Coste de la Alva en cada versión (el 1.205 € del v2c no sé a qué versión corresponde).
- Metros reales de línea, tubo y UTP (el v2c asumía 10 m; con 63 A y 25 mm² la longitud pesa mucho).
- Nº de diferenciales a cambiar, horas de mano de obra, coste de los 2 CIE.
- Llaveros: cuántos trae el kit y si el ControlBox viene incluido.
- Los importes enviados el 13/10 (4.883,89 € y 5.500,19 € con IVA) NO coinciden con los del repo (3.937,95 € y 4.922,28 €). Confirma qué lista de precios es la vigente.

## Puntos delicados (la clienta los comprobará con ChatGPT)
- **Tu mensaje del 14/10 dijo que la Alva solo tiene un ingreso y que dos líneas no se permiten. La clienta cita el manual (págs. 9 y 19): la versión sin protecciones tiene dos entradas.** La web de V2C confirma que hay dos variantes de instalación (con/sin protecciones) y que la de protecciones se alimenta por el seccionador de entrada. No he podido leer el PDF completo, así que compruébalo tú en el manual antes de contestar. Si ella tiene razón, conviene reconocerlo.
- Tu mensaje dejó sin rellenar `[Отдельно считается: ...]`. Hay que listar lo excluido: tasas de Industria, derechos de acceso/extensión de Endesa, router y segmentación de red (de ella), obras de albañilería.
- Pregunta del 3/11 sin contestar: ¿llegamos antes de Navidad? No prometer fecha, depende de Endesa/Industria.
- Tu mensaje del 14/10 decía diferencial "tipo A" a secas; en los presupuestos anteriores era "tipo A + 6 mA CC". Lo dejé con 6 mA CC; confirma si la Alva con protecciones ya lo integra.
- Sección: 25 mm² para 63 A es lo que recomendaste; las 2 líneas de 32 A van con 3G6 como en el v2c, revísalo si la distancia es larga.
- Todo el redactado técnico (ITC-BT-52, qué certificados exige Endesa) debe validarlo tu instalador autorizado antes de enviarlo.

## Costes investigados (11/11/2026)
**Verificado en la tienda oficial de V2C (PVP, IVA incluido; coste sin IVA = precio / 1,21):**
| Artículo | PVP IVA incl. | Sin IVA |
|---|---:|---:|
| Alva 7,4 kW monofásico, 2 cables lisos 5 m, SIN protecciones, sin MID (ALV-X2-32-1-L5-ES) | 1.566,95 € | 1.295,00 € |
| Alva 7,4 kW monofásico, 2 cables lisos 5 m, CON protecciones, sin MID (ALV-X2-32-1-L5-P-ES) | 1.929,95 € | 1.595,00 € |
| Tarjeta RFID | 4,17 € | 3,45 € |
| Detector de fugas DC (accesorio) | 97,79 € | 80,82 € |
| Medidor bidireccional monofásico + 1 pinza 120 A | 75,81 € | 62,65 € |

Ya están en el Excel los costes de las dos Alva y de la tarjeta RFID. Son PVP minorista: con tarifa de instalador V2C el coste baja.

**Lo que dice el manual de V2C (lo que la clienta ya habrá leído):**
- Alva tiene dos variantes de instalación. Con protecciones: los cables entran por un racor y van al seccionador principal. Sin protecciones: se conectan a bornas, a cada lado. Esto respalda su lectura.
- El ControlBox va provisto con la Alva, pero hay que instalar la pinza amperimétrica (CT) que mide el consumo total. El Excel ya no lo pone como ControlBox sino como pinza.
- Cada estación debe ir con su propio diferencial de 30 mA tipo A como máximo, sin otros circuitos en él.
- En la lista de accesorios incluidos no aparecen llaveros ni tarjetas RFID. Lo que dijiste de "брелки в комплекте" conviene comprobarlo.
- El detector de fugas DC es un accesorio aparte: pregunta a V2C si la versión sin protecciones lo necesita (6 mA CC).

**No encontrado (no lo he puesto en el Excel):** precios de Saltoki, Rexel y Sonepar (solo con cuenta de cliente), cable 3G25/3G6, magnetotérmicos C63/C32, diferenciales de 63 A y 40 A, IGA, sobretensiones, UTP, base con llave. Solo salen precios minoristas dispares (p. ej. magnetotérmico 2P 63 A C: 44–76 €; diferencial 2P 40 A tipo A: 39–90 €), que no valen como coste de instalador. Esos los tienes que sacar de tu tarifa.

## Costes de Obramat y Leroy Merlin + mano de obra (11/11/2026)
**Advertencia sobre la fuente:** Obramat bloquea el acceso automático a sus fichas, así que no pude abrirlas. Los precios salen de los resultados de búsqueda de Obramat y Leroy Merlin (que reflejan la ficha). Algunas fichas de Obramat dan precio con IGIC (Canarias): las descarté y usé solo las que indican IVA. **Verifica cada precio en la web antes de enviar.**

| Partida | Fuente | PVP | Sin IVA (en Excel) |
|---|---|---:|---:|
| Magnetotérmico 2P 63 A C 6 kA (y IGA 63 A) | Obramat, Hager | 56,21 € | 46,45 € |
| Magnetotérmico 2P 32 A C | Obramat, Schneider Acti9 | 21,82 € | 18,03 € |
| Diferencial 2P 40 A 30 mA tipo A superinmunizado | Obramat, Schneider | 47,50 € | 39,26 € |
| Protector sobretensiones permanente + transitorio | Leroy Merlin, Toscano COMBI 2P50T15 | 89,57 € | 74,02 € |
| Cable 3G6 RZ1-K | Obramat (otra ficha dice 1,55 €/m; dudoso) | | 3,06 €/m |
| UTP Cat6A | Obramat | 0,92 €/m | 0,76 €/m |
| Detector de fugas DC (solo versión sin protecciones) | tienda V2C | 97,79 € | 80,82 € |

**Sin precio fiable (siguen amarillas):** cable 3G25 (ni Obramat ni Leroy lo tienen; 3G16 en Leroy desde 10,29 €/m), diferencial 2P 63 A tipo A (el de Obramat no indica el tipo; el tipo A de Leroy es de un vendedor marketplace), C16 y diferencial de la toma de garaje, base con llave, tubos, pinza del ControlBox, CIE.

**Mano de obra:** 40 €/h sin IVA (+ IVA 21 % en el total) como precio de venta fijo, sin margen; coincide con lo comunicado al cliente el 1/10. Faltan las horas.

**Cambio respecto a la versión anterior:** quité "+6 mA CC" de los diferenciales de línea. El manual de V2C pide solo diferencial de 30 mA tipo A, exclusivo de cada estación. Para la versión sin protecciones añadí 2 detectores de fugas DC (accesorio V2C) a confirmar con V2C. La versión con protecciones ya integra tipo A 30 mA / 6 mA CC por toma según la ficha técnica.
