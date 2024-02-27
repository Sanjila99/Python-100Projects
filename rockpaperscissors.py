import random
import winsound
 
def play(user,computer):
   print(f"computer chose :{computer}")
   
   if user==computer:
        print("It's a tie!!")
        winsound.Beep(1000,1000)

   elif(user=='r'and computer=='s' or user=='s'and computer=='p'or user=='p' and computer=='r'):
        print("You win!")
   else:
       print("Computer wins!!")


while True:
    user=input("What's your choice?'r'for rock 's'for scissors 'p'for paper:")
    computer=random.choice(['p','r','s'])

    play(user,computer)

    playagain=input("Do you want to play again?(yes/no):").lower()
    if playagain!='yes':
        print("Thanks for playing")
        break


       
       
