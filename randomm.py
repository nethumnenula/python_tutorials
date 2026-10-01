import random

number = random.randint(1, 6)
print(number)

low = 1
high = 100
rand_num = random.randint(low, high)

options = ("rock", "scissor", "paper")
option = random.choice(options)
print(option)

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
random.shuffle(cards)
print(cards)