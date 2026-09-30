#credit_number = "1233-3233-2122-2111-2222"

#print(credit_number[2 : 4 : 2])  # [start : end : step]
#print(credit_number[:6])
#print(credit_number[6:])
#print(credit_number[::2])

credit_number = input("Enter your credit card number: ")
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")
print(f"Reversed: {credit_number[::-1]}")