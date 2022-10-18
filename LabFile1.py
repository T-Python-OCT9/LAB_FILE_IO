
while True:
    i = input("do you want to add a new To-Do item?answer by y for yes and n for no.")

    if i == "y" :
      file = open('to-do.txt',"w",encoding="utf-8")
      task1= input("\n write")
      file.writelines(task1)
      file.close()
      i = input("do you want to add a new To-Do item?answer by y for yes and n for no.")

    if i == "n" :
      m = input("do you want to list your To-Do items ?")
      if m == "y" :
         file = open("to-do.txt","r",encoding="utf-8")
         print(file.readlines())
         file.close()
         
    else:
         print("write Exit for stop the program")    
         if i == "Exit" :
           print("thank you for using the To-Do program, come back again soon") 
         break            
        
         

     
       


