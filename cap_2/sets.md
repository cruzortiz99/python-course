<img src="../assets/img/python-logo.png" />

[< Volver](./data_types.md)

---

## Longitud

```python
some_set = {1,2,3,3}
print(len(some_set))

# output: 3
```

## Acceder a elementos

```python
some_set = {1,2,3,3}
print(some_set[1])

# output: 2
```

## Añadir elementos

```python
some_set = {1,2,3,3}
some_set.add(4)

print(some_set)

# output: {1,2,3,4}

other_set = {5,6,6}
some_set.update(other_set)
print(some_set)

# output: {1,2,3,4,5,6}
```

## Lista fija de datos

```python
some_set = {1,2,3,3}
some_set[0] = 0

print(some_set)

# output:
# Traceback (most recent call last):
# File "path/to/file", line 2, in <module>
#    some_set[0] = 0
#TypeError: 'set' object does not support item assignment

some_set = {1,2,3,3}
some_set = list(some_set)
some_set[0] = 0
some_set = set(some_set)

print(some_set)

# output: {0,2,3}
```

---

[< Volver](./data_types.md)
