from utils import user_choice
import  soldier_manager

def main_menu():
    print ("----duty soldier management----")
    print ("wellcome to duty soldier management")
    print("for adding a soldier press 1")
    print("for removing soldier press 2")
    print("for soldier list press 3")
    print("for adding a duty press 4")
    print("for duty status update press 5")
    print("for view duties soldier press 6")
    print("for exit prees 7")

def main():
    main_menu()
    while choice in ["1","2","3","4","5","6"]:
      choice = user_choice()
      if choice ==1:
         soldier_manager.adding_a_soldier()


      
    elif choice ==2:
       
    elif choice ==7:
       print ("Thank you for using the soldier management system")
       




   

 
   

   
   


      
        

        

    