#Program to write reverse of the contents of the original file to some other file
f=open('file.txt','r')
f1=f.read()
f1=f1[(len(f1)):0:-1]
f.close()
print(f"length is {len(f1)}")

f=open('file2.txt','w')
f.write(f1)
f.close()