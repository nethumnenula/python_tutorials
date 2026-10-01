# collection = single variable used to store multiple values
#   List  = [] ordered and changeable. Duplicates OK.
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates. Cannot use Indexing
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER.


# List
fruits = ["apple", "banana", "orange", "coconut"]
print(fruits)
for fruit in fruits:
    print(fruit)

# print(dir(fruits))
# print(help(fruits))
print(len(fruits))
print("apple" in fruits)

fruits[0] = "Mango"
fruits.append("Pineapple") # add an element
fruits.remove("banana")
fruits.insert(0, "avocado")
fruits.sort()
fruits.reverse()
fruits.clear()
#print(fruits.index("pineapple"))
print(fruits.count("banana"))
for fruit in fruits:
    print(fruit)


# Set
fruits_set = {"apple", "banana", "orange", "coconut"}
print(fruits_set)
fruits_set.add("pineapple")
fruits_set.remove("apple")
fruits_set.pop()  # pop whatever in first randomly
fruits_set.clear()

# Tuple
fruits_tuple = ("apple", "banana", "orange", "coconut")
print(fruits_tuple)
print(len(fruits_tuple))
print(fruits_tuple.index("apple"))
print(fruits_tuple.count("apple"))
for fruit in fruits_tuple:
    print(fruit, end=" ")