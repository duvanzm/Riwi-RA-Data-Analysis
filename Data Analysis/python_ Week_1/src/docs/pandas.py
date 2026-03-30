#                                                                --- Pandas ---
#                                            --------------------------------------------------

#    Que es pandas :

# Su nombre viene de panel de datos, es una biblioteca de Python de código abierto, fundamental para la ciencia de datos, que proporciona estructuras rápidas y flexibles para manipular, limpiar y analizar datos tabulares (filas y columnas), similar a una hoja de cálculo de Exel. Se basa en NumPy y es ideal para trabajar con datos estructurados, series temporales y conjuntos de datos relacionales.

# Características y usos principales:

# Estructuras de datos: Introduce los DataFrames (tablas bidimensionales) y Series (unidimensionales) para organizar datos.

# Manipulación de datos: Permite filtrar, agrupar, ordenar, combinar (merge/join) y transformar conjuntos de datos complejos con facilidad.

# Gestión de datos faltantes: Ofrece herramientas potentes para detectar y manejar datos nulos o perdidos.

# Lectura/Escritura de archivos: Importa y exporta datos de múltiples formatos, incluyendo CSV, Excel, SQL y JSON.

# Análisis Temporal: Especializada en el manejo de series temporales, permitiendo indexar y convertir frecuencias. 

# Pandas es, junto con Matplotlib y Scikit-Learn, una de las herramientas más utilizadas en el ecosistema de análisis de datos. 


#   Series : 

import pandas as pd;

list = [10, 12, 18, 19]

serie = pd.Series(list)

print(serie)