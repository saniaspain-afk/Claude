#!/usr/bin/env python3
"""Agente de seguimiento de ciclo y fertilidad adaptado a ciclos irregulares (SOP).

Uso:
  python3 agente.py estado [--hoy AAAA-MM-DD]
  python3 agente.py registrar TIPO [VALOR] [--fecha AAAA-MM-DD]
  python3 agente.py inicio [--fecha AAAA-MM-DD] [--dias N]

TIPO: sexo_sin_proteccion | lh (positivo/negativo) | temp (grados C) |
      flujo (clara_huevo, cremoso...) | sintoma | prueba_embarazo (positiva/negativa)

Solo usa la libreria estandar. No es un metodo anticonceptivo ni diagnostico.
"""
import argparse
import csv
import statistics
from datetime import date, timedelta
from pathlib import Path

DATOS = Path(__file__).parent / "datos"
LIMITE_OLIGO = 35        # ciclos >35 dias: oligomenorrea (criterio SOP)
VARIACION_IRREGULAR = 9  # diferencia max-min >9 dias: ciclo irregular
ESPERA_TEST = 14         # dias tras la ultima relacion para un test fiable


def leer(nombre):
    ruta = DATOS / nombre
    if not ruta.exists():
        return []
    with ruta.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def fecha(s):
    return date.fromisoformat(s)


def cargar_ciclos():
    filas = sorted(leer("ciclos.csv"), key=lambda r: r["inicio"])
    return [(fecha(r["inicio"]), int(r["dias_regla"] or 0)) for r in filas]


def longitudes(ciclos, fusionar_manchado=False):
    """Longitudes de los ciclos completos. Con fusionar_manchado, un sangrado
    de <=2 dias se trata como manchado y no como inicio de ciclo."""
    inicios = [i for i, d in ciclos]
    if fusionar_manchado:
        inicios = [i for i, d in ciclos if d > 2 or i == ciclos[0][0]]
    return [(b - a).days for a, b in zip(inicios, inicios[1:])]


def resumen(lens):
    if not lens:
        return "sin datos suficientes"
    return (f"{len(lens)} ciclos: {lens} | media {statistics.mean(lens):.1f}, "
            f"mediana {statistics.median(lens):.0f}, min {min(lens)}, max {max(lens)}")


def evidencia_ovulacion(registro):
    """Busca subida termica sostenida (3 dias >=0.2C sobre los 6 previos)."""
    temps = sorted((fecha(r["fecha"]), float(r["valor"]))
                   for r in registro if r["tipo"] == "temp")
    hallazgos = []
    for i in range(6, len(temps) - 2):
        base = max(t for _, t in temps[i - 6:i])
        if all(t >= base + 0.2 for _, t in temps[i:i + 3]):
            hallazgos.append(temps[i][0])
    lh = [fecha(r["fecha"]) for r in registro
          if r["tipo"] == "lh" and r["valor"].lower().startswith("pos")]
    return hallazgos, lh


