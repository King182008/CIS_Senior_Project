import copy
from inventory import add_item
from utils import highlight, danger, name, slow_print

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
    def __init__(self, name, price, quantity, damage, mana_gain=5):
        super().__init__(name, price, quantity)
        self.damage = damage
        self.mana_gain = mana_gain

    def to_dict(self):
        return {
            "type": "weapon",
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "damage": self.damage,
            "mana_gain": self.mana_gain
        }
    
    def __str__(self):
        return f"{self.name}"

    def copy(self):
        return ShopWeapon(self.name, self.price, 1, self.damage, self.mana_gain)


# -------------------- SHOP ITEMS --------------------

healthPotion = ShopItem("Health Potion", 25, 2)
greaterHealthPotion = ShopItem("Greater Health Potion", 50, 1)
manaPotion = ShopItem("Mana Potion", 25, 2)
greaterManaPotion = ShopItem("Greater Mana Potion", 50, 1)
bread = ShopItem("Bread", 5, 1)
silverPendent = ShopItem("Silver Pendent", 50, 1)

weapons = {
    "fists": ShopWeapon("Fists", 0, 1, 5, 5),
    "Wooden Sword": ShopWeapon("Wooden Sword", 0, 1, 5, 5),
    "sword": ShopWeapon("Sword", 25, 1, 5, 5),
    "great sword": ShopWeapon("Great Sword", 50, 1, 10, 5),

    "staff": ShopWeapon("Staff", 30, 1, 3, 7),
    "fire staff": ShopWeapon("Fire Staff", 40, 1, 5, 8),
    "water staff": ShopWeapon("Water Staff", 40, 1, 5, 8),
    "poison staff": ShopWeapon("Poison Staff", 40, 1, 7, 10),

    "Excalibur": ShopWeapon("Excalibur", 100, 1, 20, 5),
    "Caduceus Staff": ShopWeapon("Caduceus Staff", 100, 1, 15, 15)
}

# -------------------- SHOPS --------------------

shops = {
    "forest": [healthPotion, manaPotion, weapons["sword"], weapons["staff"]],
    "desert": [healthPotion, manaPotion, weapons["fire staff"]],
    "mountains": [healthPotion, manaPotion, weapons["water staff"], weapons["great sword"]],
    "swamp": [greaterHealthPotion, greaterManaPotion, weapons["poison staff"]],
    "volcano": [greaterHealthPotion, greaterManaPotion],
    "void": [weapons["Excalibur"], weapons["Caduceus Staff"]],
    "village": [bread, silverPendent]
}

def display_shop(place, player):
    items = shops[place]

    # Helper for padding BEFORE coloring
    def pad(text, width):
        return f"{text:<{width}}"

    print(highlight(f"\n=== {place.upper()} SHOP ==="))
    print("-" * 55)

    # Header (pad first, then color)
    header = (
        highlight(pad("#", 4)) +
        highlight(pad("Item", 30)) +
        highlight(pad("Price", 10)) +
        highlight(pad("Stock", 8))
    )
    print(header)
    print("-" * 55)

    # Items
    for i, item in enumerate(items, 1):
        base_name = item.name

        # Add damage text BEFORE padding
        if hasattr(item, "damage"):
            base_name += f" ({item.damage} dmg)"

        # Pad FIRST (no colors yet)
        col_index = pad(str(i), 4)
        col_name = pad(base_name, 30)
        col_price = pad(str(item.price), 10)
        col_stock = pad(str(item.quantity), 8)

        # THEN apply colors
        col_index = highlight(col_index)
        col_name = name(col_name)
        col_price = highlight(col_price)
        col_stock = danger(col_stock) if item.quantity == 0 else highlight(col_stock)

        print(col_index + col_name + col_price + col_stock)

    print("-" * 55)

    # =========================
    # BUY LOOP
    # =========================
    while True:
        print(f"\nGold: {highlight(player.gold)}")

        choice = input(
            f"Select item {highlight('(number/name)')} or {danger('exit')}:\n>> "
        ).strip().lower()

        if choice == "exit":
            return

        selected_item = None

        # Select by number
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(items):
                selected_item = items[index]
            else:
                print(danger("Invalid selection."))
                continue
        else:
            for item in items:
                if item.name.lower() == choice:
                    selected_item = item
                    break

            if not selected_item:
                print(danger("Item not found."))
                continue

        # =========================
        # PURCHASE LOGIC
        # =========================
        if selected_item.quantity <= 0:
            print(danger("Out of stock."))
            continue

        if player.gold < selected_item.price:
            print(danger("Not enough gold."))
            continue

        purchased_item = selected_item.copy()
        add_item(purchased_item, player)

        player.gold -= selected_item.price
        selected_item.quantity -= 1

        slow_print(f"{highlight('✔ Bought')} {name(selected_item.name)}")

        # =========================
        # INVENTORY DISPLAY
        # =========================
        print(highlight("\n--- Inventory ---"))

        for i, (item_name, data) in enumerate(player.inventory.items(), 1):
            item_col = pad(item_name, 25)
            qty_col = pad(f"x{data['quantity']}", 5)

            print(f"{i:>2}. {name(item_col)}{highlight(qty_col)}")