import time
import winsound

def countdown(t):
    while t:
        mins,secs=divmod(t,60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        print(timer,end='\r')
        time.sleep(1)
        t-=1
    
def pause_timer():
    input("Press Enter to pause the timer....")

def resume_timer():
    input("press Enter to resume the timer....")

def play_sound():
    winsound.Beep(1000,1000)

def countdown_with_pause_resume_and_sound(t):
    try:
        while t:
          mins,secs=divmod(t,60)
          timer='{:02d}:{:02d}'.format(mins,secs)
          print(timer,end='\r')
          time.sleep(1)
          t-=1
          if t==0:
            play_sound()
            break
          
          if input("Press 'p' to pause or 'r' to resume:") == 'p':
            pause_timer()
            resume_timer()

    except KeyboardInterrupt:
        print("\nCountdown paused.")
        resume_timer()


t=input("enter the time in seconds:")
countdown_with_pause_resume_and_sound(int(t))
print("Time is up!!")



