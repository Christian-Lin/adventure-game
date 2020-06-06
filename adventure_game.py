import time
import random


def pause_print(text):
    print(text)
    time.sleep(2.5)


def intro():
    pause_print("You wake up on an empty field, with basic \n"
                "equipment and a wooden club.")
    pause_print("In front of you stands a sign:")
    print("")
    pause_print("'If you want to leave this reality, \n"
                "you will have to slay the dragon atop the hill.'")
    print("")
    pause_print("You look around, and you see:\n"
                "- A nearby town. \n"
                "- Some abandoned barracks. \n"
                "- An ominous dungeon at the base of a hill.\n"
                "- And a massive hill, where the dragon lives.\n")
    pause_print("Where would you like to go?")


def town(items):
    pause_print("You travel to the town.")
    if "sword" in items:
        pause_print("Everyone seems busy. There is nothing to do here.")
    elif "sword" not in items:
        pause_print("A blacksmith catches your attention.\n")
        pause_print("The blacksmith greets you, and claims \n"
                    "that he can make you something \n"
                    "a lot better than a wooden club.")
        pause_print("But he will need the appropiate materials.\n")
        if "materials" in items:
            pause_print("You hand him the materials, \n"
                        "and a few hours later he \n"
                        "gives you a brand new sword!")
            items.append("sword")
        else:
            pause_print("Unfortunately, you don't seem to \n"
                        "have the necessary materials.\n")
    pause_print("Where would you like to go next?")
    locations(items)


def explore(items):
    exploring = ""
    exploring = input("Do you wish to continue exploring? "
                      "(1)Yes (2)No\n").lower()
    if exploring == "1":
        pause_print("You continue exploring.")
        pause_print("You stumble across a corpse.")
        pause_print("It seems like it has a chainmail on.")
        pause_print("You grab it and equip it. It feels sturdy and light!")
        pause_print("You exit the barracks.\n")
        pause_print("Where would you like to go next?")
        items.append("armor")
        locations(items)
    if exploring == "2":
        pause_print("You exit the barracks.\n")
        locations(items)


def fight1(items, creature):
    fightoptions1 = ""
    fightoptions1 = input("Do you wish to (1)fight or (2)flee?\n").lower()
    if fightoptions1 == "1":
        pause_print("You brace yourself.")
        pause_print(f"The {creature} charges at you.")
        pause_print("You dodge and smash its head!\n")
        pause_print(f"The {creature} has been defeated. \n"
                    "You spot a chest, and open it.\n")
        pause_print("You find some useful materials.")
        items.append("materials")
        explore(items)
    elif fightoptions1 == "2":
        pause_print("You run for your life. "
                    "You make it out of the barracks alive.")
        locations(items)
    else:
        pause_print("Please select one of the options.")
        fight1(items)


def barracks(items):
    creature = ""
    clist = ['skeleton', 'goblin', 'zombie', 'mummy']
    creature = random.choice(clist)
    if "materials" not in items:
        pause_print("You enter the barracks. While exploring, \n"
                    f"a {creature} appears from the dark!")
        fight1(items, creature)
    elif "materials" in items:
        pause_print("You have already been here.")
        if "armor" not in items:
            explore(items)
        else:
            pause_print("The barracks have been fully explored. \n"
                        "There is nothing left for you to do here.")
            pause_print("Where would you like to go next?")
            locations(items)


def play_again():
    repeat = ""
    repeat = input("Would you like to play again? (y/n)\n")
    if repeat == "y":
        play_game()
    elif repeat == "n":
        pause_print("Thank you for playing. "
                    "See you next time!")
    else:
        pause_print("Please type in 'y'(yes) or 'n'(no).")
        play_again()


def fight2(items, boss):
    fightoptions1 = ""
    fightoptions1 = input(f"Do you wish to (1)fight the {boss} or "
                          "(2)leave the dungeon?\n").lower()
    if fightoptions1 == "1":
        if "sword" in items:
            pause_print(f"The {boss} did not notice your presence.")
            pause_print("You sneak up to it and stab its heart!")
            pause_print(f"The {boss} has been defeated.")
            pause_print("You see a glowing greatsword resting \n"
                        "on the altar.")
            pause_print("You obtain the 'Draconis Greatsword'!")
            items.append("finalweapon")
            locations(items)
        elif "sword" not in items:
            pause_print(f"The {boss} did not notice your presence.")
            pause_print("You sneak up to it, and you deliver a \n"
                        "strong hit to the head!")
            pause_print("Unfortunately, the club was not enough \n"
                        f"to defeat the {boss}.")
            pause_print(f"Oh no! The {boss} crushed your skull.")
            pause_print("You have been defeated.")
            play_again()
    elif fightoptions1 == "2":
        pause_print("You sneak back out of the dungeon.")
        pause_print("Where would you like to go next?")
        locations(items)
    else:
        pause_print("Please select one of the options.")
        fight1(items)


def dungeon(items):
    boss = ""
    blist = ['minotaur', 'troll', 'ogre']
    boss = random.choice(blist)
    if "finalweapon" not in items:
        pause_print("You sneak into the dungeon. It seems small.")
        pause_print("You scout the place, and you spot an \n"
                    f"intimidating {boss}.")
        fight2(items, boss)
    elif "finalweapon" in items:
        pause_print("You have already defeated the dungeon's boss.\n"
                    "There is nothing left to do here.")
        pause_print("Where would you like to go next?")
        locations(items)


def hill(items):
    pause_print("You gather up the courage and start "
                "climbing the hill.")
    pause_print("You cannot see the dragon.")
    pause_print("The dragon swoops down from above!")
    if "armor" in items:
        pause_print("The tail hits you, knocking you down.")
        pause_print("Luckily, the chainmail protected you from \n"
                    "the hard blow to the chest.")
        if "finalweapon" in items:
            pause_print("The dragon blows fire on you.")
            pause_print("The 'Draconis Greatsword' protects you \n"
                        "from the fire with its divine magic!")
            pause_print("You swing the sword, sending a beam \n"
                        "that pierces the dragon.")
            pause_print("Congratulations! You are victorious. \n"
                        "You are now the 'Dragonslayer'!")
        elif "finalweapon" not in items:
            pause_print("The dragon blows fire on you.")
            pause_print("You are burnt to a crisp.")
            pause_print("You have been defeated!")
            play_again()
    elif "armor" not in items:
        pause_print("The tail hits you, sending you flying.")
        pause_print("You fall to your death.")
        pause_print("You have been defeated!")
        play_again()


def locations(items):
    prompt = ""
    print("(Please enter a number):")
    prompt = input(
        "1. The town\n"
        "2. The barracks\n"
        "3. The dungeon\n"
        "4. Climb the hill\n"
    ).lower()
    if prompt == "1":
        town(items)
    elif prompt == "2":
        barracks(items)
    elif prompt == "3":
        dungeon(items)
    elif prompt == "4":
        hill(items)
    else:
        locations(items)


def play_game():
    items = []
    intro()
    locations(items)


play_game()
