username = input("Enter a username: ")

if len(username) > 12 :
    print("Cannot exceed 12 characters")
elif not username.find(" ") == -1:
    print("Cannot contain spaces")
elif not username.isalpha():
    print("Cannot contain numbers")
else:
    print(username)