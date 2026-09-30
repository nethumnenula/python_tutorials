name = input("Enter your full name: ")

print(f"Length of the name: {len(name)}")
find = name.find(" ") # first
findr = name.rfind(" ") # last
capitalized = name.capitalize()
upper = name.upper()
lower = name.lower()
is_digit = name.isdigit() # check
is_alpha = name.isalpha() # checking alphabetical chars


phone_number = input("Enter the phone #: ")
how_many = phone_number.count("0")
print(how_many)

# replace
phone_number.replace("0", " ") # replace zeros with spaces

