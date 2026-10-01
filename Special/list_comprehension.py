# A concise way to create lists in Python
# Compact and easier to read than traditional loops
# [expression for value in iterable if condition]


# Normal
doubles = []
for x in range(1, 11):
    doubles.append(x)
print(doubles)

# List Comprehensions

doubles2 = [x * 2 for x in range(1, 11)]
print(doubles2)

fruits = ["mango", "pineapple", "grapes"]
fruits = [fruit.capitalize() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruits)
print(fruit_chars)
