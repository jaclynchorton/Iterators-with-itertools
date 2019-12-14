#--------------------From Learning the Python Standard Library----------------

#---------------------------------Itertools-----------------------------------
import itertools

# This module will create an infinite counting mechanism

#--------------------------------Infinite Counting----------------------------
for x in itertools.count(50, 5):
    print(x)
    if x == 80:
        break;
    
#-------------------------------Infinite Cycling------------------------------
# Infinitely cycling through an input
x = 0;
for c in itertools.cycle("RACECAR"):
    print(c)
    x = x + 1
    if x > 50:
        break;
    
#------------------------------Infinite Repeating-----------------------------

for r in itertools.repeat(True):
    print(r)
    x = x + 1
    if x > 100:
        break;