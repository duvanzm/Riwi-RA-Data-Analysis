#                                                                   --- UV ASTRAL ---
#                                              ------------------------------------------------------- 


#      --- Como iniciar mi Primer Proyecto con un entorno virtual: ---

# Flujo ideal completo 

# uv init mi_app                    / crea el proyecto
# uv venv                           / crea el entorno
# source .venv/bin/activate         / Se debe realizar antes de agregar depenmdencias / activa el entorno (todo ocurre dentro del proyecto no en el sistema global.) 

# uv pip install pandas matplotlib  / No recomendado * NO registra las dependencias en tu proyecto / No actualiza pyproject.toml
# uv add pandas matplotlib          / instala y agrega al mismo tiempo * Ideal  / Se guarda en pyproject.toml (uv init), Se instala en .venv   

# Ahora para cambiar salir y cambiar a otro entorno:

# deactivate                        / apago mi entorno actual 
# cd proyecto_2                     / cambio a otro proyecto 
# source .venv/bin/activate         / activo este nuevo entorno 

#--------------------------------------------------------------------------------------- 

#                           --- uv init ---
#
#   Es la parte teórica / declarativa
#
# mi_proyecto/                 # Carpeta raíz del proyecto
# ├── pyproject.toml           # Archivo principal del proyecto (dependencias, config, metadata)
# ├── README.md                # Descripción del proyecto (para GitHub/documentación)
# ├── main.py                  # Punto de entrada del programa (donde inicia la ejecución)
# └── .python-version          # Versión de Python sugerida para el proyecto



#                           --- .venv ---
#
#  Es la parte práctica / real
#
# .venv/                      # Carpeta del entorno virtual (aisla tu proyecto)
# ├── bin/                    # Ejecutables del entorno (Python, pip, uv, etc.)
# │   ├── python              # Intérprete de Python propio del entorno
# │   ├── pip                 # Gestor de paquetes dentro del entorno
# │   └── activate            # Script para activar el entorno
# ├── lib/                    # Librerías instaladas (dependencias del proyecto)
# │   └── python3.x/          # Versión específica de Python
# │       └── site-packages/  # Aquí viven pandas, matplotlib, etc.
# ├── include/                # Archivos de cabecera (usados por compilaciones C/C++)
# └── pyvenv.cfg              # Configuración del entorno (versión de Python, rutas)


#                      --- COMANDOS UV ---

#   Son la forma práctica de gestionar dependencias
#   (instalar, registrar y sincronizar tu proyecto)

# uv add pandas            / Agrega la dependencia al proyecto (pyproject.toml) + la instala en .venv
#                          / Uso recomendado (modo profesional)
#
# uv pip install pandas    / Solo instala en el entorno (.venv)
#                          / No la guarda en el proyecto
#                          / Útil solo para pruebas rápidas
#
# uv sync                  / Sincroniza el entorno (.venv) con pyproject.toml
#                           / Instala, actualiza y elimina paquetes para que todo coincida


#     --- Organizar tu proyecto (MUY recomendado) ---

# No trabajes todo en main.py. Empieza a estructurar:

# mi_app/
# ├── main.py              # punto de entrada
# ├── src/                 # lógica del proyecto
# │   ├── __init__.py
# │   └── data.py          # ejemplo: manejo de datos
# ├── data/                # archivos (csv, json, etc.)
# └── notebooks/ (opcional)# pruebas o exploración


