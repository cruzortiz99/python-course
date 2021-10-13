# Functions

1. Crear una función encargada de sumar dos números
2. Crear una función encargada de sumar **n** números enteros
3. Crear una función que devuelva un valor cuando una condición se cumpla y otro valor cuando la condición no se cumpla. Ejemplo:
   ```python
   # ifOrElse(whenIsTrue, whenIsFalse, condition)
   # ifOrElse("hola", "chao", True) -> "hola"
   # ifOrElse("hola", "chao", False) -> "chao"
   ```
4. Crear una función encargada de retornar un valor cuando el retorno de una función es cierta y otro valor cuando el retorno de una función es falsa. Ejemplo:
   ```python
   # ifOrElse("hola", "chao", lambda: True) -> "hola"
   # ifOrElse("hola", "chao", lambda: False) -> "chao"
   ```
5. Crear una función encargada de ejecutar una función cuando el retorno de una función es cierta y ejecuta otra cuando el retorno de una función es falsa. Ejemplo:
   ```python
   # ifOrElse(lambda: "hola", lambda: "chao", lambda: True) -> "hola"
   # ifOrElse(lambda: "hola", lambda: "chao", lambda: False) -> "chao"
   ```
6. Hacer de las funciones anteriores, de ejecución perezosa o **funciones de orden superior**.
   ```python
   # ifOrElse("hola", "chao", True)() -> "hola"
   # ifOrElse("hola", "chao", False)() -> "chao"
   ```
7. Dado:

   ```python
   list = [
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
       },{
         "name": "German",
         "last_name": "Montero",
         "age": 63,
       }],
       "car": {"name": "Cherokee", "type": "camioneta"}}
   ]
   ```

   7.1. Contar la cantidad de persona en la lista.
   7.2. Contar la cantidad de personas que poseen amigos.
   7.3. Contar la cantidad de personas que poseen el mismo tipo de carro.
   7.4. Mostrar una lista de los carros que se poseen
   7.5. Convierta los diccionarios en la lista en un tipo personalizado
