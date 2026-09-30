# converting a variable from one data type to another str() int() float() bool()

#name = "Nethum"
#age = 22
#gpa = 4.0
#is_student = True
#gpa = int(gpa)

name = input("Enter Your name: ")
age = int(input(f"Enter Your age, {name}: "))
#age = int(age)
age += 1
print(f"\nWelcome {name}")
print(f"You are {age} years old!")
