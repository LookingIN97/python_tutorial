# Lesson 2.5: More operations

### Remainer - modular arithmetic

systematically restrict computation to a range
long division - divide by a number, we get a quotient plus a remainder
quotient is integer division //, the remainder is % (Docs)

```python
# problem - get the ones digit of a number
num = 49
tens = num // 10
ones = num % 10
print tens, ones
print 10 * tens + ones, num
```

application - 24 hour clock
http://en.wikipedia.org/wiki/24-hour_clock

```python
hour = 20
shift = 8
print (hour + shift) % 24
```

application - screen wraparound
Spaceship from week seven

```python
width = 800
position = 797
move = 5
position = (position + move) % width
print position
```

Data conversion operations

convert an integer into string - str
convert an hour into 24-hour format "03:00", always print leading zero

```python
hour = 3
ones = hour % 10
tens = hour // 10
print tens, ones, ":00"
print str(tens), str(ones), ":00"
print str(tens) + str(ones) + ":00"
```

### Python modules - extra functions implemented outside basic Python

```python
import math
print(math.pi)
```







### Stupid quizs

**Quiz: In Python, what operator computes the remainder of one number with respect to another?**

A. /

B. **

C. %

D. //



**Quiz: In the expression 6 + 7 % 5, which operator is evaluated first (i.e., which was higher precedence)?**

A. %

B. They have the same precedure

C. +

D. Both are evaluated at the same time.

**Quiz: In Python, what statement is used to load a module?**

A. `get`

B. `import`

C. `load`

D. All modules load automatically.