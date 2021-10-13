# Recibir una tabla de datos de personas:
# 1- Imprimir los nombres y cedulas
# 2- Imprimir nombres de las personas adultas
# 3- Imprimir nombres de los adolescentes del grupo
# 4- Calcular la sumatoria de las edades del grupo

from functools import reduce


class Person():
    def __init__(self, name, last_name, age, id):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.id = id


persons = [
    Person("Cruz", "Ortiz", 29, 2053481182),
    Person("German", "Montero", 62, 561231231),
    Person("John", "Smith", 14, 84321351),
    Person("Maria", "Alcalá", 15, 545121231)
]


def forEach(function, items):
    for item in items:
        function(item)


print("1.-")

# for person in persons:
#     print(person.name, person.id)


def printNameAndIdOfPerson(person):
    print(person.name, person.id)

# forEach(lambda person: print(person.name, person.id), persons)


forEach(printNameAndIdOfPerson, persons)

print("2.-")


def byAgeHigherThan18(person):
    return person.age > 18


def printPersonName(person):
    print(person.name)


forEach(printPersonName, list(filter(byAgeHigherThan18, persons)))

print("3.-")


def byAgeLowerThan18AndHigherThan12(person):
    return person.age <= 18 and person.age >= 12


forEach(
    printPersonName,
    list(
        filter(
            byAgeLowerThan18AndHigherThan12,
            persons)))

print("4.-")

# sumatoria = 0
# for person in persons:
#     sumatoria += person.age


def sumPersonAge(acc, person):
    if isinstance(acc, int):
        return acc + person.age
    else:
        return acc.age + person.age


sumatoria = reduce(sumPersonAge, persons)
print(sumatoria)
