<img src="../assets/img/python-logo.png" />

[<< Inicio](./README.md) [< Volver](./README.md) || [siguiente >](./import_modules.md)

---

## ¿Qué es?

```python
# Some file .py
def greeting():
  return print("Hello World!")

# Main file .py

import #package

greeting()
```

## Crear un módulo en python

```python
# Package file .py
def some_function():
  pass

class SomeClass(): pass

some_variable = 58
```

## Evitar que el módulo sea ejecutable

```python
# Codigo del paquete
def some_function: pass
# ...
if __name__ == '__main__':
# Codigo a ejecutar
  some_function()
```

---

[<< Inicio](./README.md) [< Volver](./README.md) || [siguiente >](./import_modules.md)
