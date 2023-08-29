# **Functions**

# [Link](http://ruslan.rv.ua/python-starter/functions_def/functions_def.html)
# [W3School](https://www.w3schools.com/python/python_functions.asp)

**1. Приклад написання функції**

```python
def назва_функції():
       return "Hello from function"
```

**2. Позиційні та ключові параметри**
```python
def function(argument1, argument2, argument3):
    return argument1, argument2, argument3

function(argument3="a3", argument1="a1", argument2="a2")

```

**3. Функції з довільною кількістю аргументів**
```python
def func_args(*args):
  print(args)


def func_kwargs(*kwargs):
  print(kwargs)

```

**4. Функції з обов'язковими та необов'язковими параметрами**

```python
def func(x, y, z = 8):
    return x, y, z
```

**5. Локальна змінна - це змінна, яка оголошена всередині функції. Локальні змінні доступні тільки всередині функції, у якій їх було створено.**

```python
def sample_function():
    x = 35
    return x

```


**6. Глобальна змінна – це змінна, яка оголошена в основній програмі, поза межами функцій. Глобальні змінні є видимими для будь-якої частини програми, зокрема, всередині функцій.
Локальну змінну, що оголошена в середині функції, можна зробити видимою для усією програми, написавши перед нею службове слово global. Тоді значення цієї змінної збережеться і після завершення роботи функції, і не буде знищено, як це стається з усіма локальними змінними.**

```python
def sample_function():
    global x
    x = 35
    return x


sample_function()

print(x)
```

**7. nonlocal в Python**

```python
def func_outer():
    x = 2
    print('x is', x)

    def func_inner():
        nonlocal x
        x = 5
    func_inner()
    print('Changed local x to', x)

func_outer()


```