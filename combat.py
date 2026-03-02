import characterCreation

class Enemy():
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} has {self.health} health remaining.")

Rat = Enemy("Rat", 10, 2)
Goblin = Enemy("Goblin", 20, 5)
Troll = Enemy("Troll", 50, 10)
Locust_Swarm = Enemy("Locust Swarm", 30, 7)
Dragon = Enemy("Dragon", 100, 20)

Enemies = {
    "forest": [Rat],
    "desert": [Goblin],
    "mountains": [Troll],
    "swamp": [Locust_Swarm],
    "volcano": [Dragon]
}

def display_enemy(enemy):
    print(f"\nYou encounter a {enemy.name}!")
    print(f"Health: {enemy.health}")
    print(f"Attack: {enemy.attack}")

    while enemy.health > 0:
        action = input("Do you want to (Attack or Run)? ").strip().lower()
        if action == "attack":
            damage = characterCreation.hero.weapon.damage  # Use player's attack power
            enemy.take_damage(damage)
            if enemy.health > 0:
                characterCreation.hero.health -= enemy.attack
                print(f"You take {enemy.attack} damage. Your health is now {characterCreation.hero.health}.")
            if characterCreation.hero.health <= 0:
                print("You have been defeated! Game Over.")
                break
        elif action == "run":
            print("You run away safely!")
            break
        elif enemy.health <= 0:
            print(f"Victory! {enemy.name} has been defeated!")
            break
        else:
            print("Invalid action. Please choose 'Attack' or 'Run'.")