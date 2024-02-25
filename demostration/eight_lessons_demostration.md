# Tuple

**1. Create tuple:** `tuple()`;

**2. Get elements from tuple:** `tuple[0]`. [Example](https://www.w3schools.com/python/python_tuples_access.asp)

**3. Check element on tuple: if, for.**
[Link](https://www.w3schools.com/python/python_tuples_loop.asp)

**example if**
```
elements = (1, 2, 3, 4, 5, 6)
element = 1
if element in elements:
    'print('OK)
```
**example for**
```
elements = (1, 2, 3, 4, 5, 6)
for element in elements:
    print(element)
```
**example len**
```
fruits = ("apple", "banana", "cherry")
for fruit in range(len(fruits)):
  print(fruits[fruit]) 
```
**4. Update tuple:**
```
fruits = ("apple", "banana", "cherry")
convert_in_list = list(fruits)
convert_in_list[2] = "kiwi"
fruits = tuple(convert_in_list)

print(fruits) 

```
**4.1. Add elements to tuple**:
```
fruits = ("apple", "banana", "cherry")
convert_in_list = list(fruits)
convert_in_list.append("orange")
fruits = tuple(convert_in_list)

print(fruits)
```
**4.2. Add tuple to tuple:**
```
fruits = ("apple", "banana", "cherry")
new_tuple = ("orange",)
fruits += new_tuple

print(fruits)


```
**5. Unpack the tuple:**
```
5.1.
fruits = ("apple", "banana", "cherry")
(first, second, third) = fruits

print(first)
print(second)
print(third)

5.2.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(first, second, *another_elements) = fruits

print(first)
print(second)
print(another_elements)

5.3.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(first, *another_elements, third) = fruits

print(first)
print(second)
print(another_elements)
```

**6. Methods**

**count**
```
elements = (1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)
count_of_elements = elements.count(6)

print(count_of_elements)
```
**index**
```
elements = (1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)
count_of_elements = elements.index(6)

print(count_of_elements)
```