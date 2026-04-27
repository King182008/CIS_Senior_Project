from utils import slow_print
from utils import actions

def ForestIntro(hero):
    slow_print("... ... ...")
    slow_print("Mother! Come! Quick!")
    slow_print(f"{hero.name} is waking up.")
    slow_print("Good Morning Darling. I'm glad to see you're finally awake.")
    slow_print("It's Been 100 years since the Great Blast and you were the only survior from your village.")
    slow_print("The Horror's creation affected much of the world.")
    slow_print("Many Beasts have sprouted up though the years")
    slow_print("The Dragons currently wreaking havok in the mountians and volcano")
    slow_print("We need your help hero, Good luck!")
    actions(hero)