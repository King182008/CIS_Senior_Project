import characterCreation

class Item:
    def __init__(self, name):
        self.name = name

class Enemy:
    def __init__(self, name, health, attack, gold, loot):
        self.name = name
        self.health = health
        self.attack = attack
        self.gold = gold
        self.loot = loot

    def take_damage(self, damage):
        self.health -= damage

# Factory function to create fresh enemy instances
def create_enemy(enemy_type):
    if enemy_type == "Rat":
        return Enemy("Rat", 10, 2, 5, Item("Rat Tail"))
    elif enemy_type == "Goblin":
        return Enemy("Goblin", 20, 5, 10, Item("Goblin Tooth"))
    elif enemy_type == "Troll":
        return Enemy("Troll", 50, 10, 25, Item("Troll Hide"))
    elif enemy_type == "Locust Swarm":
        return Enemy("Locust Swarm", 30, 7, 15, Item("Locust Wing"))
    elif enemy_type == "Dragon":
        return Enemy("Dragon", 100, 20, 50, Item("Dragon Scale"))

# Dictionary mapping regions to enemy types (strings)
Enemies = {
    "forest": ["Rat"],
    "desert": ["Goblin"],
    "mountains": ["Troll"],
    "swamp": ["Locust Swarm"],
    "volcano": ["Dragon"]
}

def display_enemy(enemy, hero):
    print(f"\nYou encounter a {enemy.name}!")
    print(f"Health: {enemy.health}")
    print(f"Attack: {enemy.attack}")

    while enemy.health > 0:
        action = input("Do you want to (Attack or Run)? ").strip().lower()

        if action == "attack":
            damage = hero.strength
            if hasattr(hero, "weapon") and hero.weapon is not None:
                damage += hero.weapon.damage

            print(f"\nYou attack the {enemy.name} for {damage} damage!")
            enemy.take_damage(damage)

            
            if enemy.health > 0:
                hero.health -= enemy.attack
                print(f"You take {enemy.attack} damage. Your health is now {hero.health}.")

                if hero.health <= 0:
                    print("You have been defeated! Game Over.")
                    return "dead"

        elif action == "run":
            print("You run away safely!")
            return "ran"

        else:
            print("Invalid action. Please choose 'Attack' or 'Run'.")

    print(f"\nVictory! {enemy.name} has been defeated!")
    hero.gold += enemy.gold
    hero.inventory.append(enemy.loot)
    print(f"You gain {enemy.gold} gold and loot: {enemy.loot}.")