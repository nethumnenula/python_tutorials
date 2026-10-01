# *args   = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments
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