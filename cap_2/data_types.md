<img src="../assets/img/python-logo.png" />

[<< Inicio](./intro) [< Volver](./variables.md) || [Siguiente >](./log_operators.md)

---

## Números

### Enteros

```python
print(type(4))

# output: <class 'int'>

print(type(int(42.5)))

# output: <class 'int'>
```

### Flotantes

```python
print(type(4.5))

# output: <class 'float'>

print(type(float(42)))

# output: <class 'float'>
```

### Complejos

```python
print(type(45+96J))

# output: <class 'complex'>

print(type(complex(42)))

# output: <class 'complex'>
```

## [Texto](./strings.md)

```python
print(type("texto"))

# output: <class 'str'>

print(type(str(4.5)))

# output: <class 'str'>
```

## Booleanos

```python
print(type(False))

# output: <class 'bool'>
```

## [Listas](./lists.md)

```python
print(type([1, 2, 3, 4, 5]))

# output: <class 'list'>'

print(type(list("a", "b", "d", "e")))

# output: <class 'list'>'
```

## [Listas Estáticas (Tuplas)](./tuples.md)

```python
print(type((4, 4.5, "texto")))

# output: <class 'tuple'>
print(type(tuple([4, 4.5, "texto"])))

# output: <class 'tuple'>
```

## [Conjuntos o Listas de elementos únicos (Sets)](./sets.md)

```python
print(type({1, 2, 3, 3}))

# output: <class 'set'>

print(type(set([1, 2, 3, 3])))

# output: <class 'set'>
```

## [Diccionarios](./dictionaries.md)

```python
print(type({"a": 1, "b": "texto", "c": []}))

# output: <class 'dict'>
```

## Tipos Personalizados

```python
class OwnType():
    def __init__(self):
        pass


print(type(OwnType()))

# <class '__main__.OwnType'>
```

---

[<< Inicio](./intro) [< Volver](./variables.md) || [Siguiente >](./log_operators.md)
