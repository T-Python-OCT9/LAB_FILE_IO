'''
To-Do List Program
'''
#--------------------- To-Do Function --------------------------
def To_Do(answer : str):
    #  you coninue this untill the user types in "exit" ,
    #  then you exit the program. and print to the user
    #  "thank you for using the To-Do program, come back again soon"
    while answer != "exit":
        # - If the user answers yes , then ask the user to type in his new To-Do item .
        #  Then save that To-Do item inside the a file to_do.txt on a new line.
        if answer == "y":
            ToDo_file = open("to_do.txt", "a", encoding="utf-8")
            item = input("Type whatever you want to add on your new TO-DO item! \n")
            ToDo_file.write(item + "\n")
            ToDo_file.close()
            answer= input("Would you like to add a new To-Do item? answer by 'y' for yes and 'n' for no -> ")
        # - If the user answers no, then ask the user : do you want to list your To-Do items ? 
        # answer "y" for yes and "n" for no. 
        if answer == "n":
                item = input("Do you want to list your To-Do items ? answer 'y' for yes and 'n' for no -> ")
                if item == "y":
                    # - If the user answers yes for reading his To-Do list ,
                    #  then print a list of the To-Do items one item per line.
                    ToDo_file = open("to_do.txt", "r", encoding="utf-8")
                    items = ToDo_file.readlines()
                    ToDo_file.close()
                    for item_ in items:
                        print(item_)
                elif item == "n":
                    # - Then return again to ther first question and ask again,
                    # To_Do(answer)
                    answer= input("Would you like to add a new To-Do item? answer by 'y' for yes and 'n' for no ")

    else:
        print("thank you for using the To-Do program, come back again soon")
        
#---------------------------------------------------------------------------------

print("HEY! WELCOME TO OUR TO-DO-LIST PROGRAM! ")
# - Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
answer= input("Would you like to add a new To-Do item? answer by 'y' for yes and 'n' for no ")
To_Do(answer)
