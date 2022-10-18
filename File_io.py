
file = open ("to_do_item_new1.txt","a+" , encoding="utf-8")
user_input = input("do want to add new to-list y for yes n For no:")

if user_input == "y"  :
    user_input_2 = input("type ur new To-list:")
    file.write(f"\n{user_input_2}")
else: user_input == "n" 
user_input_3 = input("do you want to list your To-Do items ? answer \"y\" for yes and \"n\" for no:")
if user_input_3 == "y" :
        
    print("reading one line:")
    file = open ("to_do_item_new1.txt","a+" , encoding="utf-8")
    file.seek(0)
    print(file.readlines())
    file.close
    
