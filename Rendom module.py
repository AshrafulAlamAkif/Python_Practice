import random

#get a random number 5 to 15
print(random.randrange(5, 15)) 

list = ["a","b","c","d","e","f","d","g","h"]

#get random item from the list
print(random.choice(list))

#get random item from the list with array mode
print(random.choices(list))

#print shuffled list
random.shuffle(list)
print(list)
