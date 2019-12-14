#-----------------------From Learning the Python Standard Library--------------
#------------------------Itertools: Permutations and Combinations--------------
import itertools

#-------------------------------Review of Permutations-------------------------
# A way, especially of one of several possible variations, in which a set or number of
# things can be ordered or arranged
# Permutations of same items and different order

# Permutations: Order Matters-Some copies with same inputs but in different order
# For an election we want to know what are the possible outccomes for a given election

# This will give us all the possible orderings for the election
election = {1: "Barb", 2: "Karen", 3: "Erin"}
for p in itertools.permutations(election):
    print (p)
    
for p1 in itertools.permutations(election.values()):
    print(p1)

# Combinations: Order does not matter-no copies with same inputs
# Combinations are similar to permutations in that they list a set of items but for 
# combinations no set has the exact same elements as another.

# We have a list of colors we can paint with and so we'll have a variable called 
# colors for painting and we'll have a list with red, blue, purple, orange, yellow 
# and pink but when we paint, we only want to paint with two colors and so we can use 
# the combinations method inside the itertools module.

colorsForPainting = ["Red", "Blue", "Purple", "Orange", "Yellow", "Pink"]
for c in itertools.combinations(colorsForPainting, 2):
    print(c)