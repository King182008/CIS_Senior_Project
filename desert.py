def desertIntro(hero):
    from utils import slow_print
    slow_print("You emerge on the otherside of the forest and almost instantly are hit with a wave of heat.")
    slow_print("In the distace you see a small collection of crumbled buildings.")
    slow_print("As you approach you see a collection of goblins inspecting a large stair case down into the center of the desert.")

def desertInteract(hero, place):
    from utils import actions
    from utils import slow_print
    if not hero.flags.get("desert_interact_seen", False):
        slow_print("The staircase awaits you.")
        slow_print("It seems endless, a dim merky aura emits from the entrance")
        hero.flags["desert_interact_seen"] = True

    while True:
        action = input("What would ou like to do (Descend or Exit)")

        if action.lower() == "descend":
            if "Goblin Tooth" in hero.inventory:
                slow_print("You desend into the Desert Dugeon(Feature Not added yet)")
                break
            else:
                slow_print("You must kill a goblin before entering the dungeon")
                break
        elif action.lower() == "exit":
            break
        else:
            slow_print("Invalid Action")