from utils import quest_board_menu
from utils import slow_print
from utils import actions

def ForestIntro(hero):
    slow_print("... ... ...")
    slow_print("Mother! Come! Quick!")
    slow_print(f"{hero.name} is waking up.")
    slow_print("Good Morning Darling. I'm glad to see you're finally awake.")
    slow_print("It's Been 100 years since the Great Blast and you were the only survior from your village.")
    slow_print("We've kept you alive with in hybernation with time magic.")
    slow_print("The Horror's creation affected much of the world.")
    slow_print("Many Beasts have sprouted up though the years")
    slow_print("The Dragons currently wreaking havok in the mountians and volcano")
    slow_print("We need your help hero, Good luck!")
    actions(hero)

def forestInteract(hero, place):
    if not hero.flags.get("forest_intro_seen", False):
        slow_print("You look around to see a vast clearing, bathed in soft golden light.")
        slow_print("At its center stands an enormous ancient tree, its trunk wider than a castle tower.")
        slow_print("Its leaves shimmer faintly, pulsing with lingering time magic.")
        slow_print("Elegant wooden structures spiral around the trunk, forming the home of the Elves.")
        slow_print("Elves move gracefully between platforms, their eyes occasionally glancing toward you with quiet curiosity.")
        slow_print("Beyond the clearing, a dense forest stretches endlessly, its depths dark and whispering.")
        slow_print("You feel it… something in the woods is watching.")
        slow_print("The Head Elf, Galadriel, stands nearby. She was the first to greet you upon awakening.")
        slow_print("")
        slow_print("Lore:")
        slow_print("This tree is known as the Heartroot, the last living anchor of ancient time magic.")
        slow_print("After the Great Blast, the Elves bound what remained of time itself into this tree.")
        slow_print("Without it, the world would have fallen completely into chaos.")
        slow_print("But the magic is fading… and something in the forest feeds on its power.")

        hero.flags["forest_intro_seen"] = True

    while True:
        action = input("What would you like to do (Talk, Quest, Lore, Exit): ").lower()

        if action == "talk" or action == "1":
            talkToGaladriel(hero)

        elif action == "quest" or action == "2":
            quest_board_menu(hero)

        elif action == "lore" or action == "3":
            hero.flags["forest_intro_seen"] = False
            forestInteract(hero, place)

        elif action == "exit":
            if not hero.flags.get("forest_outro_seen", False):
                slow_print("You step away from the Heartroot clearing, heading toward the edge of the forest.")
                slow_print("The air grows colder as the sounds of the Elves fade behind you.")
                slow_print("Whatever lies ahead… it won't be as safe as this place.")
                hero.flags["forest_outro_seen"] = True
                break
            else:
                break

        else:
            slow_print("That is not a valid action.")


def talkToGaladriel(hero):
    slow_print("You approach Galadriel. Her gaze is calm, but carries the weight of centuries.")
    slow_print("")
    slow_print("\"You have many questions,\" she says softly.")
    slow_print("\"And little time to ask them.\"")
    slow_print("")

    while True:
        choice = input("Ask about (Tree, Blast, Dragons, Leave): ").lower()

        if choice == "tree":
            slow_print("\"The Heartroot is older than memory,\" Galadriel explains.")
            slow_print("\"It binds the flow of time itself. Without it, past and present would collapse into chaos.\"")
            slow_print("\"But its power wanes. Something drains it from the shadows.\"")

        elif choice == "blast":
            slow_print("\"The Great Blast was no accident,\" she says grimly.")
            slow_print("\"It was the birth cry of the Horror.\"")
            slow_print("\"A being not of this world… or perhaps what remains of one.\"")
            slow_print("\"Your village stood at the epicenter. That is why you alone were… preserved.\"")

        elif choice == "dragons":
            slow_print("\"The Dragons were once guardians,\" Galadriel says.")
            slow_print("\"But the Blast twisted them.\"")
            slow_print("\"Now they rage endlessly, drawn to fire and ruin.\"")
            slow_print("\"If left unchecked, they will burn what little remains of this world.\"")

        elif choice == "leave":
            slow_print("\"Go then, hero,\" Galadriel says.")
            slow_print("\"Return if you seek guidance… or if you still draw breath.\"")
            break

        else:
            slow_print("Galadriel tilts her head slightly, not understanding your question")