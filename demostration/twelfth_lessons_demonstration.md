# 1. Запис даних до файлу ;

# 2. Виклик функції з іншого файлу ;

# 3. Відлов виключень ;


# 1. Зчитування даних з файлу ;

```python3
# Відкриваємо файл для зчитування (режим 'r' - read)
with open('myfile.txt', 'r') as file:
    # Зчитуємо вміст файлу та призначаємо його змінній data
    data = file.read()

# Файл автоматично закривається, коли виходить із блоку 'with'

# Тепер data містить вміст зчитаного файлу
print(data)
```

# 1.1 Запис даних в файл; 
```python
# Відкриваємо файл для запису (режим 'w' - write)
with open('myfile.txt', 'w') as file:
    # Записуємо дані в файл
    file.write('Hello, World!')

# Файл автоматично закривається, коли виходить із блоку 'with'
```

# 1.2. Додавання даних до файлу без перезапису ;
```python
# Відкриваємо файл для додавання (режим 'a' - append)
with open('myfile.txt', 'a') as file:
    # Додаємо дані до файлу
    file.write('\nAdditional text.')

# Файл автоматично закривається, коли виходить із блоку 'with'
```

# 1.3. Зчитування файлу по рядках ;
```python
# Відкриваємо файл для зчитування (режим 'r' - read)
with open('myfile.txt', 'r') as file:
    # Читаємо файл по рядках у циклі
    for line in file:
        print(line.strip())  # strip() - видаляє символи переведення рядка ('\n' та інші)
```

# 3. Виключення;

**3.1**
```python
# Обробка виключень без блоку except:
try:
    result = 10 / 0  # Генерує ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Помилка: {e}")

```
**3.2**
```python
# Обробка різних типів виключень
try:
    num = int("abc")  # Генерує ValueError
except ValueError as e:
    print(f"ValueError: {e}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

```

**3.3**
```python
# Блок else
try:
    num = int(input("Введіть число: "))
except ValueError:
    print("Неправильний формат числа")
else:
    print(f"Ви ввели число: {num}")
# Блок else виконується, якщо виключення не виникає. 
# У цьому випадку, він виведе введене число.
```

**3.4.**
```python
# Блок finally
try:
    f = open("myfile.txt", "r")
    # робота з файлом
except FileNotFoundError:
    print("Файл не знайдено")
finally:
    f.close()  # Закриваємо файл навіть якщо сталася помилка

# Блок finally виконується завжди, незалежно від того, 
# чи сталася помилка, чи ні. 
# В цьому випадку, ми завжди закриваємо файл.
```

**3.5**
```python
# Підняття виключення
def divide(a, b):
    if b == 0:
        raise ValueError("Ділення на нуль не допускається")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Помилка: {e}")

# Ми можемо підняти виключення за допомогою ключового слова raise. 
# У цьому прикладі ми піднімаємо ValueError, якщо b дорівнює 0.
```

**3.6**
```python
# Користувацький клас виключення
class MyCustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    raise MyCustomError("Це моя власна помилка")
except MyCustomError as e:
    print(f"Помилка: {e}")

# Ми можемо створювати власні класи виключень.

```
**3.7**
```python
# Обробка виключень у циклі

while True:
    try:
        num = int(input("Введіть число: "))
        break
    except ValueError:
        print("Неправильний формат числа. Спробуйте ще раз.")

# через цикл for

for _ in range(3):  # Максимум 3 спроби
    try:
        num = int(input("Введіть число: "))
        break  # Вихід із циклу, якщо введено правильне число
    except ValueError:
        print("Неправильний формат числа. Спробуйте ще раз.")
else:
    print("Ви вичерпали всі спроби. Програма завершує роботу.")

```