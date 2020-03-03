from random import seed
from random import randint

seed(4)

a = [randint(1, 15), randint(1, 15), randint(1, 15), randint(1, 15), randint(1, 15), randint(1, 15), randint(1, 15), randint(1, 15), randint(1, 15), randint(1, 15),]

b = [randint(1, 15), randint(1, 15), randint(1, 15), randint(1, 15), randint(1, 15), randint(1, 15), randint(1, 15), randint(1, 15), randint(1, 15), randint(1, 15),]

print(a)
print(b)

c = []

for i in a:
    if i in b:
        c.append(i)
        
print(c)