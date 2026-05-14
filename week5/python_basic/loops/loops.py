def odd_numbers():
    for num in range(10):
        if num%2==0:
            continue
        if num==7:
            break
    return num

def password():
    while True:
     password=input("please enter your password: ")
     if password=="1234":
       return "wellcome!"
     else:
        print("try again")

def product_names():
   while True:
      product_names=[]
      product=input("enter a product: ")
      if product=="done":
         break
      else:
         product_names.append("product")
   print (product_names)
      
def double_loop():
   for row in range(1,3):
      for col in range(1,3):
         print(row,col) 
         if col==2:
            break
         
def count_vowels():
    sentment=input("enter a setment: ")
    count=0
    for char in sentment:
      if char== "a" or "e" or "o" or "i" or "u":
          count+=1
    return count
    
def multiplication_table():
   for row in range(1,6):
      for col in range(1,6):
         result= row*col
         print (f"{row} x {col} = {result}")

def revers():
   
   user=input("enter str: ")
   revers=""
   for char in user:
      revers=char+revers
   return revers
   
def is_even():
   num=int(input("enter a number: "))
   count=0
   while num>0:

      if num%2==0:
         count+=1
      num=num//10
   return count

def repeat_char():
   word=input("enter a word: ")
   repeat=""
   for char in word:
      char=char*3
     
      repeat+=char
   print (repeat)

def highest_num():
    highest=0
    while True:
      num=int(input("enter a number: "))
      if num>highest:
         highest=num
      if num== 0:
          break
    print (highest)

def letters_and_numbers():
   str=input("enter your str: ")
   result=True
   for char in str:
      if not char.isalnum() :
         result= False
   return result

def revers_int():
    num=int(input("enter a number: "))
    revers_num=0
    while num>0:
      revers_num=(revers_num*10)+num%10
      num=num//10
    return revers_num

def id(name, /, age, adress):
   for i in id:
      print (i)
id(david,28,Bs)


      



   


   

         

           