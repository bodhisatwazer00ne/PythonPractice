import random
from random import randint
import statistics

#choice function from random module is used to pick a random element from a list or string
coin=random.choice(["heads", "tails"])
print(coin)

#randint(a,b) returns a random integer between a and b (inclusive)

dice = random.randint(1, 6)
print(dice)

#random.sample() returns multiple unique elements from a list
num=[1,2,3,4,5]
print(random.sample(num, 2))   # two unique values

#shuffle() shuffles the elements of a list in place
cards=["King","Queen","Jack","10"]
random.shuffle(cards)
for card in cards:
    print(card)
    
    
    
meanmarks=statistics.mean([100,88,93,69,76])
print(meanmarks)