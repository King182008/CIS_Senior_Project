import travel


class ShopItem():

    def __init__(self, name, price, quantity):

        self.name = name
        self.price = price
        self.quantity = quantity


# ---------- ITEMS ----------

healthPotion = ShopItem("Health Potion", 25, 2)
greaterHealthPotion = ShopItem("Greater Health Potion", 50, 1)

manaPotion = ShopItem("Mana Potion", 25, 2)
greaterManaPotion = ShopItem("Greater Mana Potion", 50, 1)

sword = ShopItem("Sword", 25, 2)
greatSword = ShopItem("Great Sword", 50, 1)

staff = ShopItem("Staff", 30, 1)
fireStaff = ShopItem("Fire Staff", 40, 1)
waterStaff = ShopItem("Water Staff", 40, 1)
poisonStaff = ShopItem("Poison Staff", 40, 1)


# ---------- SHOPS ----------

shops = {
    "forest": [healthPotion, manaPotion, sword, staff],
    "desert": [healthPotion, manaPotion, fireStaff],
    "mountains": [healthPotion, manaPotion, waterStaff, greatSword],
    "swamp": [greaterHealthPotion, greaterManaPotion, poisonStaff],
    "volcano": [greaterHealthPotion, greaterManaPotion]
}


# ---------- SHOP DISPLAY ----------

def display_shop(place, player):

    print(f"\nWelcome to the {place.capitalize()} Shop!")
    print("=" * 40)

    print(f"{'Name':<25}{'Price':<10}{'Quantity':<10}")

    for item in shops[place]:
        print(f"{item.name:<25}{item.price:<10}{item.quantity:<10}")

    while True:

        choice = input(
            "\nEnter item name to buy (or 'exit'): "
        ).strip().lower()

        if choice == "exit":
            return

        # SEARCH SHOP ITEMS
        for item in shops[place]:

            if choice == item.name.lower():

                if item.quantity <= 0:
                    print("Out of stock.")
                    break

                if player.gold < item.price:
                    print("Not enough gold.")
                    break

                # BUY ITEM
                player.gold -= item.price
                item.quantity -= 1

                # ADD TO INVENTORY ⭐⭐⭐⭐⭐
                player.inventory.append(item.name)

                print(f"You bought {item.name}!")

                print("Inventory:", player.inventory)

                break

        else:
            print("Item not found.")