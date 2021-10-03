<img src="../assets/img/python-logo.png" />

[<< Inicio](./README.md) [< Volver](./control_flows.md) || [Fin](./README.md)

---

## Ciclo for

```python
# Para rangos
for number in range(9):
  print(number)

# Rangos a pasos
for number in range(0, 9 , 3):
  print(number)

# Rango inverso
for number in range(0,-9,-3):
  print(number)

# Para texto
for letter in "texto":
  print(letter)

# Para Listas
some_list = [1, 1.2, "texto", {"a": 1, "b": 3}]
for item in some_list:
  print(item)

# Para diccionarios
some_dict = {"a": 1, "b": 3}
for key in some_dict:
  print(key)

# Conociendo el indice
some_list = [1, 1.2, "texto", {"a": 1, "b": 3}]
for index, key in enumerate(some_list):
    print(index, key)
```

## Ciclo while

```python
# Ciclos con limites no determinados
a = 0
while(a < 10):
    print(a)
    a = a + 1
```

---

[<< Inicio](./README.md) [< Volver](./control_flows.md) || [Fin](./README.md)
