<img src="../assets/img/python-logo.png" />

[<< Inicio](./README.md) [< Volver](./terminal_read.md) || [siguiente >](./read_csv_file.md)

---

## Lectura de archivo

```python
file = open("ruta al archivo", "r")
print(file)
file.close()
```

## Escritura de archivo

```python
new_file = open("ruta al archivo", "w")
new_file.write("hola mundo")
new_file.close()
```

## Siempre cerrar el archivo

```python
new_file = open("ruta al archivo", "w")
new_file.write("hola mundo")
new_file.close()
```

## Uso libreria Path para trabajo de rutas

```python
# Obtener ubicación actual
from pathlib import Path

CURRENT_PATH = Path(__file__)

print(CURRENT_PATH)

# Ir a la carpeta anterior

CURRENT_PATH.parent

# Unit una ruta/directorio/archivo

CURRENT_PATH.joinpath("carpeta")
CURRENT_PATH.joinpath("archivo.txt")
```

# Uso de Path para lectura de archivo

```python
from pathlib import Path
CURRENT_PATH = Path(__file__)

file = open(CURRENT_PATH.joinpath("archivo.txt"))

file.close()

```

---

[<< Inicio](./README.md) [< Volver](./terminal_read.md) || [siguiente >](./read_csv_file.md)
