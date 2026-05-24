def adding_a_soldier(soldier_list):
   new_soldier_name = str(input("please enter the new soldier name"))
   new_soldier_id = int(input("please enter teh new soldier id"))

   if new_soldier_id in soldier_list:
      print("soldier alreadi exist")
   else:
      soldier_list.append(new_soldier_id)
      print("new soldier added succefully")

def removing_a_soldier(soldier_list):
   soldier = int(input("please enter the soldier id"))
   if soldier not in soldier_list:
      print("this soldier doesn't exist")
   else:
      soldier_list.remove(soldier)
      print("soldier removed succefully")

def view_soldier_list(soldier_list):
   return soldier_list