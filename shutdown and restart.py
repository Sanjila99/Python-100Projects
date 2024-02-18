import os
import platform
def shutdown():
  if platform.system()=="Windows":
        os.system('shutdown -s')
  elif platform.system()=="Linux" or platform.system()=="Darwin":
        os.system("shutdown -h now")
  else :
        print("os not  supported!")

def restart():
     if platform.system()=="Windows":
            os.system("shutdown -t 0 -r -f")
            '''Specifies the time delay before the shutdown (in seconds). In this case, it’s set to 0 seconds, meaning an immediate shutdown.
                -r: Indicates that the computer should restart after shutting down.
                -f: Forces running applications to close without prompting the user.'''
     elif platform.system()=="Linux" or platform.system()=="Darwin":
            os.system('rebbot now')
     else:
          print("Os not supported!")
command = input("Use \'r\' for restart and \'s\' for shutdown:").lower()
if command =="r":
      restart()
elif command =="s":
      shutdown()
else:
      print("Wrong letter")


