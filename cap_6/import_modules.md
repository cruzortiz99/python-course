<img src="../assets/img/python-logo.png" />

[<< Inicio](./README.md) [< Volver](./python_modules.md) || [FIN >](./README.md)

---

## Importar un módulo en python

```python
# import # nombre o ubicación del módulo
import functools


functools.reduce(lambda acc, x: x, range(15))
```

## Importar una funcionalidad particular del módulo

```python
# from <nombre_o_ubicación_del_modulo> import <funcionalidades>
from functools import reduce


reduce(lambda acc, x: x, range(15))
```

## Renombrar el módulo cuando se importa

```python
import functools as ft

ft.reduce(lambda acc,x:x, range(15))

# Renombrar funcionalidades

from functools import reduce as rd

rd(lambda acc, x: x, range(15))
```

---

[<< Inicio](./README.md) [< Volver](./python_modules.md) || [FIN >](./README.md)
