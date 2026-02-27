import travel

class ShopItem():
    def __init__(self):
        self.name = ""
        self.price = 0
        self.quantity = 0

healthPotion = ShopItem()
healthPotion.name = "Health Potion"
healthPotion.price = 25
healthPotion.quantity = 2

greaterHealthPotion = ShopItem()
greaterHealthPotion.name = "Greater Health Potion"
greaterHealthPotion.price = 50
greaterHealthPotion.quantity = 1

manaPotion = ShopItem()
manaPotion.name = "Mana Potion"
manaPotion.price = 25
manaPotion.quantity = 2

greaterManaPotion = ShopItem()
greaterManaPotion.name = "Greater Mana Potion"
greaterManaPotion.price = 50
greaterManaPotion.quantity = 1

sword = ShopItem()
sword.name = "Sword"
sword.price = 25
sword.quantity = 2

greatSword = ShopItem()
greatSword.name = "Great Sword"
greatSword.price = 50
greatSword.quantity = 1

staff = ShopItem()
staff.name = "Staff"
staff.price = 30
staff.quantity = 1

fireStaff = ShopItem()
fireStaff.name = "Fire Staff"
fireStaff.price = 40
fireStaff.quantity = 1

waterStaff = ShopItem()
waterStaff.name = "Water Staff"
waterStaff.price = 40
waterStaff.quantity = 1

poisonStaff = ShopItem()
poisonStaff.name = "Poison Staff"
poisonStaff.price = 40
poisonStaff.quantity = 1

shops = {"forest": [healthPotion, manaPotion, sword, staff], 
         "desert": [healthPotion, manaPotion, fireStaff],
         "mountains": [healthPotion, manaPotion, waterStaff, greatSword],
         "swamps": [greaterHealthPotion, greaterManaPotion, poisonStaff],
         "volcano": [greaterHealthPotion, greaterManaPotion]
    }

def display_shop(place):
    print(f"Welcome to the {place} Shop! What would you like to buy?")
    print("=" * 30)
    print(f"{"Name":<15} {"Price":<10} {"Quantity":<10}")
    for item in shops[place]:
        print(f"{item.name:<15} {item.price:<10} {item.quantity:<10}")


if __name__ == "__main__":
    # initialize state from travel module
    currentPlace = travel.currentPlace

    while True:
        action = input("What would you like to do? (Shop, Travel or Stop) ")
        if action.lower() == "shop":
            display_shop(currentPlace)
        elif action.lower() == "travel":
            currentPlace = travel.travel(currentPlace)
        elif action.lower() == "stop":
            break