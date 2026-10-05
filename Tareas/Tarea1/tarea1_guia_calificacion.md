# Tarea 1 — Guía de calificación
## EO4040 Introducción a la Ciencia de Datos para Economía

---

## Archivos

| Archivo | Uso |
|---|---|
| `tarea1_alumno.ipynb` | Distribuyes a los alumnos por Canvas |
| `tarea1_master.ipynb` | Solo para ti — tiene las soluciones |
| `tarea1_autograder.zip` | Solo para ti — para calificar con `otter run` |
| `tests/q1.py … q8.py` | Súbelos a GitHub (carpeta `tests/`) |

---

## Setup inicial (una sola vez)

```bash
pip install otter-grader==5.5.0
```

---

## Flujo del alumno

1. Descarga `tarea1_alumno.ipynb` de Canvas
2. Lo abre en Google Colab
3. Sube `concentradohogar.csv` desde: https://www.inegi.org.mx/programas/enigh/nc/2022/
4. Corre todas las celdas en orden — la celda 1 descarga los tests de GitHub automáticamente
5. Al terminar corre la celda final `grader.export()` y sube el `.zip` a Canvas

---

## Cómo calificar

Descarga los `.zip` de Canvas. Por cada alumno:

```bash
otter run alumno.zip --autograder tarea1_autograder.zip --no-logo
```

O para calificar todos a la vez:

```bash
for f in entregas/*.zip; do
    echo "--- Calificando: $f ---"
    otter run "$f" --autograder tarea1_autograder.zip --no-logo
done
```

---

## Distribución de puntos (80 pts automáticos)

| Pregunta | Pts | Qué verifica |
|---|---|---|
| q1 | 10 | CSV cargado correctamente (filas, columnas, folioviv) |
| q2 | 10 | tabla_calidad con 4 columnas, todas las variables, rango correcto |
| q3 | 10 | vars_con_faltantes, n_duplicados, col_mas_faltantes correctos |
| q4 | 10 | df original intacto, df_clean sin duplicados en folioviv |
| q5 | 10 | rename de ing_cor a ingcor, indicador binario, sin NaN tras imputar |
| q6 | 10 | est_socio es category ordenada con categorías [1,2,3,4] |
| q7 | 10 | reporte con estructura y valores correctos |
| q8 | 10 | CSV guardado, df_verificacion con dimensiones correctas |

---

## Presentación en clase (20 pts)

Duración: 5 minutos por alumno. Preguntar al menos 2 de estas 4:

| Pregunta | 5 pts | 3 pts | 0 pts |
|---|---|---|---|
| ¿Cuántas variables con faltantes y cuál tiene más? | Cita número exacto y da hipótesis | Cita el número, sin hipótesis | No recuerda |
| ¿Por qué mediana y no media para ingcor? | Explica asimetría del ingreso y efecto de outliers | "Porque es más robusta" sin más | No sabe la diferencia |
| Si el faltante es MNAR, ¿qué sesgo introduce la mediana? | Explica que sobrerepresenta ingresos medios | "Puede haber sesgo" sin precisar | No conoce MCAR/MAR/MNAR |
| ¿Cómo afecta ese sesgo a un análisis de desigualdad? | Conecta con subestimación del GINI | Menciona error en política | No conecta los conceptos |

---

## Notas importantes

- La variable en la ENIGH 2022 se llama `ing_cor` (con guion bajo). El alumno debe renombrarla a `ingcor` en la pregunta 5.
- `ing_cor` no tiene valores faltantes en la ENIGH 2022 — es normal que `ingcor_faltante` quede en cero.
- Los tests dependen del CSV oficial de INEGI. Si el alumno usa otro archivo, q1 fallará.
