

while True :
    ask_user = input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no: ")
    if ask_user == "y":
       user_answe = input("please type what you want in your list: " ) 
       file = open("to_do.txt" , "a" , encoding="utf-8")
       file.write(user_answe + "\n")
       file.close()

    elif ask_user =="n":
         ans = input("do you want to list your To-Do items ? answer 'y' for yes and 'n' for no: ")
         if ans =='y':
          file = open("to_do.txt" , "r" , encoding="utf-8")
          content = file.read()
          file.close()
          print(content)
          
    elif ask_user == 'exit':
      print("thank you for using the To-Do program, come back again soon")
      break

    else:
      print("please entre 'y' or 'n' , or if you want to exit the program entre 'exit': ")