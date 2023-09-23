# 1. Запис даних до файлу ;


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
