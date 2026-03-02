import copy

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

    def copy(self):
        return ShopWeapon(self.name, self.price, 1, self.damage)


# -------------------- SHOP ITEMS --------------------

healthPotion = ShopItem("Health Potion", 25, 2)
greaterHealthPotion = ShopItem("Greater Health Potion", 50, 1)
manaPotion = ShopItem("Mana Potion", 25, 2)
greaterManaPotion = ShopItem("Greater Mana Potion", 50, 1)

sword = ShopWeapon("Sword", 25, 1, 5)
greatSword = ShopWeapon("Great Sword", 50, 1, 10)

staff = ShopWeapon("Staff", 30, 1, 3)
fireStaff = ShopWeapon("Fire Staff", 40, 1, 5)
waterStaff = ShopWeapon("Water Staff", 40, 1, 5)
poisonStaff = ShopWeapon("Poison Staff", 40, 1, 7)

# -------------------- SHOPS --------------------

shops = {
    "forest": [healthPotion, manaPotion, sword, staff],
    "desert": [healthPotion, manaPotion, fireStaff],
    "mountains": [healthPotion, manaPotion, waterStaff, greatSword],
    "swamp": [greaterHealthPotion, greaterManaPotion, poisonStaff],
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
                player.inventory.append(purchased_item)
                player.gold -= item.price
                item.quantity -= 1

                print(f"You bought {item.name}!")
                print("Inventory:", [i.name for i in player.inventory])
                break
        else:
            print("Item not found.")