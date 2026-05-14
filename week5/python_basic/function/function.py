def is_even(num):
    if num%2==0:
        return True
    else:
        return False

def factorial(number):
    factorial=1
    for num in range(1,number+1):
        factorial*=num
    return factorial

# def count_vowels(str):
#     for char in str:
#         if char is

def id(name, /, age, adress):
   print({name, age, adress})
id("david", 28, "jlm")

def name(*name):
    print(name)
name("jhvuyvf","ukytfd65")

def menu(name, /, *, age,):
    print(menu)
menu("david", age=28)
