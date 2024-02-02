import shutil # this help to copy a file 
import os
path="C:\\Users\\RPC\\Desktop\\yours.txt"
if os.path.exists(path):
    print("path exist ")
    if os.path.isfile(path):
        print("that is a file ")

f=open(path,'w+')
f.write('what the fuck are you saying \n' )
f.write('never say that again \n ' )
f.write('how ald are you \n ')
f.write('what is the best way to change your life \n')
f.write('i am gonna make the difference i this fucking world \n ')
f.close()
f=open(path,'r+')
print(f.readline(4))
f.close()
T=(1,2,3,4,5,6,7,8,9)
print(type(T))
for i in range(len(T)):
    print(T[i],end=" ")
L=list(T)
print("\n")
print(type(L))
L[1]=131
print(L)
T=tuple(L)
print(T)