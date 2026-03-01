import characterCreation
import shop
import travel

if __name__ == "__main__":
    currentPlace = travel.currentPlace

    while True:
        action = input("What would you like to do? (Shop, Travel or Stop) ")
        if action.lower() == "shop":
            shop.display_shop(currentPlace, characterCreation.hero)
        elif action.lower() == "travel":
            currentPlace = travel.travel(currentPlace)
        elif action.lower() == "stop":
            break