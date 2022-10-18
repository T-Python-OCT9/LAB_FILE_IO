
exitProgram="e"
while(exitProgram=="e"):
    answer= input("do you want to add a new To-Do item? answer by -y- for yes and -n- for no.")
    if answer=="y" or answer=="Y":
        writeItem=input("type in his new To-Do item ")
        file=open("to_do.txt","w", encoding="UTF-8")
        file.writelines(writeItem)
        file.close()
        answerReading=input("do you want to list your To-Do items ? answer -y- for yes and -n- for no")
        if answerReading=="y" or answerReading=="Y":
            file=open("to_do.txt","r",encoding="UTF-8")
            print(file.readlines())
        else:
            answer=input("do you want to add a new To-Do item? answer by -y- for yes and -n- for no.")
    else:
        exitProgram=input("do you want exit program ? if yes enter e")
        if exitProgram=="e" or exitProgram=="E":
            print("thank you for using the To-Do program, come back again soon")  
            break

    

    








