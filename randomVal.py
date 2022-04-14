import matplotlib.pyplot as plt                         #To plot the graph


def random(noOfletters):                                #Function to generate random numbers having number of digits = noOfletters
    ans=""
    f=open('file.txt','r')                              #Opening File
    
    global s
    s=f.read(1000)                                      #Reading the first 1000 characters from the file
    
    global a,b,c
    a,b,c=0,1,2                                         #Initializing a,b,c as global variables

    while noOfletters>0:                                #Loop till we attain the desired number of digits
        
        seed=(int(s[a]+s[b]+s[c]))                      #Initializing the seed value
        if(seed==0):                                    #Corner case handling
            seed=5
            
        noOfletters-=1                                  #Decreasing the loop variable
        k=max(int(seed%10),1)                           #Handling corner case for initializing the start variable
        
        start=int(k)
        iterations=seed%len(s)                         #Handling corner case when value of seed is greater than length of the string
        sum=0                                          #Initializing sum = 0
        while iterations>0:                            #Looping for each iteration
            try:                                       #Handling corner case if s[start] isn't a valid number(blank space could be possible)
                sum+=int(s[start])                     #Incrementing the value of sum digit by digit from the string
                start+=1                               #Incrementing start variable to point to next digit in the string
                start=start%len(s)                     #Handling corner case when start > length of string 
                iterations-=1
            except:
                start+=1
                
        avg=(int(sum*100/seed))                        #Taking modified average
        ans+=str(avg%10)                               #Appending the last digit of the obtained average into the answer
        
        a,b,c=(a+1)%len(s),(b+1)%len(s),(c+1)%len(s)   #Incrementing values of a,b and c by one and also handling corner case.
        
                                                    
    f1=f.read()                                        #Reading the full contents of the file
    f1=f1[min(len(f1),int(ans)*1000):0:-1]             #Reversing the string obtained
    f.close()                                          #Closing the file
    
    #The below code helps that the content of the file never becomes null

    if(len(f1)>1000):                                  
        f=open('file.txt','w')
        f.write(f1)                                   #Truncating the content of file with the obtained reversed string
        f.close()
    else:
        f1=open('file2.txt','r')
        dataFile2=f1.read()
        f=open('file.txt','a')                       #Appending data from another file to the current file
        f.write(dataFile2)
        f.close()
        f1.close()
    return ans



#The below function works like the one preceding it.
#Only the content of the files have been shuffled

def random1(noOfletters):
    ans=""
    
    f=open('file4.txt','r')
    global s
    s=f.read(1000)
    
    global a,b,c
    a,b,c=0,1,2

    while noOfletters>0:

        seed=(int(s[a]+s[b]+s[c]))
        if(seed==0):
            seed=5
        noOfletters-=1
        k=max(int(seed%10),1)
        start=int(k)
        iterations=seed%len(s)
        sum=0
        while iterations>0:
            try:
                sum+=int(s[start])
                start+=1
                start=start%len(s)
                iterations-=1
            except:
                start+=1
        avg=(int(sum*100/seed))
        ans+=str(avg%10)
        a,b,c=(a+1)%len(s),(b+1)%len(s),(c+1)%len(s)
        
    f1=f.read()
    f1=f1[min(len(f1),int(ans)*1000):0:-1]
    f.close()



    if(len(f1)>1000):
        f=open('file4.txt','w')
        f.write(f1)
        f.close()
    else:
        f1=open('file3.txt','r')
        dataFile2=f1.read()
        f=open('file4.txt','a')
        f.write(dataFile2)
        f.close()
        f1.close()
    return ans


if __name__=="__main__":
    #Estimation of pi using monte carlo
    x=[]                                             #It will contain the values of x coordinate 
    y=[]                                             #It will contain the values of y coordinate

    circle_points=0                                  #To mark points that lie inside the circle
    square_points=0                                  #To mark points that lie inside the square

    for i in range(1000):                            #Looping for thousand random values
        x_val=int(random(4))/10000                   
        y_val=int(random1(4))/10000                  
        x.append(x_val)                              #Appending the x coordinate value
        y.append(y_val)                              #Appending the y coordinate value
        sumOfSquares=x_val**2+y_val**2               #Calculating the sum of Squares
    
        if sumOfSquares<=1:
            circle_points+=1
        square_points+=1
        # interval+=1

        pi=4*(circle_points/square_points)          #Calculating value of pi

    print(f"pi is {pi}")

    #Plotting the random values using matplotlib
    fig2=plt.figure()
    ax=fig2.add_axes([0,0,1,1])
    ax.scatter(x,y,color='g')
    print(x)                                        #Gives random values of x
    print(y)                                        #Gives random values of y
    plt.show()                                      #To display the graph







