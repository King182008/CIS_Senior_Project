from items import Item, Weapon, is_weapon
from utils import slow_print, highlight


def show_inventory(hero):

    if not hero.inventory:
        print("Inventory empty")
        return

    items = list(hero.inventory.items())

    print("\nINVENTORY")
    for i, (key, data) in enumerate(items, 1):
        item = data["item"]
        qty = data["quantity"]
        print(f"{i}. {item.name} x{qty}")

    print("\n[use] [equip] [exit]")
    choice = input(">> ").strip().lower()

    if choice == "exit":
        return

    if choice not in ["use", "equip"]:
        print("Invalid option")
        return

    try:
        index = int(input("Select item number: ")) - 1
        key, data = items[index]
    except:
        print("Invalid selection")
        return

    item = data["item"]

    # =========================
    # USE ITEM
    # =========================
    if choice == "use":

        if isinstance(item, Weapon):
            print("Weapons cannot be used")
            return

        name = item.name.lower()

        if "health" in name:
            hero.health += 25
        elif "mana" in name:
            hero.mana += 25
        else:
            print("Nothing happens")

        data["quantity"] -= 1

        if data["quantity"] <= 0:
            del hero.inventory[key]


    # =========================
    # EQUIP WEAPON
    # =========================
    elif choice == "equip":

        if isinstance(item, Weapon):
            hero.weapon = item
            slow_print(f"Equipped {highlight(item.name)}")
        else:
            print("Not a weapon")