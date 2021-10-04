<img src="../assets/img/python-logo.png" />

[<< Inicio](./README.md) [< Volver](./data_types.md) || [Siguiente >](./mat_operators.md)

---

## and

| A     | B     | AND   |
| ----- | ----- | ----- |
| False | False | False |
| False | True  | False |
| True  | False | False |
| True  | True  | True  |

```python
a = 15 < 18
b = 75 > 10
print(a and b)

# output: True
```

## or

| A     | B     | OR    |
| ----- | ----- | ----- |
| False | False | False |
| False | True  | True  |
| True  | False | True  |
| True  | True  | True  |

```python
a = 15 > 18
b = 75 > 10
print(a or b)

# output: True
```

## not

| A     | OR    |
| ----- | ----- |
| False | True  |
| True  | False |

```python
a = 15 > 18
print(not a )

# output: True
```

## is

```python
x = "texto"
y = str(x)
print(x is y)

# output: True
```

## is not

```python
x = "texto"
y = str(x)
print(x is not y)

# output: False
```

## in

```python
x = "texto"
print("ext" in x)

# output: True
```

## not in

```python
x = "texto"
print("ext" not in x)

# output: False
```

### Otros: & (AND), | (OR), ^ (XOR), ~ (NOT)

---

[<< Inicio](./README.md) [< Volver](./data_types.md) || [Siguiente >](./mat_operators.md)
