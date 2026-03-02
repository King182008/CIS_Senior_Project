import characterCreation
import shop
import travel
import combat

if __name__ == "__main__":
    currentPlace = travel.currentPlace

    while True:
        action = input("What would you like to do? (Shop, Travel, Save or Stop) ")
        if action.lower() == "shop":
            shop.display_shop(currentPlace, characterCreation.hero)
        elif action.lower() == "travel":
            currentPlace = travel.travel(currentPlace)
        elif action.lower() == "save":
            slot = characterCreation.choose_slot()
            characterCreation.save(slot)
        elif action.lower() == "combat":
            enemy = combat.Enemies[currentPlace][0]  # Get the first enemy for the current location
            combat.display_enemy(enemy)
        elif action.lower() == "stop":
            break