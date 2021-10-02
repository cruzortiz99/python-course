<img src="../assets/img/python-logo.png" />

[<< Inicio](./intro) [< Volver](./basic_functions.md) || [Siguiente >](./fp.md)

---

## Definir Lambda

```python
filtered_list = list(filter(lambda x: x > 5, range(10)))

print(filtered_list)

transformed_list = list(map(lambda x: x**2, range(10)))

print(transformed_list)

```

## Definir una función para recibir una función

```python
def forEach(func, list):
    for index, value in enumerate(list):
        func(index, value)


forEach(lambda index, value: print(index, value), [1, 1.2, 3, 85])
```

---

[<< Inicio](./intro) [< Volver](./basic_functions.md) || [Siguiente >](./fp.md)
