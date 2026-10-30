# Agente de ciclo y fertilidad (adaptado a SOP)

Basado en el informe de Flo (6 abr – 4 nov 2026). No sustituye a un médico ni es anticonceptivo.

## Qué dicen tus datos
| Ciclo | Días | Nota |
|---|---|---|
| 6 abr – 18 may | 43 | |
| 19 may – 4 jun | 17 | regla de 1 día: probablemente manchado, no regla |
| 5 jun – 11 jul | 37 | |
| 12 jul – 26 ago | 46 | |
| 27 ago – 28 sep | 33 | |
| 29 sep – (4 nov previsto) | 37 previsto | hoy (30 oct) es el día 32 |

- Media 35 días, pero con rango 17–46. Si el sangrado de 1 día fue manchado, el ciclo real fue de 60 días.
- 3 de 4–5 ciclos superan los 35 días y la variación es mayor de 9 días: patrón compatible con ovulación infrecuente (SOP).
- **Relaciones**: casi todos los días del 6 al 35 del ciclo tienen relaciones sin protección (≈39 registros). Si ovulas, es casi seguro que había espermatozoides disponibles. Es decir, **el cuello de botella probable no es el momento, sino que no se ovule o se ovule muy tarde**. Calcular "días fértiles" con calendario no aportaría nada en tu caso.
- **Flujo tipo clara de huevo** en días 8, 13 y 14, y sensibilidad mamaria en varios picos (12–16, 28–30, 38–39, 43–44): hay varias señales hormonales por ciclo, pero el informe es agregado y no permite saber si hubo ovulación.
- Limitación: el PDF solo da conteos por día de ciclo, no fechas reales. Por eso `registro.csv` empieza vacío.

## Investigación (resumen y fuentes)
- Calendario/calculadoras: poco fiables con ciclos irregulares o SOP, y no detectan anovulación ([Guava](https://guavahealth.com/ovulation-calculator)).
- Ventana fértil ≈ 6 días: el esperma vive hasta 5 días y el óvulo ~24 h ([Essentia Health](https://www.essentiahealth.org/health-and-news/blog/obgyn-recognize-signs-ovulation-at-home-predictor-kits)).
- Test de LH: pueden salir positivos sin ovulación en SOP; predicen, no confirman ([Oova](https://www.oova.life/blog/opk-limitations)). Empieza antes de lo que dice la caja si tus ciclos son largos.
- Temperatura basal: confirma la ovulación a posteriori, no la predice; la alteran alcohol, enfermedad y sueño irregular. La confirmación médica es progesterona a mitad de fase lútea o ecografía.
- Guía internacional de SOP 2023: letrozol como primera opción para inducir ovulación; estilo de vida saludable como base, con evidencia de calidad baja-moderada ([guía](https://pcoschallenge.org/pdf/PCOS-Evidence-Based-Guideline.pdf), [resumen nórdico](https://pubmed.ncbi.nlm.nih.gov/37983875/)).
- Calidad de fuentes: varias son blogs de empresas de tests. Conviene contrastar con la guía original (monash.edu/medicine/mchri/pcos/guideline). No pude verificar en esta sesión lo que dice la guía sobre seguimiento de ovulación.

## Qué te recomiendo registrar (lo que más falta)
1. **Fecha de cada relación sin protección** (con fecha real, no solo en Flo).
2. **Temperatura basal** cada mañana, antes de levantarte.
3. **Test de LH** desde el día ~10 de cada ciclo, cada 1–2 días.
4. **Test de embarazo** cuando el agente lo indique.

## Uso
```bash
python3 agente.py estado
python3 agente.py registrar sexo_sin_proteccion --fecha 2026-10-28
python3 agente.py registrar temp 36.5
python3 agente.py registrar lh positivo
python3 agente.py inicio --dias 5     # cuando te baje la regla
```

## Cuándo consultar (independiente del agente)
- Buscando embarazo desde hace ≥3 meses con ciclos >35 días: pedir cita sin esperar 12 meses. Pueden valorar ovulación, resistencia a la insulina y tiroides, y ofrecer letrozol o metformina si procede.
- Si quieres evitar el embarazo: usa un método anticonceptivo real; con tu patrón el seguimiento del ciclo no protege.
- Sangrado muy abundante, dolor intenso o regla ausente >3 meses: consultar.
