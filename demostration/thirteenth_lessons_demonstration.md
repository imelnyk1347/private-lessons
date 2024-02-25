# Exceptions

1. SyntaxError: Помилка синтаксису.
```python
if x = 5:
    print("Hello")

    
try:
    if x = 5:
        print("Hello")
except SyntaxError as e:
    print(f"Caught an exception: {e}")
```

2. IndentationError: Помилка відступів.
```python
def my_function():
print("Indentation error")


try:
    def my_function():
    print("Indentation error")
except IndentationError as e:
    print(f"Caught an exception: {e}")
```

3. NameError: Спроба використання невизначеної змінної.
```python
print(variable_that_does_not_exist)


try:
    print(variable_that_does_not_exist)
except NameError as e:
    print(f"Caught an exception: {e}")
```

4. TypeError: Невідповідність типів.
```python
result = 5 + "2"


try:
    result = 5 + "2"
except TypeError as e:
    print(f"Caught an exception: {e}")
```

5. ValueError: Отримання правильного типу, але неправильного значення.
```python
number = int("hello")


try:
    number = int("hello")
except ValueError as e:
    print(f"Caught an exception: {e}")
```

6. ZeroDivisionError: Ділення на нуль.
```python
result = 5 / 0


try:
    result = 5 / 0
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")
```

7. IndexError: Спроба доступу за межами списку або рядка.
```python
my_list = [1, 2, 3]
print(my_list[10])


try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError as e:
    print(f"Caught an exception: {e}")
```

8. KeyError: Спроба отримати доступ до неіснуючого ключа словника.
```python
my_dict = {"name": "John"}
print(my_dict["age"])


try:
    my_dict = {"name": "John"}
    print(my_dict["age"])
except KeyError as e:
    print(f"Caught an exception: {e}")
```

9. FileNotFoundError: Спроба відкрити неіснуючий файл.
```python
with open("nonexistent_file.txt", "r") as file:
    data = file.read()


try:
    with open("nonexistent_file.txt", "r") as file:
        data = file.read()
except FileNotFoundError as e:
    print(f"Caught an exception: {e}")
```

10. ModuleNotFoundError: Модуль не знайдено.
```python
import non_existent_module


try:
    import non_existent_module
except ModuleNotFoundError as e:
    print(f"Caught an exception: {e}")
```

11. AttributeError: Спроба отримати доступ до атрибута, який не існує.
```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list.upper())


try:
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list.upper())
except AttributeError as e:
    print(f"Caught an exception: {e}")
```

12. TypeError: Спроба викликати функцію з неправильною кількістю аргументів.
```python
def add(x, y):
    return x + y

result = add(3)


try:
    def add(x, y):
        return x + y

    result = add(3)
except TypeError as e:
    print(f"Caught an exception: {e}")
```

13. ImportError: Помилка імпорту модуля.
```python
from non_existent_module import some_function


try:
    from non_existent_module import some_function
except ImportError as e:
    print(f"Caught an exception: {e}")
```

14.MemoryError: Вичерпана пам'ять; IOError: Помилка вводу/виводу (наприклад, при спробі зчитати закритий файл).
```python
# IOError: Помилка вводу/виводу (наприклад, при спробі зчитати закритий файл).
with open("closed_file.txt", "r") as file:
    data = file.read()

    
try:
    with open("closed_file.txt", "r") as file:
        data = file.read()
except IOError as e:
    print(f"Caught an exception: {e}")

# MemoryError: Вичерпана пам'ять
my_list = [0] * 1000000000


try:
    my_list = [0] * 1000000000
except MemoryError as e:
    print(f"Caught an exception: {e}")
```