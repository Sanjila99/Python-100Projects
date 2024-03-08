import random

def choose_word():
    words=['apple', 'banana', 'orange', 'grape', 'strawberry', 'watermelon', 'pineapple']
    return random.choice(words)

def display_word(words,guessed_letters):
    display=" "
    for letter in words:
        if letter in guessed_letters:
            display+=letter
        else:
            display+='_'
    return display
def hangman():
    print("Welcome to Hangman!")
    word=choose_word()
    guessed_letters=[]
    attempts=6

    while True:
        print("\n Attempts left:",attempts)
        print("Word:",display_word(word,guessed_letters))
        
        if '_' not in display_word(word,guessed_letters):
           print("Congratulations !You guessed the word:",word)
           break

        if attempts==0:
            print("Sorry,you ran out of attempts! The word was:",word)
            break
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            print("Incorrect guess!")
            attempts -= 1

hangman()