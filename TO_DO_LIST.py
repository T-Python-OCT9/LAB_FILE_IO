def to_do():
    print('---WELCOME---')  # welcome massage
    file = open('TODO.txt', "w+", encoding="utf-8") # create a file
    while True:
        operation = input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no: ")
        if operation == 'y':
            note = input('type your note: ')
            file = open('TODO.txt', "a+", encoding="utf-8")
            note_plas = f'{note}\n' # to add note in a new line
            file.write(note_plas)
            file.close()
        elif operation == 'n':
            answer = input('do you want to list your To-Do items ? answer "y" for yes and "n" for no: ')
            if answer == 'y':
                file = open('TODO.txt', "r+", encoding="utf-8")
                content_lines = file.readlines()
                for line in content_lines:
                    print(f'The first item is: {line}')
                file.close()
        elif operation == 'exit':
            break
        else:
            print('This operation is not valid')
        
to_do()