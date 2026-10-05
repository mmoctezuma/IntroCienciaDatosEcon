# Guía de Calificación — Tarea 2: EDA y Series de Tiempo
## EO4040 Introducción a la Ciencia de Datos para Economía
**Tecnológico de Monterrey — Gobierno y Transformación Pública**

---

## Archivos de la tarea

| Archivo | Destinatario | Descripción |
|---|---|---|
| `tarea2_alumno.ipynb` | Estudiantes | Notebook con espacios `...` para rellenar |
| `tarea2_master.ipynb` | Profesor (no compartir) | Notebook maestro con soluciones y tests |
| `dist/autograder/tarea2_master-autograder_*.zip` | Profesor | Paquete para calificación automática con otter run |

---

## Qué compartir con los estudiantes

Comparte únicamente `tarea2_alumno.ipynb`. No compartas el master ni el directorio `dist/`.

Instrucciones para incluir en Canvas u otro LMS:

```
Descarga tarea2_alumno.ipynb y ábrelo en Google Colab o Jupyter.
Ejecuta las celdas en orden. Reemplaza cada bloque "..." con tu código.
No modifiques las celdas de configuración, datos ni tests.
Al terminar, descarga tu notebook (File > Download > Download .ipynb)
y súbelo a Canvas antes de la fecha límite.
```

---

## Estructura de puntuación

| Componente | Puntos |
|---|---|
| Calificación automática (otter) | 80 pts |
| Presentación en clase | 20 pts |
| **Total** | **100 pts** |

### Desglose automático

| Pregunta | Tema | Puntos |
|---|---|---|
| Q1 | Tabla de frecuencias (variable categórica) | 10 |
| Q2 | Estadísticas descriptivas + asimetría (PIB) | 10 |
| Q3 | Matriz de correlación de Pearson | 10 |
| Q4 | Estadísticas por grupo (mediana desempleo) | 10 |
| Q5 | Preparación de serie de tiempo con PeriodIndex | 10 |
| Q6 | Descomposición seasonal (tendencia + residuos) | 10 |
| Q7 | Función de autocorrelación ACF (lags 0-5) | 10 |
| Q8 | Regresión OLS + diagnóstico Durbin-Watson | 10 |

---

## Entorno requerido

Otter-grader 7.0.0 debe estar instalado en el entorno de calificación.

```bash
pip install otter-grader==7.0.0 wbgapi statsmodels -q
```

Los datos se descargan automáticamente vía wbgapi (Banco Mundial). El entorno de calificación necesita acceso a internet para la primera ejecución. Si el entorno no tiene acceso, ver sección "Calificación sin internet" al final.

---

## Calificar un notebook de estudiante

### Método 1: otter run (recomendado, un notebook a la vez)

```bash
otter run tarea2_alumno_NOMBRE.ipynb \
    -a dist/autograder/tarea2_master-autograder_*.zip \
    --no-logo
```

El resultado muestra la puntuación por pregunta y el total.

### Método 2: otter grade (batch, varios notebooks)

Coloca todos los notebooks entregados en un directorio, por ejemplo `entregas/`:

```bash
mkdir entregas
# copia aquí los notebooks descargados de Canvas

otter grade \
    --notebooks entregas/ \
    --autograder dist/autograder/tarea2_master-autograder_*.zip \
    --output-dir resultados/ \
    --no-logo
```

Los resultados se guardan en `resultados/final_grades.csv`.

### Verificar el autograder (prueba con la solución completa)

Para confirmar que el autograder funciona correctamente antes de la entrega, prueba calificando el propio master:

```bash
otter run tarea2_master.ipynb \
    -a dist/autograder/tarea2_master-autograder_*.zip \
    --no-logo
```

Debe reportar **80/80 puntos** (10 por cada una de las 8 preguntas).

---

## Rúbrica para los 20 puntos de presentación

Cada grupo presenta 10 minutos en clase. Evalúa con la siguiente rúbrica.

| Criterio | 5 pts | 3-4 pts | 1-2 pts | 0 pts |
|---|---|---|---|---|
| Claridad técnica | Explican correctamente todos los conceptos usados | Explican la mayoría con alguna imprecisión | Explicaciones superficiales o incorrectas | No explican |
| Interpretación económica | Conectan resultados con contexto económico de manera sólida | Mencionan algún contexto pero con poca profundidad | Poca o ninguna interpretación | Sin interpretación |
| Visualizaciones | Gráficas claras, bien etiquetadas, pertinentes | Gráficas presentes pero con deficiencias menores | Gráficas confusas o ausentes | Sin visualizaciones |
| Conclusiones | Conclusiones claras, basadas en evidencia, relevantes para política pública | Conclusiones presentes pero poco sustentadas | Conclusiones vagas o incorrectas | Sin conclusiones |

**Total máximo: 20 puntos**

---

## Preguntas frecuentes

**¿Por qué `period=2` en seasonal_decompose si los datos son anuales?**
Los datos son anuales por definición (una observación por año), por lo que no existe estacionalidad en el sentido clásico. Usamos `period=2` únicamente como parámetro mínimo técnico para que la función extraiga tendencia de mediano plazo. El foco de la pregunta es la tendencia y los residuos, no la componente estacional.

**¿Qué pasa si los datos del Banco Mundial cambian?**
Los tests están escritos con rangos flexibles donde sea posible (p.ej. `20 <= n_obs_col <= 24`). La pregunta 1 (conteo de países) y la pregunta 3 (orden de correlaciones) son deterministas. Si los datos cambian sustancialmente, revisa los tests en `tarea2_master.ipynb` antes de usarlo en un nuevo periodo.

**¿Se puede usar Colab sin internet para calificar?**
No directamente — wbgapi necesita internet para descargar. Alternativa: ejecuta el notebook de descarga de datos una vez, guarda los DataFrames como CSV, y reemplaza la celda de descarga por una lectura de CSV. Contacta al asistente de la materia si necesitas esta variante.

---

## Regenerar el autograder

Si modificas `tarea2_master.ipynb`, regenera el autograder con:

```bash
rm -rf dist/
otter assign tarea2_master.ipynb dist/ --no-run-tests
cp dist/student/tarea2_master.ipynb tarea2_alumno.ipynb
```

Vuelve a distribuir `tarea2_alumno.ipynb` a los estudiantes.
