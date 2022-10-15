# Automatic String Manipulation Utility

# Task 1.
def user_name(name):  # function to get the username
    username = (name.strip().title())
    return username


def get_user_input(userinput):  # function to get the string from the user
    global temp_user_input
    print(welcome_message)
    print("\nTo get started, input a string of your choice. \n"
          "EX: 'Hello world, I am Coding'"
          )
    ending_loop = 0
    while ending_loop == 0:  # loop to validate that the user is using at least 15 characters
        temp_user_input = str(input(userinput))
        if temp_user_input == "":  # if the user did not enter anything
            print("You did not enter anything, try again.")
        elif len(temp_user_input) < 15:  # code to make sure that the user enter at least 15 chr
            print("Make sure your string is at least 15 characters long, try again.")
        else:  # when all has been checked, then prints the users input
            print(f"Your string: {temp_user_input}")
            ending_loop += 1
            temp_user_input = temp_user_input.lower()

    return temp_user_input


# Task 2
def menu():  # function to show all the menu options available
    menu_list = ['white-space counter', 'non white-space counter',
                 'word counter', 'word swapper', 'white space corrector', 'Quit']
    for _, items in enumerate(menu_list, start=1):
        print(f"Menu options: {_} - {items}")


def white_space(string):  # function to count the white space in the users string
    count = 0
    for i in string:
        if i.isspace() == True:
            count += 1
    return count


def nonwhite_space(string):  # function to count the non-white space in the string
    count = 0
    for i in string:
        if i.isspace() == False:
            count += 1
    return count


def fix_space(string):  # function to check and fix for unnecessary white space
    for i in string:
        if i.isspace() == True:
            i = ""
    return string


def num_words(string):
    return len(string.split())  # split function splits the string into substring of just the words excluding whitespace


def flag_word(string, flag, safe):  # function to swap words
    new_string = string.replace(flag, safe)
    return new_string


def instances(word, string):  # function to check the instance a word has been swapped
    list(string)

    return string.count(word)


def remove_white(string):  # function to remove white space
    return " ".join(string.split())


def menu_choice(input_string):  # function for all menu choice activities
    menu()
    menu_list_number = ['1', '2', '3', '4', '5', '6']  # user will enter numbers corresponding to the menu option
    print("\nEnter the number option. \n\""
          "EX| '1'  Which counts for white space in your string ")
    user_menu = str(input("Enter: "))

    counter = 0
    while counter == 0:  # loop to keep the user asking incase an invalid option was inputted
        if user_menu not in menu_list_number:
            user_menu = str(input("Option not valid, Try again: "))

        elif user_menu == menu_list_number[0]:  # when user selects  option 1
            print("White space counter:", white_space(input_string))
            user_menu = str(input("Check for another option: "))
        elif user_menu == menu_list_number[1]:  # when user selects option 2
            print("Non white space counter:", nonwhite_space(input_string))
            user_menu = str(input("Check for another option: "))
        elif user_menu == menu_list_number[2]:  # when user selects option 3
            print("Number of words in your string:", num_words(input_string))
            user_menu = str(input("Check for another option: "))
        elif user_menu == menu_list_number[3]:  # when user selects option 4

            counting = 0
            while counting == 0:

                counting = 1
                print(f"This is your string: {input_string}")
                words_swap_num = int(input("How many words are you planing to swap? "))  # to see how man words swapping

                for i in range(words_swap_num):  # loop based on how many words the user is planning to swap
                    ask_flag = input("Choose a word from your string to swap: ")  # word user is replacing
                    instances_user = instances(ask_flag, input_string)  # how many times that word is in the string
                    change_word = input("Choose word to change: ")  # word the user wants to swap to.
                    new_string = flag_word(input_string, ask_flag,
                                           change_word)  # the new string stored with the swap words intact
                    print(f"'{ask_flag}' was removed {instances_user} times.")
                    print("New string:", new_string)
                    input_string = new_string
                user_menu = str(input("Check for another option: "))

        elif user_menu == menu_list_number[4]:
            print(remove_white(user_input))
            user_menu = str(input("Check for another option: "))
        elif user_menu == menu_list_number[5]:
            print("Exit")
            counter = 2


get_name = input("What is your name: ")

welcome_message = f"Hey {user_name(get_name)}, Welcome to Automatic String Manipulation Utility \n" \
                  f"This software is to help Manipulate your strings of your choosing."

user_input = get_user_input("Enter a string: ")

menu_choice(user_input)
