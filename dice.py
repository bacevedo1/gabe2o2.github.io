from random import randint
number = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

for i in range(500):
    rolls = randint(1,6) + randint(1,6)
    number[rolls] += 1
for z in number:
    print (number[z]/500)
