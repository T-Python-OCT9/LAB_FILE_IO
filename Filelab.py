# this is the Files-lab 18 oct - ghadah lahrbi 


import os
from pickle import TRUE

to_do = open ("to_do.txt", "a+", encoding="utf-8")

while TRUE:

    x=input("do you want to add a new To-Do item? please enter Y for yes and N for no , if you want to exit type exit ")

    if (x in 'yY'):
        to_do.write("\n")
        to_do.write(input("type in your new To-Do item : "))

    elif (x in 'Nn'):

        n=input("do you want to list your To-Do items ? ")

        if (n in 'nN'):

            print("please type exit , thank you ")

        elif (n in 'Yy'):

            to_do.seek(0)
            lines=to_do.readlines()
            for l in lines:
                print(l)
    else:
        to_do.close()
        break


            
