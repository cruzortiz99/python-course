# 1. Cree una clase que pueda representar una carro en una aplicación para
# la gestión de un estacionamiento.

from functools import reduce
from datetime import datetime


class Car():
    def __init__(self, brand, name, location, time_in):
        self.brand = brand
        self.name = name
        self.location = location
        self.time_in = time_in


# 2. Cree una clase que pueda representar una mascota en una aplicación
# para la adopción de animales.

class Pet():
    def __init__(self, id, name, race, color, owner=None):
        self.id = id
        self.name = name
        self.race = race
        self.color = color
        self.owner = owner


# 3. Cree las clases que se requieran para representar los elementos y las
# relaciones para un sistema de venta de productos. El sistema debe
# representar los Clientes, Factura y Productos


class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price


class InvoiceProduct(Product):
    def __init__(self, product, quantity):
        Product.__init__(self, product.name, product.price)
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class Client():
    def __init__(self, name):
        self.name = name


class Invoice():
    def __init__(self, nro, date, client, products_invoice=[]):
        self.nro = nro
        self.date = date
        self.client = client
        self.__products__ = products_invoice

    def getProducts(self):
        return self.__products__

    def addProduct(self, product):
        self.__products__.append(product)

    def removeProduct(self, product):
        self.__products__ = list(
            filter(
                lambda invoice_product: invoice_product.name != product.name,
                self.__products__))

    def getTotalPrice(self):
        return reduce(lambda acc, product_price: acc + product_price,
                      list(map(
                          lambda product: product.total_price(),
                          self.__products__)),
                      0)

    def print(self):
        return f"""
      Nro: {self.nro}
      Client: {self.client.name}
      Date: {self.date}
      --------------------------
      Products:
      --------------------------{
        reduce(self.__getPrintableLines__, self.__products__, "")}
      --------------------------
      Total: {self.getTotalPrice()}
      --------------------------
      """

    def __getPrintableLines__(self, acc, product):
        return f"""{acc}
      {product.name}: {product.price} x {product.quantity} = {
        product.total_price()}"""


products = [
    Product("computadora", 50),
    Product("mouse", 2),
    Product("teclado", 3)
]

client = Client(name="Cruz")

client_invoice = Invoice(8569, date=datetime.now(), client=client)

client_invoice.addProduct(InvoiceProduct(products[0], 2))
client_invoice.addProduct(InvoiceProduct(products[1], 4))
client_invoice.addProduct(InvoiceProduct(products[2], 2))

print(client_invoice.print())


# 4. Cree a través del uso de clase o clases, una calculadora. Esta debe
# hacer las operaciones de suma, resta, multiplicación y división.
class CalculatorBuilder():
    def __init__(self):
        self.__first__ = None
        self.__second__ = None

    def set_first_value(self, first):
        self.__first__ = first
        return self

    def set_second_value(self, second):
        self.__second__ = second
        return CalculatorOperation(self.__first__, self.__second__)

    def get_result(self):
        return self.__first__

    def reset(self):
        self.__first__ = None
        self.__second__ = None
        return self


class CalculatorOperation():
    def __init__(self, first, second):
        self.__first__ = first
        self.__second__ = second

    def add(self):
        return CalculatorBuilder().set_first_value(
            self.__first__ + self.__second__)

    def substract(self):
        return CalculatorBuilder().set_first_value(
            self.__first__ - self.__second__)

    def multiply(self):
        return CalculatorBuilder().set_first_value(
            self.__first__ * self.__second__)

    def divide(self):
        if self.__second__ is None or self.__second__ == 0:
            return CalculatorBuilder().set_first_value(self.__first__)
        else:
            return CalculatorBuilder().set_first_value(
                self.__first__ / self.__second__)


calculator = CalculatorBuilder()
add_result = calculator.set_first_value(11).set_second_value(5).add()
substract_result = add_result.set_second_value(15).substract()
multiply_result = substract_result.set_second_value(7).multiply()
divide_result = multiply_result.set_second_value(2).divide()
print(f"""4. Calculated:
-> Suma 5 + 11: {add_result.get_result()}
-> Resta -15: {substract_result.get_result()}
-> Multiplicación x7: {multiply_result.get_result()}
-> División /2: {divide_result.get_result()}
""")


class Calculadora():
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def substract(self):
        return self.first - self.second

    def multiply(self):
        return self.first * self.second

    def divide(self):
        return self.first / self.second


calculadora = Calculadora(5, 10)
calculadora.add()
