# Tarea 1 — Guía de calificación con otter-grader
## EO4040 Introducción a la Ciencia de Datos para Economía

---

## Archivos que tienes

| Archivo | Uso |
|---|---|
| `tarea1_alumno.ipynb` | **Este es el que distribuyes a los alumnos** |
| `tarea1_master.ipynb` | Solo para ti — tiene las soluciones y los tests |

---

## Setup (una sola vez)

```bash
pip install otter-grader
```

---

## Flujo de trabajo

### 1. Distribuir la tarea
Sube `tarea1_alumno.ipynb` a Canvas como archivo descargable.  
Los alumnos también necesitan descargar `concentradohogar.csv` desde:  
https://www.inegi.org.mx/programas/enigh/nc/2022/

### 2. Recibir las entregas
Descarga todos los notebooks de Canvas. Ponlos en una carpeta, por ejemplo:
```
entregas/
  alumno01.ipynb
  alumno02.ipynb
  ...
```
Cada alumno debe haber colocado `concentradohogar.csv` en la misma carpeta que su notebook antes de correrlo — el CSV estará embebido en los outputs de las celdas.

### 3. Calificar automáticamente (un solo comando)
```bash
otter run alumno01.ipynb --autograder tarea1_master.ipynb
```

O para calificar todos a la vez:
```bash
for f in entregas/*.ipynb; do
    echo "--- Calificando: $f ---"
    otter run "$f" --autograder tarea1_master.ipynb
done
```

La salida muestra los puntos obtenidos por pregunta y el total sobre 80.

### 4. Alternativa: calificación no-containerizada (más rápida, sin Docker)
```bash
otter run alumno01.ipynb --autograder tarea1_master.ipynb --no-containers
```

---

## Distribución de puntos automáticos (80 pts)

| Pregunta | Pts | Qué verifica |
|---|---|---|
| q1 | 10 | El CSV se cargó correctamente (filas, columnas, columna folioviv) |
| q2 | 10 | tabla_calidad tiene las 4 columnas, cubre todas las variables, rango correcto |
| q3 | 10 | vars_con_faltantes correcta, n_duplicados correcto, col_mas_faltantes correcto |
| q4 | 10 | df original intacto, df_clean sin duplicados en folioviv |
| q5 | 10 | ingcor sin NaN, indicador binario correcto, conteo consistente |
| q6 | 10 | est_socio es category ordenada con categorías [1,2,3,4] |
| q7 | 10 | reporte con estructura y valores correctos, limpieza mejoró |
| q8 | 10 | CSV guardado, df_verificacion con dimensiones correctas |

---

## Presentación en clase (20 pts) — rúbrica sugerida

Duración: 5 minutos por alumno. Preguntar al menos 2 de estas 4:

| Pregunta | 5 pts = excelente | 3 pts = suficiente | 0 pts = no sabe |
|---|---|---|---|
| ¿Cuántas variables con faltantes y cuál tiene más? | Cita el número exacto y da una hipótesis sobre por qué | Cita el número, sin hipótesis | No recuerda o no corrió el diagnóstico |
| ¿Por qué mediana y no media para ingcor? | Explica la asimetría del ingreso y el efecto de los outliers | "Porque es más robusta" sin más | No sabe la diferencia |
| Si el faltante es MNAR, ¿qué sesgo introduce la mediana? | Explica que sobrerepresenta ingresos medios | "Puede haber sesgo" sin precisar | No conoce MCAR/MAR/MNAR |
| ¿Cómo afecta ese sesgo a un análisis de desigualdad? | Conecta con subestimación del GINI o coeficiente de Atkinson | Menciona que puede haber error en la política | No conecta los conceptos |

---

## Notas
- Los tests son deterministos: el resultado correcto depende únicamente del archivo CSV oficial de la ENIGH 2022.
- Si un alumno usa un archivo diferente o con nombre distinto, q1 fallará y el resto de la cadena también — está diseñado así intencionalmente.
- La pregunta de presentación 3 (MNAR) es la más difícil — es normal que pocos la respondan perfectamente.
