
def to_do():
    print('---WELCOME---')  
    while True:
        operation = input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no or 'exit' to break: ")
        if operation == 'y':
            write_to_file()  
        elif operation == 'n':
            read_from_file()
        elif operation == 'exit':
            print("Good Bey!")
            break
        else:
            print('This operation is not valid')

def write_to_file(): 
    note = input('type your note: ')
    file = open('TODO.txt', "a", encoding="utf-8")
    file.write(note + '\n')
    file.close()

def read_from_file(): 
    operation = input('do you want to list your To-Do items ? answer "y" for yes and "n" for no: ')
    if operation == 'y':
        file = open('TODO.txt', "r+", encoding="utf-8")
        content_lines = file.readlines()
        for index, line in enumerate(content_lines):
            print(f'{index} - {line}')
        file.close()
to_do()