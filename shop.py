from items import Item, Weapon
from utils import slow_print, danger, highlight

def add_to_inventory(hero, item):
    if item.name in hero.inventory:
        hero.inventory[item.name]["quantity"] += 1
    else:
        hero.inventory[item.name] = {
            "item": item,
            "quantity": 1
        }

# ITEMS
health_potion = Item("Health Potion", 25)
mana_potion = Item("Mana Potion", 25)

weapons = {
    "sword": Weapon("Sword", 25, 5),
    "great sword": Weapon("Great Sword", 50, 10),
    "excalibur": Weapon("Excalibur", 100, 20),
}

shops = {
    "forest": [health_potion, mana_potion, weapons["sword"]],
    "mountains": [weapons["great sword"]],
    "void": [weapons["excalibur"]],
}


def display_shop(place, player):
    items = shops.get(place, [])

    while True:
        print(f"\n--- {place.upper()} SHOP ---")
        print(f"Gold: {player.gold}")

        for i, item in enumerate(items, 1):
            print(f"{i}. {item.name} ({item.price}g)")

        choice = input("Buy item or 'exit': ").strip().lower()

        if choice == "exit":
            return

        if not choice.isdigit():
            slow_print(danger("Invalid input"))
            continue

        index = int(choice) - 1
        if index < 0 or index >= len(items):
            slow_print(danger("Invalid selection"))
            continue

        item = items[index]

        if player.gold < item.price:
            slow_print(danger("Not enough gold"))
            continue

        player.gold -= item.price
        add_to_inventory(player, item.copy())

        slow_print(f"Bought {highlight(item.name)}")