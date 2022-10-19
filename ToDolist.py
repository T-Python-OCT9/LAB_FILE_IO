while True:
    User_Input = input("Welcome to Todo list app !, to countinue answer \"y\" if you want to exit the app write \"exit\" :\n ")
    if User_Input == 'y':
        user_notes = input("what To-Do note do you want to add?: \n ")
        file = open("TodoList.txt", "a", encoding="utf-8")
        file.write(user_notes + "\n")
        file.close()

    elif User_Input == 'n':
        user_todoList = input("do you want to list your To-Do list ?\n")
        if user_todoList =='y':
            file = open("TodoList.txt", "r", encoding="utf-8")
            content = file.readlines()
            
            for index, notes in enumerate(content):
                print(f"{index} - {notes}")
    elif User_Input == "exit":
        print("We're happy to help you , see you next time!") 
        break

'''
while True:
    user_input = input("Welcome to Todo list app !, to countinue answer \"y\" if you want to exit the app write \"exit\" :\n ")
    if user_input == "y":
        user_new_item = input("what To-Do note do you want to add?: \n ")
        file = open("TodoList.txt","a", encoding=("utf-8"))
        file.write(user_new_item  + "\n")
       
        file.close
    elif user_input == "n":
        user_ask_no = input("do you want to list your To-Do list ?\n")
        if user_ask_no == "y":
            file = open("TodoList.txt","r", encoding=("utf-8"))
            print(file.readlines())
            file.close()
            content = file.readlines()
            
            for index, notes in enumerate(content):
                print(f"{index} - {otes}")
            
    elif user_input == "exit":
        print("tWe're happy to help you , see you next time!")
        break      
       
'''