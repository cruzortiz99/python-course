import math
"""
1. Crear una lista usando la función constructora `list(...)`.
   Imprimir en consola la lista """

# Usando la función constructora sería MyList = list(1,5,3,28,9)
MyList = [1, 5, 3, 28, 9]
print("Tarea 1.1.")
print(MyList)
print("\n")


"""
Tarea 1.2.
2.	Crear una lista e imprimir en consola el tamaño de la lista. """

MyList = [1, 5, 3, 28, 9]
print("Tarea 1.2")
print(len(MyList))
print("\n")

"""
Tarea 1.3.
3.	Crear una lista desordena y utilice el método sort para ordenarlo. """

MyList = sorted([1, 5, 3, 28, 9])  # Usando el método sort seria MyList.sort()
print("Tarea 1.3")
print(MyList)
print("\n")

"""
Tarea 1.4.
4.	Crear una lista desordenada, creer una función de ordenamiento y ordene
 la lista usando la función. """

# La idea de esta tarea es ordenar una lista de forma personalizada
MyList = [1, 5, 3, 28, 9]


def Ordenar():
    MyList.sort()


print("Tarea 1.4")
Ordenar()
print(MyList)
print("\n")

""" Tarea 1.5.
5. Crear una lista desordenada y ordene de forma inversa """

MyList = [1, 5, 3, 28, 9]
MyList.sort(reverse=True)
print("Tarea 1.5")
print(MyList)
print("\n")

""" Tarea 2. (NUMEROS)

Tarea 2.1.

1.	Crear una variable que contenga un numero entero.
    Imprimir en consola el número y el tipo de dato. """

MyVar = 4
print("Tarea 2.1")
print(MyVar, type(MyVar), "\n")

"""
2. Crear una variable que contenga la operación de la multiplicación
   de dos números enteros. Ej: suma = 15*1235.
   Imprima en consola el resultado y el tipo de datos. """

MyProd = 458 * 6
print("Tarea 2.2")
print(MyProd, type(MyProd))
print("\n")

"""
3. Crear una variable que contenga la operación de división de dos números enteros.
   Ej: división = 10/2.
   Imprima en consola el resultado y el tipo de datos. """

MyDiv = int(878 / 2)
print("Tarea 2.3")
print(MyDiv, type(MyDiv))
print("\n")

# Nota: Si a MyDiv no le coloco "int", el resultado de la división de dos enteros,
#       resulta en un número tipo "float"... ¿?

"""
4. Crear un entero usando la función creadora `int(...)` a partir de un numero decimal. Imprimir en consola
   el número y el tipo de datos """


MyInt = int(math.pi)
print("Tarea 2.4")
print(MyInt, type(MyInt))
print("\n")

# Nota:
# Encontré en internet la forma de usar el número pi. Es a través de "import", me hablaste
# algo de esto, pero no lo recuerdo. El sábado me refrescas esto, por favor.


"""
5. Crear un entero usando la función creadora `int(...)` a partir de un texto.
   Imprimir en consola el número y el tipo de datos. """

MyInt = int("45")
print("Tarea 2.5")
print(MyInt, type(MyInt), "\n")

"""
6. Crear un `float` usando la función creadora `float(...)` a partir de un número entero.
   Imprimir en consola el número y el tipo de datos.   """

MyFloat = float(29)
print("Tarea 2.6")
print(MyFloat, type(MyFloat), "\n")


"""
7. Crear un `float`usando la función creadora `float(...)` a partir de un texto.
   Imprimir en consola el número y el tipo de datos. """

MyFloat = float("3.23")
print("Tarea 2.7")
print(MyFloat, type(MyFloat), "\n")


""" 3. (STRINGS)

1. Crear un texto usando la función constructora `str(...)`.
   Imprimir en consola el texto y el tipo de datos. """

MyText = str(2021)
print("Tarea 3.1")
print("Año: ", MyText)
print(MyText, type(MyText), "\n")

"""
2. Crear un texto de multiples líneas e imprimir en consola."""

MyText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n"
MyText2 = "Integer non elit elit. Donec viverra nisi facilisis tellus fringilla ultrices.\n"
MyText3 = MyText + MyText2 + \
    "Ut porttitor ac lorem faucibus rhoncus. Aenean vel velit ex.\n"
print("Tarea 3.2.")
print(MyText3)

# Otra forma: usando triple dobles comillas.

MyText = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Integer non elit elit. Donec viverra nisi facilisis tellus fringilla ultrices.
Ut porttitor ac lorem faucibus rhoncus. Aenean vel velit ex."""

print("Tarea 3.2.b.")
print(MyText, "\n")

"""3. Crear un texto e imprimir en consola su longitud."""

MyText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
print("Tarea 3.3.")
print(len(MyText), "\n")

"""
4. Crear un texto e imprimir en consola la primera y ultima letra en consola."""

MyText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
print("Tarea 3.4.")
print(MyText[0], MyText[-1], "\n")

"""
5. Crear un texto e imprimir una sección del texto que inicie con el texto
    hasta la mitad del mismo."""

MyText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
print("Tarea 3.")
print(MyText[0:int((len(MyText)) / 2)], "\n")

"""
6. Crear un texto e imprimir una sección del texto que
   inicie en la mitad del texto hasta el final."""

MyText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
print("Tarea 3.6")
print(MyText[int((len(MyText)) / 2):], "\n")

"""
7. Crear un texto de multiples palabras.
   Imprimir el texto en mayúsculas."""

MyText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
print("Tarea 3.7.")
print(MyText.upper(), "\n")

"""
8. Crear un texto de multiples palabras.
   Imprimir el texto en minúsculas."""

MyText = "LOREM IPSUM DOLOR SIT AMET, CONSECTETUR ADIPISCING ELIT"
print("Tarea 3.8.")
print(MyText.lower(), "\n")

"""
9. Crear un texto de multiples palabras.
   Remplazar la ultima palabra por otra e imprimir ambos textos"""

# Debería usarse el método replace. MyText.replace(...)

MyText = ["manzana", "mango", "patilla", "cambur"]
print("Tarea 3.9")
print(MyText)
MyText2 = MyText[0:len(MyText) - 1]
MyText2.append("mango")
print(MyText2, "\n")

# ¿Cómo hacer para que al imprimir una lista no aparezcan los corchetes?

"""10.
Crear un texto de multiples palabras. Dividir el texto entre cada palabra.
   Ej: text = "Hola mundo"
       # output: ["Hola", "mundo"] """

MyText = "Germán Montero Alcalá"
print("Tarea 3.10")
MyText2 = MyText.split()
print(MyText2, "\n")

"""
11. Crear un texto plantilla y usa el método format para incluir
    texto dentro de la plantilla. """

# No recuerdo qué es un "texto plantilla", hice el ejercicio con lo que encontré
# en internet.

print("Tarea 3.11")
MyText = "Nombre: {nombre}"
print(MyText.format(nombre="Germán"), "\n")

"""
12. Crear un texto plantilla con 3 espacios disponibles. Usa el método format para incluir
    textos dentro de la plantilla. """

MyText = "Fruta 1: {}, Fruta 2: {}, Fruta 3: {}"
print("Tarea 3.12.")
print(MyText.format("Mango", "Uva", "Níspero"), "\n")

"""
13. Crear un texto y contar la cantidad de veces que se repite una letra."""

# No me acuerdo cuál fue el método del curso,
# busqué en internet "Character counting in Python".

print("Tarea 3.13")
MyText = "Maracaibo, la tierra del sol amada"
print(MyText)
MyLetter = "a"
print("Cantidad de:", '"', MyLetter, '":', MyText.count(MyLetter), "\n")
