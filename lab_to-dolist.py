
file = open("to_do.txt", "a+", encoding="utf-8")

while True:
    answers_one = input(
        'do you want to add a new To-Do item? answer by "y" for yes and "n" for no')
    if answers_one == "y":

        file.write(input("type your new To-Do item :"))

    elif answers_one == "n":
        answers_two = input(
            'do you want to list your To-Do items ? answer "y" for yes and "n" for no.')
        if answers_two == "n":
            print("pleass type exit ")

        if answers_two == "y":
            file.seek(0)
            n = file.readlines()
            for i in n:
                print(i)

    else:
        file.close()
        break
