#--------------------From Learning the Python Standard Library----------------

#---------------------------------Itertools-----------------------------------
import itertools

# This module will create an infinite counting mechanism

#--------------------------------Infinite Counting----------------------------
for x in itertools.count(50, 5):
    print(x)
    if x == 80:
        break;