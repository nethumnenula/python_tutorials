name = input("Enter your name: ")

while name == "":
    print("Empty!")
    name = input("Enter your name: ")
print(name)

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero.")
    else:
        break


