<img src="../assets/img/python-logo.png" />

[<< Inicio](./intro) [< Volver](./intro.md) || [Siguiente >](./basic_functions.md)

---

## Crear una función

```python
def greeting():
  print("Hello :)")
```

## Ejecutar una función

```python
greeting()
```

## Dar información a la función

```python
# Dar información vía parámetros
def greeting(name):
  print(f"Hola, {name}")

greeting("Jose")

# Multiples parámetros
def add(num1, num2):
  print(num1 + num2)

add(2,5)

# Numero indefinido de parámetros
def multiply(*nums):
  result = 1
  for number in nums:
      result *= number
  print(result)


multiply(2, 4, 5, 2)

# Parámetros indefinidos con nombre
def greeting(**person):
    print("Hola, {} {}".format(person["name"], person["last_name"]))


greeting(name="Jose", last_name="John")

# Valores por defecto
def increment(start, to, step=3):
    for number in range(start, to, step):
        print(number)


increment(0, 9)
```

## Obtener datos de una función

```python
def add(*nums):
  result = 0
  for number in nums:
    result += number
  return result

print(add(1,2,3,10,859))
```

## Re-usar secciones de código

```python
print(add(1,2,3,10,859))
print(add(1,2,3))
print(add(9,6,3))
```

## Recursividad

```python
def for_loop(list, index=0):
  if (index < len(list) - 1):
    print(list[index])
    return for_loop(list, index + 1)
  else:
    print(list[index])
    return list[index]

for_loop([1, 2, 3])
```

## Ejecución agresiva y perezosa (Eager and lazy evaluation)

```python
def eagerAdd(num1, num2):
    return num1 + num2


print(eagerAdd(2, 10))


def lazyAdd(num1):
    def innerAdd(num2):
        return num1 + num2
    return innerAdd


print(lazyAdd(2)(3))
add10 = lazyAdd(10)
print(add10(1000))

# Usando lambdas
def lazyAddLambda(num1):
    return lambda num2: num1 + num2


print(lazyAddLambda(1000)(10))
```

---

[<< Inicio](./intro) [< Volver](./intros.md) || [Siguiente >](./basic_functions.md)
