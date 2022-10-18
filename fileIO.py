
while(True):

    user_input = input("user do you want to add a new To-Do item :")
    if user_input == "y":
        file = open("todo.txt", "a+", encoding="utf-8")
        input_user= input("do you want to type in his new To-Do item :")
        file.write(user_input + "\n")
        file.close()
    if user_input == "n":
        input_list= input("do you want to list your To-Do items :")
        if input_list == "n":
            file = open("todo.txt", "a+", encoding="utf-8")
            content = file.readline()
            file.close()
            for note in content:
                print(note)
    else:
        if user_input == "exit":
            print("bye !")
        break





