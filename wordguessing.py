from random import choice
 
words=['soy', 'pen', 'heart', 'guitar', 'laptop', 'hand', 'coder']
computer=choice(words)

print("-------------Welcome to the Word Guessing Game-------------------")
print(f"Instructions : Enter any word from {words} and see if u guessed the computer's choice and u have three chances.")
players_name=input("Enter your name:")
print(f"All best {players_name}!!!")

turns=3
guesses=''

while turns>0:
    failed=0
    for char in computer:
        if char in guesses:
            print(char,end=" ")
        else:
            print("-",end=" ")
            failed+=1

    if failed==0:
        print("\n Congratulations!You Won!")
        break

    guess=input("\n Enter your guess word:")
    guesses+=guess
    
    if guess not in computer:
        turns-=1
        print("Wrong guess!")
        print("You have",turns,"more turns.")
        if turns==0:
            print("You lose!! The word was:",computer)
