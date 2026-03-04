import copy
from inventory import add_item

class ShopItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {
            "type": "item",
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

    def copy(self):
        return ShopItem(self.name, self.price, 1)


class ShopWeapon(ShopItem):
    def __init__(self, name, price, quantity, damage):
        super().__init__(name, price, quantity)
        self.damage = damage

    def to_dict(self):
        return {
            "type": "weapon",
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "damage": self.damage
        }
    
    def __str__(self):
        return f"{self.name}"

    def copy(self):
        return ShopWeapon(self.name, self.price, 1, self.damage)


# -------------------- SHOP ITEMS --------------------

healthPotion = ShopItem("Health Potion", 25, 2)
greaterHealthPotion = ShopItem("Greater Health Potion", 50, 1)
manaPotion = ShopItem("Mana Potion", 25, 2)
greaterManaPotion = ShopItem("Greater Mana Potion", 50, 1)

weapons = {
    "sword": ShopWeapon("Sword", 25, 1, 5),
    "great sword": ShopWeapon("Great Sword", 50, 1, 10),
    "staff": ShopWeapon("Staff", 30, 1, 3),
    "fire staff": ShopWeapon("Fire Staff", 40, 1, 5),
    "water staff": ShopWeapon("Water Staff", 40, 1, 5),
    "poison staff": ShopWeapon("Poison Staff", 40, 1, 7)
}

# -------------------- SHOPS --------------------

shops = {
    "forest": [healthPotion, manaPotion, weapons["sword"], weapons["staff"]],
    "desert": [healthPotion, manaPotion, weapons["fire staff"]],
    "mountains": [healthPotion, manaPotion, weapons["water staff"], weapons["great sword"]],
    "swamp": [greaterHealthPotion, greaterManaPotion, weapons["poison staff"]],
    "volcano": [greaterHealthPotion, greaterManaPotion]
}


def display_shop(place, player):
    print(f"\nWelcome to the {place.capitalize()} Shop!")
    print("=" * 40)
    print(f"{'Name':<25}{'Price':<10}{'Quantity':<10}")

    for item in shops[place]:
        print(f"{item.name:<25}{item.price:<10}{item.quantity:<10}")

    while True:
        print(f"\nYou have {player.gold} gold.")
        choice = input("\nEnter item name to buy (or 'exit'): ").strip().lower()
        if choice == "exit":
            return

        for item in shops[place]:
            if choice == item.name.lower():
                if item.quantity <= 0:
                    print("Out of stock.")
                    break
                if player.gold < item.price:
                    print("Not enough gold.")
                    break

                purchased_item = item.copy()
                add_item(purchased_item, player)
                player.gold -= item.price
                item.quantity -= 1

                print(f"You bought {item.name}!")
                print("Inventory:")
                for item_name, data in player.inventory.items():
                    print(f"{item_name} x{data['quantity']}")
                break
        else:
            print("Item not found.")