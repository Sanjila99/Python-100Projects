import os

def main():
    i=0
    path=r"C:\Users\dell\Desktop\pics"
    for filename in os.listdir(path):
        my_dest="img"+str(i)+".jpg"
        my_source = os.path.join(path, filename)
        my_dest=path+my_dest
        os.rename(my_source,my_dest)
        i +=1


if __name__=='__main__':
    main()