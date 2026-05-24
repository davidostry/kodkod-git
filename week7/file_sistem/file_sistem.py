def create_diary():
    with open ("diary.txt", "w", encoding = "utf-8") as create_diary:
         create_diary.write("24-5-26: I had a bisy day. \n25-5-26: I learn abote python. \n26-5-26: I compleate the project")
         print("diary created succefuly")
    with open("diary.txt", "r",encoding= "utf-8") as diary:
         diary = diary.read()
         print(diary)

def add_entry(file_name, date, content):
     with open(file_name, "a", encoding= "utf-8") as diary:
          diary.write(f"{date}: {content}\n")
    
print(add_entry(file_name="diary.txt",date="27-05-26",content="wonderfool day"))     

          

