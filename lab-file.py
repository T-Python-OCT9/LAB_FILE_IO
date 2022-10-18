'''## Using what you learned about Python File I/O , we want to make a progeram called To-Do List , this program should do the following:
- Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
- If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
- If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no. 
- If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
- Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"
'''

while (True):
    user_input=''
    print("Helllo, do you want to add a new To-Do item?answer y for yes and n for no exit to end:")
    user_input=input("\n")
    if user_input=='y':
        file = open("to_do.txt", "a", encoding="utf-8")
        file.write("*"+input("please enter your to do task:\n")+"\n")
        file.close()
    if user_input=='n':
        user_input=input("do you want to list your To-Do items ? answer y for yes and n for no. ")
        if user_input=='y':
            file = open("to_do.txt", "r", encoding="utf-8")
            content = file.read()
            print(content)
            file.close()
    if user_input=="exit":
        print("thank you for using the To-Do program, come back again soon^_^")
        break
    if user_input!='n' and user_input!='y':
        print("please enter valid value!")




