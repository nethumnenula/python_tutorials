num = 5
a = 6
b = 7
user_role = "Admin"

max_num = a if a > b else b
min_num = a if a < b else a

print(f"Maximum Number: {max_num}")
print(f"Minimum Number: {min_num}")

access_level = "Full Access" if user_role.lower() == "admin" else "Limited Access"
print(access_level)