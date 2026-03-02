import characterCreation
import shop

def show_inventory():
    hero = characterCreation.hero

    if not hero.inventory:
        print("Your inventory is empty.")
        return

    print("\nYour Inventory:")
    for i, item in enumerate(hero.inventory, start=1):
        if isinstance(item, shop.ShopWeapon):
            print(f"{i}. {item.name} (Weapon, Damage: {item.damage})")
        else:
            print(f"{i}. {item.name} (Item)")

    choice = input("\nDo you want to use or equip an item? (use/equip/exit) ").strip().lower()
    if choice == "exit":
        return

    item_name = input("Enter the name of the item: ").strip().lower()

    for item in hero.inventory:
        if item.name.lower() == item_name:
            # ---------- USE ITEM ----------
            if choice == "use":
                if isinstance(item, shop.ShopWeapon):
                    print("That item cannot be used.")
                    return

                # Determine effect based on item name
                if "health" in item.name.lower():
                    if "greater" in item.name.lower():
                        restore = 50
                    else:
                        restore = 25
                    hero.health += restore
                    print(f"You used {item.name} and restored {restore} health. Current health: {hero.health}")

                elif "mana" in item.name.lower():
                    if "greater" in item.name.lower():
                        restore = 50
                    else:
                        restore = 25
                    hero.mana += restore
                    print(f"You used {item.name} and restored {restore} mana. Current mana: {hero.mana}")

                # Remove used item
                hero.inventory.remove(item)
                return

            # ---------- EQUIP ITEM ----------
            elif choice == "equip":
                if isinstance(item, shop.ShopWeapon):
                    hero.weapon = item
                    print(f"You equipped {item.name}.")
                    return
                else:
                    print("That item cannot be equipped.")
                    return

    else:
        print(f"No item named '{item_name}' found in your inventory.")