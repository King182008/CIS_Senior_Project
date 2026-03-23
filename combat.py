import characterCreation

class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

class Enemy:
    def __init__(self, name, health, attack, gold, xp, loot):
        self.name = name
        self.health = health
        self.attack = attack
        self.gold = gold
        self.xp = xp
        self.loot = loot

    def take_damage(self, damage):
        self.health -= damage

# Factory function to create fresh enemy instances
def create_enemy(enemy_type):
    if enemy_type == "Rat":
        return Enemy("Rat", 10, 2, 5, 5, Item("Rat Tail"))
    elif enemy_type == "Goblin":
        return Enemy("Goblin", 20, 5, 10, 10, Item("Goblin Tooth"))
    elif enemy_type == "Troll":
        return Enemy("Troll", 50, 10, 25, 25, Item("Troll Hide"))
    elif enemy_type == "Locust Swarm":
        return Enemy("Locust Swarm", 30, 7, 15, 30, Item("Locust Wing"))
    elif enemy_type == "Dragon":
        return Enemy("Dragon", 100, 20, 50, 200, Item("Dragon Scale"))
    elif enemy_type == "Cuthulu":
        return Enemy("Cuthulu", 200, 30, 100, 500, Item("Cuthulu's Eye"))

# Dictionary mapping regions to enemy types
Enemies = {
    "forest": ["Rat"],
    "desert": ["Goblin"],
    "mountains": ["Troll"],
    "swamp": ["Locust Swarm"],
    "volcano": ["Dragon"],
    "void": ["Cuthulu"]
}

spells = {
    "heal": {"name": "Heal", "damage": 0, "heal": 20, "Mana": 20},
    "fireball": {"name": "FireBall", "damage": 30, "Mana": 50},
    "crash": {"name": "Crash", "damage": 25, "Mana": 35},
    "poison cloud": {"name": "Poison Cloud", "damage": 15, "Mana": 15}
}

def display_enemy(enemy, hero):
    print(f"\nYou encounter a {enemy.name}!")
    print(f"Health: {enemy.health}")
    print(f"Attack: {enemy.attack}")

    while enemy.health > 0:
        action = input("Do you want to (Attack, Spell or Run)? ").strip().lower()

        if action == "attack" or action == "1":
            damage = hero.strength
            if hasattr(hero, "weapon") and hero.weapon is not None:
                damage += hero.weapon.damage

            print(f"\nYou attack the {enemy.name} for {damage} damage!")
            enemy.take_damage(damage)

            print(f"You regained 5 mana. You know have {hero.mana} mana.")
            hero.mana += 5

            
            if enemy.health > 0:
                hero.health -= enemy.attack
                print(f"You take {enemy.attack} damage. Your health is now {hero.health}.")

                if hero.health <= 0:
                    print("You have been defeated! Game Over.")
                    return "dead"

        elif action == "spell" or action == "2":
            weapon_name = hero.weapon.name.lower()

            # Always ensure heal exists
            hero.spellList.add("heal")

            # Add weapon-based spells (no duplicates automatically)
            if "fire" in weapon_name:
                hero.spellList.add("fireball")
            elif "water" in weapon_name:
                hero.spellList.add("crash")
            elif "poison" in weapon_name:
                hero.spellList.add("poison cloud")

            print("You can cast:", list(hero.spellList))  # convert to list for display

            spell_choice = input("Which spell do you want to cast? ").strip().lower()

            if spell_choice in hero.spellList:
                spell = spells[spell_choice]

                if hero.mana - spell["Mana"] < 0:
                    print("Not enough mana to cast that spell.")
                    continue

                if "heal" in spell:
                    heal_amount = spell["heal"] + hero.intelligence
                    hero.health += heal_amount
                    print(f"You cast {spell['name']} and restore {heal_amount} health!")
                elif "damage" in spell:
                    damage = spell["damage"] + hero.intelligence
                    print(f"You cast {spell['name']} and deal {damage} damage to the {enemy.name}!")
                    enemy.take_damage(damage)

                hero.mana -= spell["Mana"]
                print(f"You have {hero.mana} mana left.")

                if enemy.health > 0:
                    hero.health -= enemy.attack
                    print(f"You take {enemy.attack} damage. Your health is now {hero.health}.")

                if hero.health <= 0:
                    print("You have been defeated! Game Over.")
                    return "dead"

            else:
                print("You don't know that spell.")

                

        elif action == "run" or action == "3":
            print("You run away safely!")
            return "ran"

        else:
            print("Invalid action. Please choose 'Attack', 'Spell' or 'Run'.")

    print(f"\nVictory! {enemy.name} has been defeated!")
    hero.gold += enemy.gold
    from inventory import add_item
    add_item(enemy.loot, hero)
    print(f"You gain {enemy.gold} gold and loot: {enemy.loot}.")
    gain_xp(hero, enemy.xp)

def gain_xp(hero, amount):
    hero.xp += amount
    print(f"You gained {amount} XP!")

    while hero.xp >= hero.xp_to_next_level:
        print(f"Congratulations! You leveled up to level {hero.level}!")

        level_option = input("Choose an attribute to increase: (1) Strength, (2) Intelligence, (3) Agility: ").strip()
        if level_option == "1":
            hero.strength += 1
            print("Strength increased!")
        elif level_option == "2":
            hero.intelligence += 1
            print("Intelligence increased!")
        elif level_option == "3":
            hero.agility += 1
            print("Agility increased!")
        else:
            print("Invalid choice. No attribute increased.")

        hero.xp -= hero.xp_to_next_level
        hero.level += 1
        hero.xp_to_next_level = 50 * (hero.level ** 2)  # Or whatever formula you choose