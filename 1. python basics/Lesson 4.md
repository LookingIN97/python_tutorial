# Lesson 4: Conditionals (Control Flow)

**Example**

```python
def greet(friend, money):
    if friend and (money > 20):
        print "Hi!"
        money = money - 20
    elif friend:
        print "Hello"
    else:
        print "Ha ha"
        money = money + 10
    return money


money = 15

money = greet(True, money)
print "Money:", money
print ""

money = greet(False, money)
print "Money:", money
print ""

money = greet(True, money)
print "Money:", money
print ""
```



**Quiz: write a Python script to identify if a year is a leap year**

















**Answer**

```python
# Conditionals Examples

# Return True if year is a leap year, false otherwise
def is_leap_year(year):
    if (year % 400) == 0:
        return True
    elif (year % 100) == 0:
        return False
    elif (year % 4) == 0:
        return True
    else:
        return False


year = 2012
leap_year = is_leap_year(year)
    
if leap_year:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
    
```

**Quiz: Which of the following are valid clauses in an `if` statement?**

A. `elseif`

B. `if`

C. `else`

D. `elif`

