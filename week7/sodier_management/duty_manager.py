from data import soldier_list
from data import 
def adding_a_duty(soldier_list):
   soldier = int(input("please enter the soldier id"))
   duty = str(input("please enter the duty name"))
   if soldier not in soldier_list:
      print("this soldier doesn't exist")
   if duty in soldier:
      print("this duty is already exist for this soldier")
   else:
      soldier[duties].append(duty)

def duty_status_update():
   duty = str(input("please enter a duty"))
   duty[status] = (str("please enter your update")) 

def viwe_duties_soldier(soldier_list):
   soldier = int(input("please enter the soldier id"))  
   if soldier not in soldier_list:
      print("this soldier doesn't exist")
   else:
      return soldier[duties] 