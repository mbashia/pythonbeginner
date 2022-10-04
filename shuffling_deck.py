import random
import itertools
deck = list(itertools.product(range(1,14),['spades', 'clubs', 'hearts', 'diamonds'])) # finding the cartesian product
random.shuffle(deck)
for i in range(5):
    print(deck[i])