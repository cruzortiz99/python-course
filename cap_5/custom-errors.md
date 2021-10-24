<img src="../assets/img/python-logo.png" />

[<< Inicio](./README.md) [< Volver](./raise-error.md) || [FIN >](./README.md)

---

## Extender desde Exception

```python
class CustomError(Exception):
  def __init__(self, message="")
    Exception.__init__(self, message)

def add(num1, num2):
  if not type(num1) is int:
    raise CustomError("num1 must be int")
  if not type(num2) is int:
    raise CustomError("num2 must be int")
  return num1 + num2
```

---

[<< Inicio](./README.md) [< Volver](./raise-error.md) || [FIN >](./README.md)
