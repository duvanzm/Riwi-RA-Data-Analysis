# UV Astral

---

## Cómo iniciar mi primer proyecto con un entorno virtual

### Flujo ideal completo

```bash
uv init mi_app
uv venv
source .venv/bin/activate
```

- `uv init mi_app`: crea el proyecto  
- `uv venv`: crea el entorno  
- `source .venv/bin/activate`: activa el entorno (todo ocurre dentro del proyecto, no en el sistema global)

---

### Instalación de dependencias

```bash
uv pip install pandas matplotlib
```

No recomendado:
- No registra las dependencias en tu proyecto  
- No actualiza `pyproject.toml`  

```bash
uv add pandas matplotlib
```

Recomendado:
- Instala y agrega al mismo tiempo  
- Se guarda en `pyproject.toml`  
- Se instala en `.venv`  

---

### Cambiar de entorno

```bash
deactivate
cd proyecto_2
source .venv/bin/activate
```

- `deactivate`: apaga el entorno actual  
- `cd proyecto_2`: cambia de proyecto  
- `source .venv/bin/activate`: activa el nuevo entorno  

---

## uv init

Es la parte teórica / declarativa

```text
mi_proyecto/
├── pyproject.toml
├── README.md
├── main.py
└── .python-version
```

- `pyproject.toml`: dependencias, configuración y metadata  
- `README.md`: documentación del proyecto  
- `main.py`: punto de entrada  
- `.python-version`: versión de Python sugerida  

---

## .venv

Es la parte práctica / real

```text
.venv/
├── bin/
│   ├── python
│   ├── pip
│   └── activate
├── lib/
│   └── python3.x/
│       └── site-packages/
├── include/
└── pyvenv.cfg
```

- `bin/`: ejecutables del entorno  
- `lib/`: librerías instaladas  
- `site-packages/`: paquetes como pandas o matplotlib  
- `include/`: archivos para compilaciones  
- `pyvenv.cfg`: configuración del entorno  

---

## Comandos UV

```bash
uv add pandas
```
- Agrega la dependencia al proyecto (`pyproject.toml`)  
- La instala en `.venv`  
- Uso recomendado  

```bash
uv pip install pandas
```
- Solo instala en el entorno  
- No la guarda en el proyecto  
- Útil para pruebas rápidas  

```bash
uv sync
```
- Sincroniza `.venv` con `pyproject.toml`  
- Instala, actualiza o elimina paquetes  

---

## Organización del proyecto (muy recomendado)

No trabajes todo en `main.py`. Usa una estructura como:

```text
mi_app/
├── main.py
├── src/
│   ├── __init__.py
│   └── data.py
├── data/
└── notebooks/
```

- `main.py`: punto de entrada  
- `src/`: lógica del proyecto  
- `data/`: archivos (csv, json, etc.)  
- `notebooks/`: pruebas o exploración (opcional)  
