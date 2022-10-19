open('to_do.txt', 'a', encoding='utf-8')
to_do_file = open('to_do.txt', 'r+', encoding='utf-8')
user_input: str = ''
list_input: str = ''
while user_input.upper() != 'EXIT':

    user_input = input(
        '> Do you want to add a new To-Do item? (Y or N) or type (EXIT) ')
    if user_input.upper() == 'Y':
        to_do_item = f'{input(" > Type your new To-Do item: ")}\n'
        to_do_file.write(to_do_item)
    elif user_input.upper() == 'N':
        list_input = input(" > Do you want to list your To-Do items ? (Y or N) or type (EXIT) ")
        if list_input.upper() == 'Y':
            to_do_file.seek(0)
            print(to_do_file.read())
        else:
            user_input = ''
else:
    print("Thank you for using the To-Do program, Come back again soon!")