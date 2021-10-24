# from functools import reduce
# # Fibonacci
# lista = range(15)


# def reductor_func(acc, _):
#     return acc + [acc[-1] + acc[-2]]


# reduce(reductor_func, lista, [0, 1])

# # i | acc | return
# # 0 | [0,1] | [0,1]+[1+0] = [0,1,1]
# # 1 | [0,1,1]| [0,1,1]+[1+1] = [0,1,1,2]
# # 2 | [0,1,1,2]| [0,1,1,2] + [2+1] = [0,1,1,2,3]
# students = {"Pepito Perez": (7.2, 120)}


# def filter_func(x):
#     return (x[1][0], x[1][1]) > (6.0, 70)


# result = dict(filter(filter_func, students.items()))

# # student.items() -> [("Pepito Perez", (7.2,120))]
# # filter_func : x[1] -> (7.2, 120); (x[1][0] -> 7.2, x[1][1] -> 120)

class AddTypeErrorException(Exception):
    def __init__(
            self,
            message="El tipo de dato no es correcto al usar la función add"):
        Exception.__init__(self, message)


def add(num1, num2):
    if (not isinstance(num1, int) and not isinstance(num1, float)):
        raise AddTypeErrorException()
    if (not isinstance(num2, int) and not isinstance(num2, float)):
        raise AddTypeErrorException()
    return num1 + num2

# print(add([1.5, 78], [45, 78]))


for num in range(10000):
    try:
        print(add("2", num))
    except AddTypeErrorException:
        print("Error en tipos de datos")
