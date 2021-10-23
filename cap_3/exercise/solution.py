# 1. Crear una función encargada de sumar dos números
from functools import reduce


def add(first, second):
    return first + second


# 2. Crear una función encargada de sumar n números enteros
def add(*nums):
    result = 0
    for num in nums:
        result = result + num
    return result

# 3. Crear una función que devuelva un valor cuando una condición se cumpla y
# otro valor cuando la condición no se cumpla. Ejemplo:

# ifOrElse(whenIsTrue, whenIsFalse, condition)
# ifOrElse("hola", "chao", True) -> "hola"
# ifOrElse("hola", "chao", False) -> "chao"


def ifOrElse(whenSuccess, whenFails, condition):
    if condition:
        return whenSuccess
    else:
        return whenFails


# 4. Crear una función encargada de retornar un valor cuando el retorno de
# una función es cierta y otro valor cuando el retorno de una función es
# falsa. Ejemplo:

# ifOrElse("hola", "chao", lambda: True) -> "hola"
# ifOrElse("hola", "chao", lambda: False) -> "chao"
def ifOrElse(whenSuccess, whenFails, condition):
    if condition():
        return whenSuccess
    else:
        return whenFails


# 5. Crear una función encargada de ejecutar una función cuando el retorno
# de una función es cierta y ejecuta otra cuando el retorno de una función
# es falsa. Ejemplo:

# ifOrElse(lambda: "hola", lambda: "chao", lambda: True) -> "hola"
# ifOrElse(lambda: "hola", lambda: "chao", lambda: False) -> "chao"
def ifOrElse(whenSuccess, whenFails, condition):
    if condition():
        return whenSuccess()
    else:
        return whenFails()


# if 15 > 16:
#     do_some_work()
# else:
#     do_nothing()

# ifOrElse(do_some_work, do_nothing, slow_condition)


# 6. Hacer de las funciones anteriores, de ejecución perezosa o funciones
# de orden superior.
def addLazy(*nums): return lambda: add(nums)


def ifOrElseLazy(whenSuccess, whenFails, condition):
    def container():
        if condition():
            return whenSuccess()
        else:
            return whenFails()
    return container

# lazy_result = ifOrElseLazy(do_some_work, do_nothing, slow_condition)

# ifOrElse(do_some_work,do_nothing,slow_condition)

# ...


# lazy_result()

# 7.Dado:
# list = [
#  {
#    "name": "Cruz",
#    "last_name": "Ortiz",
#    "age": 29,
#    "friends": [],
#    "car": {"name": "Logan", "type": "sedan"}},
#  {
#    "name": "German",
#    "last_name": "Montero",
#    "age": 63,
#    "friends": [{
#      "name": "Cruz",
#      "last_name": "Ortiz",
#      "age": 29}],
#    "car": {"name": "Mustang", "type": "deportivo"}},
#  {
#    "name": "Martin",
#    "last_name": "Palermo",
#    "age": 42,
#    "friends": [],
#    "car": {"name": "Cherokee", "type": "camioneta"}},
#  {
#    "name": "John",
#    "last_name": "English",
#    "age": 72,
#    "friends": [],
#    "car": {"name": "Aveo", "type": "sedan"}},
#  {
#    "name": "Indiana",
#    "last_name": "Jones",
#    "age": 55,
#    "friends": [],
#    "car": {"name": "Mustang", "type": "deportivo"}},
#  {
#    "name": "Luke",
#    "last_name": "Skywalker",
#    "age": 56,
#    "friends": [{
#      "name": "Cruz",
#      "last_name": "Ortiz",
#      "age": 29,
#    },{
#      "name": "German",
#      "last_name": "Montero",
#      "age": 63,
#    }],
#    "car": {"name": "Cherokee", "type": "camioneta"}}
# ]
# 7.1. Contar la cantidad de persona en la lista.
#
# 7.2. Contar la cantidad de personas que poseen amigos.
#
# 7.3. Contar la cantidad de personas que poseen el mismo tipo de carro.
#
# 7.4. Mostrar una lista de los carros que se poseen
#
# 7.5. Convierta los diccionarios en la lista en un tipo personalizado
#
# persons = [
#  {
#    "name": "Cruz",
#    "last_name": "Ortiz",
#    "age": 29,
#    "friends": [],
#    "car": {"name": "Logan", "type": "sedan"}},
#  {
#    "name": "German",
#    "last_name": "Montero",
#    "age": 63,
#    "friends": [{
#      "name": "Cruz",
#      "last_name": "Ortiz",
#      "age": 29}],
#    "car": {"name": "Mustang", "type": "deportivo"}},
#  {
#    "name": "Martin",
#    "last_name": "Palermo",
#    "age": 42,
#    "friends": [],
#    "car": {"name": "Cherokee", "type": "camioneta"}},
#  {
#    "name": "John",
#    "last_name": "English",
#    "age": 72,
#    "friends": [],
#    "car": {"name": "Aveo", "type": "sedan"}},
#  {
#    "name": "Indiana",
#    "last_name": "Jones",
#    "age": 55,
#    "friends": [],
#    "car": {"name": "Mustang", "type": "deportivo"}},
#  {
#    "name": "Luke",
#    "last_name": "Skywalker",
#    "age": 56,
#    "friends": [{
#      "name": "Cruz",
#      "last_name": "Ortiz",
#      "age": 29,
#    },{
#      "name": "German",
#      "last_name": "Montero",
#      "age": 63,
#    }],
#    "car": {"name": "Cherokee", "type": "camioneta"}}
# ]

