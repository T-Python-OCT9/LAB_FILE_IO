stop_the_app = input("Write 'exit' if you want to exit the app: ")

while stop_the_app != "exit":
    user_answer = input("do you want to add a new To-Do item? answer by ""y"" for yes and ""n"" for no. ")
    if user_answer == "y":
        file = open("to_do.txt", "a", encoding="utf-8")
        user_notes = input("Please write your note: ")
        file.write(user_notes)
        file.close
        continue
    else:
        user_list = input("do you want to list your To-Do items ? answer 'y' for yes and 'n for no. ")
        if user_list == "y":
            print("reading one line:")
            file = open("to_do.txt", "a+", encoding="utf-8")
            file.seek(0)
            print(file.readlines())

            file.close()
            continue
        else:
            continue