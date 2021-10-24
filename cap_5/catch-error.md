<img src="../assets/img/python-logo.png" />

[<< Inicio](./README.md) [< Volver](./README.md) || [Siguiente >](./raise-error.md)

---

## Atrapar un error

```python
try:
  do_something()
except:
  do_something_when_fails()
```

## Multiples excepciones

```python
try:
  do_something()
except NameError:
  do_something_with_this_exception()
except:
  do_something_with_other_errors()
```

## Usando else

```python
try:
  do_something()
except:
  do_something_when_fails()
else:
  do_something_when_do_not_fails()

# ...
try:
  do_something()
except:
  do_something_when_fails()

do_something_when_do_not_fails()

```

## Usando finally

```python
try:
  do_something()
except:
  do_something_when_fails()
finally:
  do_something_after_success_or_fails()
```

---

[<< Inicio](./README.md) [< Volver](./README.md) || [Siguiente >](./raise-error.md)
