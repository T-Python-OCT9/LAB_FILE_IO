'''
# LAB_FILE_IO

## Using what you learned about Python File I/O , we want to make a progeram called To-Do List , this program should do the following:
- Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
- If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
- If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no. 
- If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
- Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"

'''
while(True):
    user_input = input("Do you want to add a new To-Do item? Use y for Yes n for No and Exit to exit the program ! ")
    if user_input == "y":
        user_new_item = input("Type in the new To-Do item : ")
        file = open("to_do.txt","a+", encoding=("utf-8"))
        file.write(f"\n {user_new_item}")
        print(file.read())
        file.close
    elif user_input == "n":
        user_ask_no = input("do you want to list your To-Do items ?")
        if user_ask_no == "y":
            file = open("to_do.txt","r", encoding=("utf-8"))
            print(file.readlines())
            file.close()
            continue
        else:
            print("Type exit to exit the program or ")
    elif user_input == "exit":
        print("thank you for using the To-Do program, come back again soon")
        break