# *args   = allows you to pass multiple non-key arguments, stores as a tuple
# **kwargs = allows you to pass multiple keyword arguments, stores as a dictionary
#           * unpacking operator



# args
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,4,568,4,2))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("a","as","sa")
print()

# kwargs
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="nnn",city="meegoda", state="dampe", zip="10504")




# args & kwargs

