# **Dict / list comprehension**

# **1. Create dict**

```python3
dict_example = {
    '1': 'first',
    '2': 'second',
    '3': 'third',
    '4': 'fourth',
    '5': 'fifth'
}
print(type(dict_example))

tuple_dict = dict(name = "John", age = 36, country = "Norway")

print(tuple_dict) 
```

# **2. Get elements from dict**
```python3
# 2.1
countries_capitals = {
    "Ukraine": "Kyiv",
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo"
}
print(countries_capitals['USA'])

# 2.2
countries_capitals = {
    "Ukraine": "Kyiv",
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo"
}
new_dict = countries_capitals.keys()
print(new_dict)

# 2.3
countries_capitals = {
    "Ukraine": "Kyiv",
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo"
}
new_dict = countries_capitals.values()
print(new_dict)

# 2.4
countries_capitals = {
    "Ukraine": "Kyiv",
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo"
}
new_dict = countries_capitals.items()
print(new_dict)

# 2.5
countries_capitals = {
    "Ukraine": "Kyiv",
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo"
}
for key, value in countries_capitals.items():
    print(f'Key is {key}, value as {value}')
```

# **3. Update items**
```python3
cars = {
    "brand": "Ford",
    "model": "BMW",
    "year": 2020
}

cars["model"] = "Renault"
cars["year"] = 2025
print(cars)

cars = {
    "brand": "Ford",
    "model": "BMW",
    "year": 2020
}

cars.update({"year": 2026})
print(cars)
```

# **4. Remove elements**
```python3
# pop() - remove by key
cars = {
    "brand": "Ford",
    "model": "BMW",
    "year": 2020
}
cars.pop("year")
print(cars)

# popitem() - removes the last inserted item
cars = {
    "brand": "Ford",
    "model": "BMW",
    "year": 2020
}
cars.popitem()
print(cars)

# del - danger !!! - del keyword removes the item with the specified key name
cars = {
    "brand": "Ford",
    "model": "BMW",
    "year": 2020
}
del cars["year"]
print(cars)

# !!! delete dict with all variables
cars = {
    "brand": "Ford",
    "model": "BMW",
    "year": 2020
}
del cars
print(cars)
```

# **5. Loops**

```python3
cars = {
    "brand": "Ford",
    "model": "BMW",
    "year": 2020
}
for key in cars.keys():
    print(key)

for value in cars.values():
    print(value)

for key, value in cars.items():
    print(key, value)
```

# **6. Copy elements**

```python3
cars = {
    "brand": "Ford",
    "model": "BMW",
    "year": 2020
}
new_cars_dict = cars.copy()
new_cars_dict["model"] = "Renault"

print(new_cars_dict, cars, sep='\n')
```

# **7. Nested dictionaries**
```python3
family = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  },
  "child3": {
    "name": "Linus",
    "year": 2011
  }
}

print(family["child1"])

# Create nested dict
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

family = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(family)
```
# **8. setdefault()**
```python3
# returns the value of the item with the specified key. 
# If the key does not exist, insert the key, with the specified value, see example below

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x)
```

# **9. fromkeys()**
```python3
# Create a dictionary

tuple_object = ('key1', 'key2', 'key3')
values = 0

create_dict = dict.fromkeys(tuple_object, values)

print(create_dict)

# ------------------next example--------------------------

tuple_object = ('key1', 'key2', 'key3')

create_dict = dict.fromkeys(tuple_object)

print(create_dict)
```
# **10.clear()**
```python3
# clear all elements from dict

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

print(car)
```

# **List comprehension**
```python3
# 1.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list_first = []

for i in fruits:
    new_list_first.append(i)
    
new_list = [x for x in fruits]

print(new_list)
print(new_list_first)

# 2. 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for x in fruits:
  if "a" in x:
    new_list.append(x)

print(new_list)

new_list_1 = [fruit for fruit in fruits if "a" in fruit]
print(new_list_1)

# 3. 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = [x for x in fruits if x != "apple"]

print(new_list)

# 4.
new_list = [x for x in range(10)]

print(new_list)

# 5. 
new_list = [i for i in range(10) if i % 2 == 0]
new_list_second = [i for i in range(10) if i > 6]
print(new_list, new_list_second, sep="\n")

# 6.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = [i.upper() for i in fruits]
new_list_second = [i.title() for i in fruits]

print(new_list, new_list_second, sep="\n")

# 7.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = [x if x != "banana" else "orange" for x in fruits]

print(new_list)
```