<img src="../assets/img/python-logo.png" />

[<< Inicio](./README.md) [< Volver](./catch-error.md) || [Siguiente >](./custom-errors.md)

---

## Usando raise

```python
def add(num1, num2):
  if not type(num1) is int:
    raise Exception()
  if not type(num2) is int:
    raise Exception()
  return num1 + num2
```

## Lanzar Exception con mensaje

````python
def add(num1, num2):
  if not type(num1) is int:
    raise Exception("num1 must be int")
  if not type(num2) is int:
    raise Exception("num2 must be int")
  return num1 + num2
```

---

[<< Inicio](./README.md) [< Volver](./catch-error.md) || [Siguiente >](./custom-errors.md)
````
