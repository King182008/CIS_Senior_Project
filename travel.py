currentPlace = "forest"
placesBeen = {"forest": True,"desert": False,"mountains": False,"swamp": False,"volcano": False}

def travel(place):
    destinations = {"forest": ["desert", "mountains"],"desert": ["forest", "swamp"],"mountains": ["forest", "volcano"],"swamp": ["desert"],"volcano": ["mountains"]} 
    print("You're currently at the", place.title())
    print("You can travel to locations", [d.title() for d in destinations[place]])
    decision = input("Where would you like to go? ").strip().lower()
    if decision not in destinations[place]:
        print("You can't go there!")
        return place
    
    if placesBeen[decision] == True:
        reAsk = input("You've been here would you still like to go? (Yes or No) ")
        if reAsk.lower() == "yes":
            print("You traveled to", decision)
            return decision
        else: 
            return place
    else:
        print("You traveled to the", decision.title())
        placesBeen[decision] = True
        return decision
        
if __name__ == "__main__":
    while True:
        action = input("What would you like to do? (Travel or Stop) ")
        if action.lower() == "travel":
            currentPlace = travel(currentPlace)
        elif action.lower() == "stop":
            break