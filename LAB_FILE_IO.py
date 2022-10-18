'''

## Using what you learned about Python File I/O , we want to make a progeram called To-Do List , this program should do the following:

- Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
- If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
- If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no. 
- If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
- Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"

'''
# Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
new_item = str (input("do you want to add a new To-Do item?   'y' for yes and 'n' for no."))

# If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.

while new_item == "exit" or new_item == "n" or new_item == "y":
    new_item = str (input("do you want to add a new To-Do item?   'y' for yes and 'n' for no."))

    if new_item == exit :
        print("thank you for using the To-Do program, come back again soon")
        break   
    if new_item == "y" :
       toDo_item = str (input(" type in his new To-Do item ? ") )
       if toDo_item == "w":
        file = open("to_do.txt","W", encoding="utf-8")
        the_w = str(input(" what do you wint to write ? "))
        file.write(the_w) 
        file.close() 
       if toDo_item == "r":
        file = open("to_do.txt","r", encoding="utf-8")
        file.read()
        file.seek(0)
        content = file.read()
        print(content) 
        file.close()  
        if toDo_item == "a":
         file = open("to_do.txt","a", encoding="utf-8")
         the_w = str(input(" what do you wint to write ? "))
         file.seek(0)
         file.write(the_w) 
         file.close() 
        
      #If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no.
    elif new_item=="n":
      listToDo = str(input("do you want to list your To-Do items"))
      file = open("to_do.txt","a", encoding="utf-8")
      file.seek(0)
      print(file.readlines())
    
#- Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"


    
     