def estado(hoy):
    ciclos = cargar_ciclos()
    registro = leer("registro.csv")
    out = []
    p = out.append

    p(f"=== Estado del ciclo a {hoy.isoformat()} ===")
    todas = longitudes(ciclos)
    fusion = longitudes(ciclos, fusionar_manchado=True)
    p(f"Ciclos (tal cual Flo):      {resumen(todas)}")
    if fusion != todas:
        p(f"Ciclos (manchado fusionado): {resumen(fusion)}")
    ref = fusion or todas
    if ref:
        variacion = max(ref) - min(ref)
        largos = sum(1 for x in ref if x > LIMITE_OLIGO)
        p(f"Patron: variacion {variacion} dias entre el mas corto y el mas largo; "
          f"{largos}/{len(ref)} ciclos >{LIMITE_OLIGO} dias.")
        if variacion > VARIACION_IRREGULAR or largos:
            p("  -> Ciclos irregulares/largos, compatibles con ovulacion poco frecuente "
              "(coherente con SOP). Las predicciones por calendario NO son fiables.")

    inicio_actual = ciclos[-1][0]
    dia = (hoy - inicio_actual).days + 1
    p(f"\nCiclo actual: empezo el {inicio_actual}, hoy es el dia {dia}.")
    if ref:
        previsto_min = inicio_actual + timedelta(days=min(ref))
        previsto_max = inicio_actual + timedelta(days=max(ref))
        mediana = inicio_actual + timedelta(days=int(statistics.median(ref)))
        p(f"Proxima regla probable: entre {previsto_min} y {previsto_max} "
          f"(centro ~{mediana}). Rango amplio a proposito: tus ciclos varian mucho.")
        retraso = (hoy - previsto_max).days
        if retraso > 0:
            p(f"  ! Llevas {retraso} dias mas que tu ciclo mas largo registrado.")

    relaciones = sorted(fecha(r["fecha"]) for r in registro
                        if r["tipo"] == "sexo_sin_proteccion")
    ultima = relaciones[-1] if relaciones else None
    pruebas = [r for r in registro if r["tipo"] == "prueba_embarazo"]
    p("\n--- Prueba de embarazo ---")
    if pruebas and pruebas[-1]["valor"].lower().startswith("pos"):
        p("Test positivo registrado: confirma con ginecologia/atencion primaria y "
          "empieza acido folico 400 mcg/dia si no lo tomas.")
    elif ultima is None:
        p("No hay relaciones sin proteccion registradas: sin datos para recomendar test.")
    else:
        desde = (hoy - ultima).days
        apto = ultima + timedelta(days=ESPERA_TEST)
        p(f"Ultima relacion sin proteccion: {ultima} (hace {desde} dias).")
        if hoy < apto:
            p(f"Un test ahora podria dar falso negativo. Fecha minima fiable: {apto}.")
        elif ref and dia > min(ref):
            p("Ya han pasado >=14 dias desde la ultima relacion y la regla no ha bajado: "
              "haz un test de embarazo (orina matutina). Si es negativo y sigue sin bajar, "
              "repite a los 3-7 dias.")
        else:
            p("Puedes hacer un test si lo deseas; es fiable desde hoy.")

    p("\n--- Senales de ovulacion en este registro ---")
    subidas, lh = evidencia_ovulacion(registro)
    if subidas:
        p(f"Subida de temperatura basal sostenida desde: {subidas[-1]} (ovulacion probable, "
          f"confirmada a posteriori).")
    elif lh:
        p(f"LH positivo el {lh[-1]}: posible ovulacion, pero en SOP puede haber falsos "
          f"positivos; confirma con temperatura o progesterona.")
    else:
        p("Sin temperatura ni test de LH registrados: no hay forma de saber si ovulas. "
          "Es el dato que mas falta (ver README).")

    p("\n--- Avisos ---")
    if not registro:
        p("El registro diario esta vacio: el informe de Flo solo trae agregados por dia de "
          "ciclo, no fechas concretas. Registra desde hoy con 'registrar'.")
    p("Esto no es un anticonceptivo ni un diagnostico. Con >=3 meses buscando embarazo y "
      "ciclos >35 dias, consulta con ginecologia sin esperar 12 meses.")
    return "\n".join(out)


def añadir_registro(tipo, valor, dia):
    ruta = DATOS / "registro.csv"
    with ruta.open("a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([dia.isoformat(), tipo, valor])


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("estado")
    e.add_argument("--hoy", default=date.today().isoformat())
    r = sub.add_parser("registrar")
    r.add_argument("tipo")
    r.add_argument("valor", nargs="?", default="")
    r.add_argument("--fecha", default=date.today().isoformat())
    i = sub.add_parser("inicio")
    i.add_argument("--fecha", default=date.today().isoformat())
    i.add_argument("--dias", default="")
    a = ap.parse_args()

    if a.cmd == "estado":
        print(estado(fecha(a.hoy)))
    elif a.cmd == "registrar":
        añadir_registro(a.tipo, a.valor, fecha(a.fecha))
        print("Registrado.")
    elif a.cmd == "inicio":
        with (DATOS / "ciclos.csv").open("a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([a.fecha, a.dias, ""])
        print("Nuevo ciclo registrado.")


if __name__ == "__main__":
    main()
