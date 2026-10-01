from script1 import *

def fav_drink(drink):
    print(f"Your favourite drink is {drink}")

def main():
    print("This is script2")
    fav_food("sushi")
    fav_drink("pepsi")
    print("goodbye!")



if __name__ == '__main__':
    main()