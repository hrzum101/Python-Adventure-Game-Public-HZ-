import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print("I dont understand you.\n")
    return response


def intro(rand_shop):
    print_pause("You find yourself in the city and are tired")
    print_pause("Rumor has it that a " + rand_shop + " is "
                "somewhere around "
                "here, and is able to make you not tired")
    print_pause("In front of you is a coffee shop")
    print_pause("To your right is casino")
    print_pause("In your hand you hold you have $2 (but not enough)"
                " to buy yourself a Flat White with single origin"
                " espresso.\n")


def store(wallet, rand_shop):
    print_pause("You approach the door of the coffee shop")
    print_pause("You enter the coffee shop and the barista at "
                + rand_shop + " gives you a smug look.")
    print_pause("The barista passive agressively stares at you")
    if "money" in wallet:
        user_choice = valid_input("Would you like to (1) pay or "
                                  "(2) walk away?\n", "1", "2")
        if user_choice == '1':
            fight(wallet, rand_shop)
        elif user_choice == '2':
            street(wallet, rand_shop)
    else:
        print_pause("You feel a bit under-prepared for this, what with only "
                    "having a $2.")
        user_choice = valid_input("Would you like to (1) pay or "
                                  "(2) walk away?\n", "1", "2")
        if user_choice == '1':
            fight(wallet, rand_shop)
        elif user_choice == '2':
            street(wallet, rand_shop)


def casino(wallet, rand_shop):
    print_pause("You walk into the casino")
    if "money" in wallet:
        print_pause("You've been here before, and got what you needed. "
                    "Its better to walk away while you are up.")
    else:
        print_pause("You walk up to a slot machine")
        print_pause("You place your last $2 into the machine and bet MAX")
        print_pause("The slot machine makes alot of noise and music.")
        print_pause("You won $5!, just enough to get a Flat White")
        wallet.append("money")
    print_pause("You walk back out to the street.\n")
    choice(wallet, rand_shop)


def fight(wallet, rand_shop):
    if "money" in wallet:
        print_pause("As the barista at " + rand_shop + " is expecting you to "
                    "not have enough money, you do in-fact have enough.")
        print_pause("You hand the barista a fresh $5 bill from the casino.")
        print_pause("The barista takes your order of a Single Origin Flat"
                    " White.")
        print_pause("You recieve your newly concoted drink and are no longer"
                    " tired.")
    else:
        print_pause("You attempt to shove your $2 in their face.")
        print_pause("but $2 is not enough for what you want.")
        print_pause("You end up getting a dismal brewed cup of dark roast.")
        print_pause("you have been defeated because it tastes awful and burnt")
    play_again()


def street(wallet, rand_shop):
    print_pause("You run back into the street.")
    choice(wallet, rand_shop)


def choice(wallet, rand_shop):
    print_pause("Enter 1 to walk into the " + rand_shop + ("."))
    print_pause("Enter 2 to walk into the casino.")
    print_pause("What would you like to do?\n")
    user_choice = valid_input("(Please enter 1 or 2).\n", "1", "2")
    if user_choice == '1':
        store(wallet, rand_shop)
    elif user_choice == '2':
        casino(wallet, rand_shop)


def play_again():
    response = valid_input("Would you like to play again? (y/n)\n", "n", "y")
    if "n" in response:
        print_pause("bye")
    if "y" in response:
        print_pause("ok")
        play_game()


def play_game():
    wallet = []
    shop = ['BlueBottle', 'Samba Latte', 'Starbucks']
    rand_shop = random.choice(shop)
    intro(rand_shop)
    choice(wallet, rand_shop)


play_game()
