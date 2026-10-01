# dictionaries = a collection of {key:value} pairs
#               ordered and changeable. NO Duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

capitals.get("USA") # Get the value of the key

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem() # remove the latest item
# capitals.clear()
print(capitals)

keys = capitals.keys() # Get all keys
print(keys)

for key in keys:
    print(key)

values = capitals.values() # get all values
for value in values:
    print(value)


items = capitals.items()
print(items)
for key, value in items:
    print(f"{key}: {value}")

