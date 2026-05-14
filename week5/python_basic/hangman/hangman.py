def computer_choise():
    from random import choice
    words=["adventure", "building", "coffee", "dinosaur", "elephant", 
    "football", "galaxy", "holiday", "imagine", "journey", 
    "kitchen", "language", "mountain", "notebook", "ocean", 
    "pyramid", "quality", "rainbow", "science", "thunder", 
    "universe", "vacation", "weather", "yellow", "zipper"]
    secret_word = choice(words)
    return secret_word

def user_letter(letters_guessed):
    while True:
        user_letter = input("please guess a letter: ").lower()
        if user_letter <"a" or user_letter>"z":
           print("invalid input. please enter an english letters only")
        elif len(user_letter)>1:
           print("too meny chars. please enter one letter")
        elif user_letter in letters_guessed:
            
            print("yo already guessed this letter")
        else:
            return user_letter
            

def comparison(secret_word, user_letter, hidden_word, attempts):
    if user_letter in secret_word:
        for i in range(len(secret_word)):
            if user_letter == secret_word[i]:
                hidden_word[i] = user_letter
                print(f"bingo! '{user_letter}' is successful guess")
    else:
        attempts-=1
        print("wrong guess")
    return attempts
        
def menue():
    attempts = 10
    secret_word=computer_choise()
    hidden_word = ["_"] *len(secret_word)
    letters_guessed = []
    

    print("---wellcome to hangman---")
   
    while attempts > 0 and "_" in hidden_word:
         print(f"word: {' '.join(hidden_word)}")
         print(f"you have: {attempts} attempts")
         print(f"letters guessed: {', '.join(letters_guessed)}")
         user_letter=user_letter(letters_guessed)

         letters_guessed.append(user_letter)
         attempts=comparison(secret_word, user_letter, hidden_word, attempts)

menue()








