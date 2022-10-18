'''
Using what you learned about Python File I/O , we want to make a progeram called To-Do List , this program should do the following:
'''
open('to_do.txt', 'a', encoding='utf-8')
to_do_file = open('to_do.txt', 'r+', encoding='utf-8')
user_input: str = ''
list_input: str = ''
while user_input.upper() != 'EXIT':
    # Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
    user_input = input(
        '> Do you want to add a new To-Do item? (Y or N) or type (EXIT) ')
    if user_input.upper() == 'Y':
        # If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
        to_do_item = f'{input(" > Type your new To-Do item: ")}\n'
        to_do_file.write(to_do_item)
    elif user_input.upper() == 'N':
        # If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no.
        list_input = input(
            " > Do you want to list your To-Do items ? (Y or N) or type (EXIT) ")
        if list_input.upper() == 'Y':
            # If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
            to_do_file.seek(0)
            print(to_do_file.read())
        else:
            user_input = ''
else:
    # Then return again to ther first question and ask again, you coninue this untill the user types in "exit" ,
    # then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"
    print("Thank you for using the To-Do program, Come back again soon!")
