<img src="../assets/img/python-logo.png" />

[< Volver](./data_types.md)

---

## Texto en multiples lineas

```python
print("""
Texto en
multiples
lineas
""")

# output:
Texto en
multiples
lineas
```

## Texto como lista de caracteres

```python
a = "texto"

print(a[2])

# output: x
```

## Longitud del texto

```python
print(len("texto"))

# output: 5
```

## Tomar parte del texto

```python
text = "texto"

print(text, text[1:3], text[:2], text[2:])

# output: texto ex te xto
```

## Modificar el texto

```python
text = "   Texto   "
# Mayúsculas
print(text.upper())

# output:    TEXTO
# ---
# Minúsculas
print(text.lower())

# output:    texto
# ---
# Remover Espacios en blanco al inicio y final
print(text.strip())

# output: Texto
# ---
# Remplazar texto
print(text.replace("T", "TT"))

# output:    TTexto
# ---
# Dividir texto
print(text.split("x"))

# output: ['   Te', 'to   ']
# ---
# Concatenar texto
text1 = "Te"
text2 = "xto"

print(text1 + text2)

# output: Texto
#---
# Formatear texto o hacerlo dinámico
dynamic_text = "Hola, {}"

print(dynamic_text.format("Cruz"))

# output: Hola, Cruz
# ---
# Capitalizar un texto
print(text.capitalize())

# output:    text
# ---
# Contar caracteres
print(text.count("t"))

# output: 1
# ---
# Revisar ultimo elemento del texto de
print(text.endswith("0"))

# output: False
# ---
# Encontrar indice de un sub-texto
print(text.find("ext"))

# output: 4

```

---

[< Volver](./data_types.md)
