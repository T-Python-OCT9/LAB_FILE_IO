file = open("to_do.txt","a+" , encoding="utf-8")

ex = True

while ex:
    ans = input("do you want to add a new To-Do item (\"y\" for yes and \"n\" for no or \"e\" to exit )?  ")
    if ans == 'y':
        todo = input("Enter your new To-Do item: ")
        file.write(todo + "\n")
    elif ans =='n':
        ans2 = input("Do you want to list your To-Do items (\"y\" for yes and \"n\" for no or \"e\" to exit)? ")
        if ans2 == 'y':
            file.seek(0)
            ListToDo =file.readlines()
            for i in ListToDo:
                print("-" , i)
        elif ans2 == 'n':
            continue
        elif ans2 == 'e':
            ex = False
        else:
            print("The answer not yes \"y\" or no \"n\"..")
    elif ans =='e':
        ex = False
    else:
        print("The answer not yes \"y\" or no \"n\"..")

print("Thank you for using the To-Do program, come back again soon")
file.close()