import os 

''''
A = ''

a = 'yes'

B = 'txt'
c = ''

def Do():
    A = input('do you want to add a new To-Do item? ' )

    if A == a:
        A1 = input('plase type the new To-Do item ' )
        c  = input('Enter the name of the ' )
        
        if A1 == f"{c}.{A1}":
            file = open(f"{A1}.txt",'r+')


'''
print('Welcome to our app')
    
while(True):

    user_answer = input('do you want to add a new To-Do item? ( n ) for no ( y ) for Yes  ' )

    if user_answer == 'y':
        user_note = input('Type your item\n' )
        file = open('to_do.txt', 'a', encoding='utf-8')
        file.write(user_note+ "\n")
        file.close()

    elif user_answer == 'n':
        list_items = input('do you want list show your items? ')
        if list_items == 'y':
            file = open('to_do.txt', 'a', encoding='utf-8')
            content = file.readlines()
            for note in content:
              print(note)

    elif user_answer == 'exit':
        print('Good bye')
        break


            



