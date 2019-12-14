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
# Combinations: Order does not matter-no copies with same inputs
