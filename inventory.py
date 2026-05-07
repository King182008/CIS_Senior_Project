import re
from utils import highlight, danger, name


# =========================
# HELPERS (ANSI-safe padding)
# =========================

def clean_len(text):
    """Remove ANSI color codes so spacing works correctly."""
    return len(re.sub(r'\x1b\[[0-9;]*m', '', str(text)))


def pad(text, width):
    """Pad based on visible length (not colored length)."""
    text = str(text)
    return text + " " * max(0, width - clean_len(text))


# =========================
# INVENTORY UI
# =========================

def show_inventory(hero):

    if not hero.inventory:
        print(danger("\n--- Inventory Empty ---"))
        print(f"Gold: {highlight(hero.gold)}")
        return

    print(highlight("\n=== INVENTORY ==="))
    print("-" * 55)

    items_list = list(hero.inventory.items())

    # Header (NO coloring inside padding)
    header = (
        pad("#", 4) +
        pad("Item", 30) +
        pad("Qty", 6)
    )

    print(highlight(header))
    print("-" * 55)

    # =========================
    # ITEMS LIST
    # =========================
    for i, (item_name, data) in enumerate(items_list, 1):
        item = data["item"]
        qty = data["quantity"]

        base_name = item_name

        if hasattr(item, "damage"):
            base_name += f" ({item.damage} dmg)"

        # PAD FIRST (no colors)
        col_index = pad(str(i), 4)
        col_item = pad(base_name, 30)
        col_qty = pad(f"x{qty}", 6)

        # COLOR LAST
        print(
            highlight(col_index) +
            name(col_item) +
            highlight(col_qty)
        )

    print("-" * 55)
    print(f"Gold: {highlight(hero.gold)}")

    # =========================
    # SELECTION
    # =========================
    choice = input(
        f"\nSelect item number {danger('exit')}:\n>> "
    ).strip().lower()

    if choice == "exit":
        return

    if not choice.isdigit():
        print(danger("Invalid input."))
        return

    index = int(choice) - 1

    if index < 0 or index >= len(items_list):
        print(danger("Invalid selection."))
        return

    item_name, item_data = items_list[index]
    item = item_data["item"]

    print(f"\nSelected: {name(item.name)}")

    # =========================
    # ACTION MENU
    # =========================
    if hasattr(item, "damage"):
        action = input(f"{highlight('(equip / back)')} >> ").strip().lower()
    else:
        action = input(f"{highlight('(use / back)')} >> ").strip().lower()

    if action == "back":
        return

    # =========================
    # USE ITEM
    # =========================
    if action == "use":

        if hasattr(item, "damage"):
            print(danger("You can't use a weapon."))
            return

        if "health" in item.name.lower():
            restore = 50 if "greater" in item.name.lower() else 25
            hero.health += restore
            print(highlight(f"✔ Restored {restore} HP"))

        elif "mana" in item.name.lower():
            restore = 50 if "greater" in item.name.lower() else 25
            hero.mana += restore
            print(highlight(f"✔ Restored {restore} Mana"))

        else:
            print(danger("This item can't be used."))
            return

        item_data["quantity"] -= 1
        if item_data["quantity"] <= 0:
            del hero.inventory[item_name]

    # =========================
    # EQUIP ITEM
    # =========================
    elif action == "equip":

        if not hasattr(item, "damage"):
            print(danger("This item can't be equipped."))
            return

        old_weapon = hero.weapon
        hero.weapon = item

        print(highlight(f"✔ Equipped {item.name}"))

        item_data["quantity"] -= 1
        if item_data["quantity"] <= 0:
            del hero.inventory[item_name]

        if old_weapon:
            if old_weapon.name in hero.inventory:
                hero.inventory[old_weapon.name]["quantity"] += 1
            else:
                hero.inventory[old_weapon.name] = {
                    "item": old_weapon,
                    "quantity": 1
                }

    else:
        print(danger("Invalid action."))


# =========================
# ADD ITEM (FIXED SAFELY)
# =========================

def add_item(item, hero):
    if item is None:
        print(danger("No loot dropped."))
        return

    if item.name in hero.inventory:
        hero.inventory[item.name]["quantity"] += 1
    else:
        hero.inventory[item.name] = {
            "item": item,
            "quantity": 1
        }

    print(highlight(f"+ Obtained {item.name}"))