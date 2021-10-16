# 1. Cree una clase que pueda representar una carro en una aplicación para
# la gestión de un estacionamiento.

from functools import reduce
from datetime import datetime


class Car():
    def __init__(self, branch, name, location, time_in):
        self.branch = branch
        self.name = name
        self.location = location
        self.time_in = time_in


# 2. Cree una clase que pueda representar una mascota en una aplicación
# para la adopción de animales.

class Pet():
    def __init__(self, name, race, color, owner=None):
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
                          lambda product: product.price * product.quantity,
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
        product.price * product.quantity}"""


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
