<img src="../assets/img/python-logo.png" />

[<< Inicio](./README.md) [< Volver](./classes.md) || [Siguiente >](./inheritance.md)

---

## Acciones o métodos de una clase

```python
class Pet():
    def __init__(self, name):
        self.name = name
        self.__hungry__ = True
        self.__falling_asleep__ = False
        self.__boring__ = True
        self.__mood__ = "angry"

    def eat(self):
        self.__hungry__ = False
        self.__falling_asleep__ = True

    def sleep(self):
        self.__falling_asleep__ = False
        self.__boring__ = True

    def play(self):
        self.__boring__ = False
        self.__hungry__ = True

    def mood(self):
        if (self.__hungry__ or self.__boring__):
            return "enojado"
        else:
            return "feliz"


dog = Pet("Tomy")
print("El perro esta: ", dog.mood())
dog.eat()
print("El perro esta: ", dog.mood())
dog.sleep()
print("El perro esta: ", dog.mood())
dog.play()
print("El perro esta: ", dog.mood())
dog.eat()
print("El perro esta: ", dog.mood())

# output:
# El perro esta:  enojado
# El perro esta:  enojado
# El perro esta:  enojado
# El perro esta:  enojado
# El perro esta:  feliz
```

## Diferencias con una funcion

```python
# function
def play():
  # ...
  return # value

play(# value)

# method
class ThingThatCanPlay():
  def __init__():
    pass
  def play(self):
    # ...
    return # value

can_play = ThingThatCanPlay()
can_play.play()
```

## Accesibilidad

```python
# No existe métodos privados
class Pet():
    def __init__(self, name):
        self.name = name
        self.__hungry__ = True
        self.__falling_asleep__ = False
        self.__boring__ = True
        self.__mood__ = "angry"

    def eat(self):
        self.__hungry__ = False
        self.__falling_asleep__ = True

    def sleep(self):
        self.__falling_asleep__ = False
        self.__boring__ = True

    def play(self):
        self.__boring__ = False
        self.__hungry__ = True

    def mood(self):
        if (self.__hungry__ or self.__boring__):
            return "enojado"
        else:
            return "feliz"

# Por convención
class Pet():
    def __init__(self, name):
        self.name = name
        self.__hungry__ = True
        self.__falling_asleep__ = False
        self.__boring__ = True
        self.__mood__ = "angry"

    def eat(self):
        self.__hungry__ = False
        self.__falling_asleep__ = True

    def sleep(self):
        self.__falling_asleep__ = False
        self.__boring__ = True

    def play(self):
        self.__boring__ = False
        self.__hungry__ = True

    def mood(self):
        if (self.__hungry__ or self.__boring__):
            return "enojado"
        else:
            return "feliz"
    def __go_to_bathroom__():
      pass

dog = Pet()
# Todavia es accesible
dog.__go_to_bathroom__()
```

---

[<< Inicio](./README.md) [< Volver](./classes.md) || [Siguiente >](./inheritance.md)
