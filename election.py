from random import randint
total = 0 #sets the total equal to 0
for i in range(10000): #repeats the process below 10,000 times since the range in 10000
  wins = 0 #makes wins equal to 0
  if randint(1,100) <= 87: #picks a number between 1-100 and compares it to 87 to see if that region is won
    wins = wins+1
  if randint(1,100) <= 65: #same as comment on line 5, but with it compared to 65
    wins = wins+1
  if randint(1,100) <= 17: #same as comment on line 7, but with it compared to 17
    wins = wins+1
  if wins >= 2: #checks to see if wins is greater than or equal to 2, and then adds 1 to total
    total += 1 
chance = (total/((float(10000))) * 100 #gives probability of winning
print "your chance in winning is %s%" % chance #statement that is printed out
