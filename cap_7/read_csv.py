from pathlib import Path

CURRENT_PATH = Path(__file__)

ARCHIVO_CSV_PATH = CURRENT_PATH.parent.parent.joinpath(
    "project").joinpath("assets").joinpath("test.csv")


class Person():
    def __init__(self, name, last_name, age, ci, work):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.ci = ci
        self.work = work


# Imprimir un enter
print("\n")
file_csv = open(ARCHIVO_CSV_PATH, "r", encoding="utf8")
lines_in_file = file_csv.readlines()
file_csv.close()


def from_line_to_person(line):
    values = line.split(',')
    return Person(values[0], values[1], int(values[2]), values[3], values[4])


persons = list(map(from_line_to_person, lines_in_file[1:]))

print("Personas inscritas", len(persons))
print("Personas mayores 30:", len(
    list(filter(lambda person: person.age >= 30, persons))))
