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
