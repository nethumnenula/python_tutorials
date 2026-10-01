# An argument preceded by an identifier
# helps with readability
# order of argument does not matter

def hello(greeting, title, first, last):
    print(f"{greeting} {title}.{first} {last}")

hello("Hello", "Mr", last="Nethum", first="Nenula")


for x in range(1, 11):
    print(x, end=" ")

print()
print(1,2,3,4, sep="-")