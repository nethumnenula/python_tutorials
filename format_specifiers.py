# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center justify
# :+ = use a plus sign to indicate positive values
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma seperator


price1 = 37777.14159
price2 = -982.222
price3 = 12.34

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2}")
print(f"Price 3 is ${price3}")