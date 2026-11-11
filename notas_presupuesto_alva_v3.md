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
