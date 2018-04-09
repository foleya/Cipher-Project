import os
import sys

from affine import Affine
from atbash import Atbash
from bifid import Bifid
from caesar import Caesar


def build_menu(menu):
    """
    Builds different kinds of menus
    
    Arg: Dictionary (includes menu type and options)
    Returns: Nothing, it just prints the menu.
    """
    print("{} Menu:".format(menu['type']))
    for number, option in menu['options'].items():
        print("{}: {}".format(number, option))


def get_menu_choice(menu):
    """
    Gets a user's choice from a menu
    
    Arg: Dictionary (includes menu type and options)
    Returns: String (user's selection from the menu's options)
    """
    choice = ''
    while choice == '':
        print("\nChoose an option by entering its menu number.")
        choice = str.lower(input('>'))

        # Return a valid choice, or prompt the user to try again.
        if choice in menu['options']:
            return menu['options'][choice]
        else:
            clear_screen()
            print(
                "'{}' is not a valid option. \nPlease enter"
                " a number 1-{}.\n".format(choice, len(menu['options']))
            )
            build_menu(menu)
            choice = ''


def clear_screen():
    """clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def cipher_program():
    """
    Encrypts/decrypts a message using a chosen cipher
    
    This program prompts the user to choose a cipher from a menu, then
    to choose whether they want to encrypt or decrypt a message using
    the chosen cipher.
    
    The program then asks the user to input a message, encrypts/decrypts the
    message, and prints that result.
    """
    chosen_cipher = ''
    chosen_action = ''
    cipher_menu = {
        'type': 'Cipher',
        'options': {
            '1': 'Affine',
            '2': 'Atbash',
            '3': 'Bifid',
            '4': 'Caesar',
            '5': 'Exit Program'
        }
    }
    action_menu = {
        'type': 'Action',
        'options': {
            '1': 'Encrypt',
            '2': 'Decrypt',
            '3': 'Exit Program'
         }
    }

    # Ask the user to choose a cipher.
    while chosen_cipher == '':

        # Build the cipher menu and get the user's cipher choice:
        build_menu(cipher_menu)
        chosen_cipher = get_menu_choice(cipher_menu)

        # Exit the program if the user chooses 'Exit Program'.
        if chosen_cipher == 'Exit Program':
            sys.exit()

    # If a valid cipher is chosen, ask if user wants to encrypt or decrypt.
    while chosen_action == '':
        clear_screen()

        # Build the action menu and get the user's action choice:
        # encryption or decryption.
        build_menu(action_menu)
        chosen_action = get_menu_choice(action_menu)

        # Exit the program if the user chooses 'Exit Program'.
        if chosen_action == 'Exit Program':
            sys.exit()

    # If a valid action is chosen prompt the user to enter a message
    # to encrypt/decrypt.
    clear_screen()
    print(
        "Enter the text you would like to {}, with the"
        " {} cipher:".format(chosen_action.lower(), chosen_cipher.lower())
    )
    users_message = str.upper(input('> '))

    # Create an instance of the user's chosen cipher, by using eval() to turn
    # the string (chosen_cipher) into a callable object.
    cipher = eval(chosen_cipher)()

    # Using that instance (cipher), call the method (encrypt/decrypt)
    # on the user's message, then print the result.
    if chosen_action == 'Encrypt':
        print(cipher.encrypt(users_message))
    if chosen_action == 'Decrypt':
        print(cipher.decrypt(users_message))

    # Then ask whether user is done using the program.
    print("\nWould you like to encrypt/decrypt another message? [Y,n]\n")
    if input('> ').lower() != "n":
        cipher_program()

if __name__ == '__main__':
    cipher_program()


