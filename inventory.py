import characterCreation
import shop
import combat

def show_inventory(hero):

    if not hero.inventory:
        print("\nYour inventory is empty.")
        print(f"Gold: {hero.gold}")
        return

    print("\nYour Inventory:")
    for i, (item_name, data) in enumerate(hero.inventory.items(), 1):
        print(f"{i}. {item_name} x{data['quantity']}")

    choice = input("\nDo you want to use or equip an item? (use/equip/exit) ").strip().lower()
    if choice == "exit":
        return

    item_name = input("Enter the name of the item: ").strip()

    if item_name not in hero.inventory:
        print(f"No item named '{item_name}' found in your inventory.")
        return

    item_data = hero.inventory[item_name]
    item = item_data["item"]

    # ---------- USE ITEM ----------
    if choice == "use":

        if isinstance(item, shop.ShopWeapon):
            print("That item cannot be used.")
            return

        if "health" in item.name.lower():
            restore = 50 if "greater" in item.name.lower() else 25
            hero.health += restore
            print(f"You used {item.name} and restored {restore} health. Current health: {hero.health}")

        elif "mana" in item.name.lower():
            restore = 50 if "greater" in item.name.lower() else 25
            hero.mana += restore
            print(f"You used {item.name} and restored {restore} mana. Current mana: {hero.mana}")

        # Reduce quantity
        item_data["quantity"] -= 1
        if item_data["quantity"] <= 0:
            del hero.inventory[item_name]

    # ---------- EQUIP ITEM ----------
    elif choice == "equip":

        if isinstance(item, shop.ShopWeapon):
            hero.weapon = item
            print(f"You equipped {item.name}.")
        else:
            print("That item cannot be equipped.")

def add_item(item, hero):
    if item.name in hero.inventory:
        hero.inventory[item.name]["quantity"] += 1
    else:
        hero.inventory[item.name] = {
            "item": item,
            "quantity": 1
        }