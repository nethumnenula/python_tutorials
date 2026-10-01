# fruits =     ["apple", "orange", "banana", "mango"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats =      ["chicken", "pork", "beef"]

groceries = [["apple", "orange", "banana", "mango"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "pork", "beef"]]

print(groceries[0][1])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()