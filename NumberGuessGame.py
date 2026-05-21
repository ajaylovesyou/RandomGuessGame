# Number Guess game using python : 
import random
def show_mode():

    print("Choose Your mode !\n")
    print("1. Easy ")
    print("2. Medium ")
    print("3. Hard")
    print("4. Very hard\n")

def UserGuess(SecretGuess):

    secret = SecretGuess
    counter = 0
    while True:
        guess = int(input("Enter your guess: "))
        counter += 1

        if guess == secret:

             print("Woahh ! You Guessed it Right. Victoryyyy.....🏆✨\n ")
             print(f"You Guessed In { counter } Attampts.")
             break

        elif guess > secret:

             print("Too High!")

        elif guess < secret:

                print("Too Low!")

def Easy():

    SecretNumber = random.randint(1,10)
    return SecretNumber
    
        
def Medium():

    SecretNumber = random.randint(1,50)
    return SecretNumber

def Hard():

    SecretNumber = random.randint(1,100)
    return SecretNumber

def Very_hard():

    SecretNumber = random.randint(1,1000)
    
    return SecretNumber

def main():

    mode = show_mode()
    choice = input ("Enter your mode : ")
    match choice:
        case '1':

            UserGuess(Easy())

        case '2':

            UserGuess(Medium())

        case '3':
             
             UserGuess(Hard())

        case '4':
            
            UserGuess(Very_hard())
        
        case _:
            print("Invalid Mode ! Please choose again : ")

if __name__ == "__main__":
    main()

