---
Language: Python
Author: PenguLabs
---

```
dHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHb
HHP%%#%%%%%%%%%%%%%%%%#%%%%%%%#%%VHH
HH%%%%%%%%%%#%v~~~~~~\%%%#%%%%%%%%HH
HH%%%%%#%%%%v'        ~~~~\%%%%%#%HH
HH%%#%%%%%%v'dHHb      a%%%#%%%%%%HH
HH%%%%%#%%v'dHHHA     :%%%%%%#%%%%HH
HH%%%#%%%v' VHHHHaadHHb:%#%%%%%%%%HH
HH%%%%%#v'   `VHHHHHHHHb:%%%%%#%%%HH
HH%#%%%v'      `VHHHHHHH:%%%#%%#%%HH
HH%%%%%'        dHHHHHHH:%%#%%%%%%HH
HH%%#%%        dHHHHHHHH:%%%%%%#%%HH
HH%%%%%       dHHHHHHHHH:%%#%%%%%%HH
HH#%%%%       VHHHHHHHHH:%%%%%#%%%HH
HH%%%%#   b    HHHHHHHHV:%%%#%%%%#HH
HH%%%%%   Hb   HHHHHHHV'%%%%%%%%%%HH
HH%%#%%   HH  dHHHHHHV'%%%#%%%%%%%HH
HH%#%%%   VHbdHHHHHHV'#%%%%%%%%#%%HH
HHb%%#%    VHHHHHHHV'%%%%%#%%#%%%%HH
HHHHHHHb    VHHHHHHH:%odHHHHHHbo%dHH
HHHHHHHHboodboooooodHHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
VHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHV
```
---

## 1. What is a variable?

A variable is a name that points to a value in memory.
> In Python, you do not "create variables", you assign names to values.

```Python
x = 10
name = "Alice"
pi = 3.14159
```

- The value exists first, then the name points to it
- Variables can be reassigned

```Python
x = 10
print(x)
x= 20
print(x)
```

## 2. Python is dynamically typed
You do not need to specify the type of a variable

```Python
x = 10
x = "hello"
x = 3.5
```

> The **type belongs to the value**, not to the variable.

## 3. Common built-in types (first contact)
- Integer (int)
```Python
age = 25
print(type(age))
count = -3
print(type(count))
```

- Float
```Python
price = 19.99
print(type(price))
temperature = -5.2
print(type(temperature))
```

- String
```Python
name = "Python"
print(type(name))
message = 'Hello world'
print(type(message))
```
Quotes matters (" " vs ' ')
Choose the one that makes your string easier to read.

- Boolean
```Python
is_active = True
print(type(is_active))
is_admin = False
print(type(is_admin))
```

## 4. How to name variables? (Python style)
- Use lowercase
- Use underscores
- Be descriptive

Technical rules:
- Cannot start with a number
- No spaces
- Case-sensitive (age ≠ Age)
## 5. Variables are references
- a and b point to the same value
- This matters more later (lists, objects)
```Python
a = 10
b = a
print(a)
print(b)

a = 15

print(a)
print(b)
```