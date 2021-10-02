<img src="../assets/img/python-logo.png" />

[<< Inicio](./intro) [< Volver](./lambdas.md) || [Fin](./intro.md)

---

## Map

```python
some_list = [1, 2, 3, 4]
mapped_list = list(map(lambda x: str(x**x), some_list))
print(some_list, mapped_list)

# output: [1, 2, 3, 4] ['1', '4', '27', '256']
```

## Filter

```python
some_list = [1, 2, 3, 4]
filtered_list = list(filter(lambda x: len(str(x**x)) > 1, some_list))
print(some_list, filtered_list)

# output: [1, 2, 3, 4] [3, 4]
```

## Reduce

```python
from functools import reduce

some_list = [1, 2, 3, 4]
reduced_list = reduce(lambda acc, current: acc + current, some_list)
print(some_list, reduced_list)

# output: [1, 2, 3, 4] 10
```

---

[<< Inicio](./intro) [< Volver](./lambdas.md) || [Fin](./intro.md)
