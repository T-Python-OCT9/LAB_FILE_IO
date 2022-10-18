while(True):#to r

    user_input = input("do you want to add a new To-Do item? \npleas answer by yes or no  :")
    if user_input == "yes":
        file = open("todo.txt", "a+", encoding="utf-8")
        input_user= input("do you want to type in his new To-Do item :")
        file.write(user_input)
        file.close()
    if user_input == "no":
        input_list= input("do you want to list your To-Do items ? :")
        if input_list == "no":
            file = open("todo.txt", "s+", encoding="utf-8")
            content=file.readline()
            file.close()
            for note in content:
                print(note)
    else:
        user_exit = input(" do u want to exite please write (exite) :")
        if user_exit == "exite" :
            print("thank you for using the To-Do program, come back again soon")
        break
    break