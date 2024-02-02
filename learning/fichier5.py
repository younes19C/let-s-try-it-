import shutil # this help to copy a file 
import os
path ="C:\\Users\\RPC\python\\tp1\\learning\\test.txt"

if os.path.exists(path):
    print("path exist ")
    if os.path.isfile(path):
        print("that is a file ")
else:
    print("path not exist ")
# this is the method that ollow you to read what is inside the file 
f=open(path,"r")
print(f.read())
f.close()
print(f.closed)
# this is the method that ollow you to write inside the file 
text='yoooo i finaly did it \n this is a good day for me i will learn\n  a lot about python  '
f=open(path,"a")
f.write(text)
f.close()

# now i will copy this file his path to the desctop (we can copy a file in multiple destinations )
shutil.copy(path,"C:\\Users\\RPC\\Desktop\\test.txt") #(src,destination )
f3=open("C:\\Users\\RPC\\Desktop\\demo.txt",'w')
f3.write('work work and more work ')
f3.close()
def nligne(sourc):
    f1 = open(sourc,'r')
    n=0
    for i in f1:
        n+=1
    f1.close()
    return n
print(nligne(path))










''' with open("fille.txt","a") as f:

    The key function for working with files in Python is the open() function.

    The open() function takes two parameters; filename, and mode.

    There are four different methods (modes) for opening a file:

    "r" - Read - Default value. Opens a file for reading, error if the file does not exist

    "a" - Append - Opens a file for appending, creates the file if it does not exist

    "w" - Write - Opens a file for writing, creates the file if it does not exist

    "x" - Create - Creates the specified file, returns an error if the file exists
    '''
    
    #f.write("let's add more information to this file ")
    #f.close()
    # If the file is located in a different location, you will have to specify the file path#
    # You can return one line by using the readline() method:
   # f=open("fille1.txt","r")
    #ch=f.read()
    #print(ch)
    #f.close()
###To delete a file, you must import the OS module, and run its os.remove() function:
''' import os
os.remove("fille1.txt")
f.close() '''
#for i in range(len(f)) :
    #print(i)