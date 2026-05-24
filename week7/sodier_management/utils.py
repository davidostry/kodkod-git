def user_choice():
    user = False
    while user == False: 
        choice = (input("please enter your choice: "))
        if choice not in ["1", "2", "3", "4"]:
           print ("invalid choice")
        else:
          user = True
    return choice