persons = [
    {
        "name": "Cruz",
        "last_name": "Ortiz",
        "age": 29,
        "friends": [],
        "car": {"name": "Logan", "type": "sedan"}},
    {
        "name": "German",
        "last_name": "Montero",
        "age": 63,
        "friends": [{
            "name": "Cruz",
            "last_name": "Ortiz",
            "age": 29}],
        "car": {"name": "Mustang", "type": "deportivo"}},
    {
        "name": "Martin",
        "last_name": "Palermo",
        "age": 42,
        "friends": [],
        "car": {"name": "Cherokee", "type": "camioneta"}},
    {
        "name": "John",
        "last_name": "English",
        "age": 72,
        "friends": [],
        "car": {"name": "Aveo", "type": "sedan"}},
    {
        "name": "Indiana",
        "last_name": "Jones",
        "age": 55,
        "friends": [],
        "car": {"name": "Mustang", "type": "deportivo"}},
    {
        "name": "Luke",
        "last_name": "Skywalker",
        "age": 56,
        "friends": [{
            "name": "Cruz",
            "last_name": "Ortiz",
            "age": 29,
        }, {
            "name": "German",
            "last_name": "Montero",
            "age": 63,
        }],
        "car": {"name": "Cherokee", "type": "camioneta"}}
]
# 7.1
print(f"7.1 Cantidad de personas: {len(persons)}")


# 7.2
def if_has_friend(person):
    return len(person["friends"]) > 0


person_with_friends = len(
    list(filter(if_has_friend, persons)))

print(f"7.2 Cantidad de personas con amigos: {person_with_friends}")


# 7.3

def groupByCar(groups, person_dict):
    car_name = person_dict["car"]["name"]
    if car_name in groups:
        groups[car_name] = groups[car_name] + [person_dict]
    else:
        groups[car_name] = [person_dict]
    return groups


def totalizeGroups(persons_group_by_car):
    totalize = {}
    for car_name in persons_group_by_car:
        totalize[car_name] = len(
            persons_group_by_car[car_name])
    return totalize


print(f"""7.3 Cantidad de personas agrupadas por carro: {
      totalizeGroups(reduce(groupByCar, persons, {}))}""")
# [{...}, {...}]
# {"Logan": [{...}], "Mustang": [{...}]}
# {"Logan": 85, "Mustang": 8}
# 7.4


def dischardIfExists(acc, current_car):
    filtered_car_name = list(map(lambda car: car["name"], acc))
    if current_car["name"] in filtered_car_name:
        return acc
    else:
        return acc + [current_car]


cars = reduce(dischardIfExists, list(
    map(lambda person: person["car"], persons)), [])


print(f"7.4 Carros que se poseen: {list(map(lambda car: car['name'], cars))}")


# 7.5
class Person:
    def __init__(self, name, last_name, age, car=None, friends=[]):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.car = car
        self.friends = friends


class Car:
    def __init__(self, name, type):
        self.name = name
        self.type = type


def dictToPersons(person_dict):
    return Person(
        name=person_dict["name"],
        last_name=person_dict["last_name"],
        age=person_dict["age"],
        car=Car(
            name=person_dict["car"]["name"],
            type=person_dict["car"]["type"]),
        friends=list(map(
            lambda friend: Person(
                name=friend["name"],
                last_name=friend["last_name"],
                age=friend["age"]
            ),
            person_dict["friends"])))


persons_in_class = list(map(dictToPersons, persons))

print("7.5 Personas con clases: ", list(
    map(lambda person: person.name, persons_in_class)))
