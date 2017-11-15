# Lesson 5: Flow diagram, Loop, List, Dictionary

### Flow diagram

Go draw them on the whiteboard.



### Loop

```python
my_list = [1, 2, 3]
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

# use value from iteration    
for num in my_list:
    print(num)

# use index to extract value
for i in range(len(my_list)):
    print(i, my_list[index])

# use enumerate to write better code
for index, num in enumerate(my_list):
    print(index, num)

```



### List

```python
# initialize a list
my_list = [1, 2, 3]
print(my_list)

# append a value to its end
my_list.append(4)
print(my_list)

# pop the first element out of the list
my_list.pop()
print(my_list)

# add two more values to maintain length
my_list.extend([5, 6])
print(my_list)

# insert a value to specific index
my_list.insert(2, 666)
print(my_list)

# remove an element by value
my_list.remove(666)
print(my_list)

# remove an element by index
my_list.pop(2)
print(my_list)
```



### Dictionary

```python
# create a dictionary
my_dict = {"year": 2017,
           1: True,
           (1, 2): "tuple can be keys"}

# access a value by key
print(my_dict[1])

# iter through all key, value pairs
for key, value in my_dict.items():
    print(key, value)

# add a key-value pair
my_dict["one more"] = 666
print(my_dict)

# alter a key-value pair
my_dict["year"] = 2007
print(my_dict)
```

