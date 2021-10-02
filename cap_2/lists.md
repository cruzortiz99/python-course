<img src="../assets/img/python-logo.png" />

[< Volver](./data_types.md)

---

## Longitud de una lista

```python
print(len([1, 3, 5]))

# output: 3
```

## Acceder a elementos

```python
print([1, 3, 5][1])

# output: 3
```

## Cambiar valor en una posición

```python
some_list = [1, 2, 3]
some_list[1] = 0
print(some_list)

#output: [1,0,3]
```

## Insertar elementos a la lista

```python
some_list = [1, 2, 3]
some_list.insert(1, 4)
print(some_list)

# output: [1, 4, 2, 3]

some_list.append(5)
print(some_list)

# output: [1, 4, 2, 3 , 5]

some_list.extend([5,6,7])
print(some_list)

# output: [1, 4, 2, 3, 5, 5, 6, 7]
```

# Remover un elemento

```python
some_list = [1,2,3,4]
some_list.remove(3)
print(some_list)

# output: [1, 2, 4]

some_list.pop(1)
print(some_list)

# output: [1, 4]

some_list.clear()
print(some_list)

# output: []
```

# Ordenamiento

```python
some_list = [1, 5, 9, 7, 6, 3, 2, 4, 8, 6]

some_list.sort()
print(some_list)

# output: [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]

some_list.sort(reverse=True)
print(some_list)

# output: [9, 8, 7, 6, 6, 5, 4, 3, 2, 1]

def close_to_3(number):
    return abs(number - 3)


some_list.sort(key=close_to_3)
print(some_list)

# output: [3, 4, 2, 5, 1, 6, 6, 7, 8, 9]

some_list.reverse()
print(some_list)

# output: [9, 8, 7, 6, 6, 1, 5, 2, 4, 3]

```

---

[< Volver](./data_types.md)
