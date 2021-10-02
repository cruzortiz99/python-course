<img src="../assets/img/python-logo.png" />

[< Volver](./data_types.md)

---

## Acceder a la información

```python
some_tuple = ("primero", 2, 2.5)
print(some_tuple[1])

# output: 2
```

## Longitud

```python
some_tuple = ("primero", 2, 2.5)
print(len(some_tuple))

# output: 3
```

## Lista fija e inmutable

```python
some_tuple = ("primero", 2, 2.5)
some_tuple[1] = ["texto"]

print(some_tuple)

# output:
# Traceback (most recent call last):
#  File <path/to/file>, line 2, in <module>
#    some_tuple[1] = ["texto"]
#TypeError: 'tuple' object does not support item assignment

some_tuple = ("primero", 2, 2.5)
some_tuple[1] = 4

print(some_tuple)

# output:
# Traceback (most recent call last):
#  File "path/to/file", line 2, in <module>
#    some_tuple[1] = 4
# TypeError: 'tuple' object does not support item assignment

some_tuple = ("primero", 2, 2.5)
some_tuple = list(some_tuple)
some_tuple[1] = 4
some_tuple = tuple(some_tuple)

print(some_tuple)

# output: ('primero', 4, 2.5)
```

---

[< Volver](./data_types.md)
