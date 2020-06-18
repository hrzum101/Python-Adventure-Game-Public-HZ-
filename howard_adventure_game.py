import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print("please make a valid choice.\n")
    return response


def intro(rand_monster):
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + rand_monster + " is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)"
                " dagger.\n")


def house(items, rand_monster):
    print_pause("You approach the door of the house.")
    print_pause("You are about to kock when the door opens and out steps a "
                + rand_monster + ".")
    print_pause("Eep! This is the " + rand_monster + "'s house!")
    print_pause("The " + rand_monster + " attacks you!")
    if "sword" in items:
        user_choice = valid_input("Would you like to (1) fight or "
                                  "(2) run away?\n", "1", "2")
        if user_choice == '1':
            fight(items, rand_monster)
        elif user_choice == '2':
            field(items, rand_monster)
    else:
        print_pause("You feel a bit under-prepared for this, what with only "
                    "having a tiny dagger.")
        user_choice = valid_input("Would you like to (1) fight or "
                                  "(2) run away?\n", "1", "2")
        if user_choice == '1':
            fight(items, rand_monster)
        elif user_choice == '2':
            field(items, rand_monster)


def cave(items, rand_monster):
    print_pause("You peer cautiously into the cave.")
    if "sword" in items:
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword"
                    " with you.")
        items.append("sword")
    print_pause("You walk back out to the field.\n")
    choice(items, rand_monster)


def fight(items, rand_monster):
    if "sword" in items:
        print_pause("As the " + rand_monster + " moves to attack, you "
                    "unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand as "
                    "your brace yourself for the attack.")
        print_pause("But the " + rand_monster + " takes one look at your "
                    "shiny new toy and runs away!")
        print_pause("You have rid the town of the " + rand_monster +
                    ". You are victorious!")
    else:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the " + rand_monster +
                    ".")
        print_pause("you have been defeated!")
    play_again()


def field(items, rand_monster):
    print_pause("You run back into the field. Luckily, you don't seem to have"
                " been followed.\n")
    choice(items, rand_monster)


def choice(items, rand_monster):
    print_pause("Enter 1 to knock on the door of the house")
    print_pause("Enter 2 to peer into the cave")
    print_pause("What would you like to do?\n")
    user_choice = valid_input("(Please enter 1 or 2).\n", "1", "2")
    if user_choice == '1':
        house(items, rand_monster)
    elif user_choice == '2':
        cave(items, rand_monster)


def play_again():
    response = valid_input("Would you like to play again? (y/n)\n", "n", "y")
    if "n" in response:
        print_pause("Thanks for playing! See you next time.")
    if "y" in response:
        print_pause("Excellent! Restarting the game ...")
        play_game()


def play_game():
    items = []
    monsters = ['Ogre', 'Goblin', 'Tax Collector']
    rand_monster = random.choice(monsters)
    intro(rand_monster)
    choice(items, rand_monster)


play_game()
