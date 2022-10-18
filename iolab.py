

## Using what you learned about Python File I/O , we want to make a progeram called To-Do List , this program should do the following:
from ast import Break
from fileinput import close
from tkinter import Y
from typing import Optional


def ask()->str:
    user_input=input("Do you want to add a new To-Do item? answer y for yes and n for no :")
    return  Option_1(user_input)
    

def Option_1(x:str):
   if x == "y": 
      file = open('to_do.txt', "a+", encoding="utf-8")
      file.write(" " + input("Please type the new To-Do item  : ") + "\n")
      file.close()
      ask()

   elif x == "n":
    y =input("do you want to list your To-Do items?  answer y for yes and n for no  :")
    if y == "y":
        file = open('to_do.txt', "r", encoding="utf-8")
        content = file.read() 
        print(content) 
        Option_1(x)
    elif x=="n":
        ask()
    elif x=="exit":
        close()
        
    else:
        print( "thank you for using the To-Do program, come back again soon  :")

user_input = ask()
Option_1(user_input)
