n = int(input())
n1=(n+1)//2
startValue = 1
for i in range(1,n+1):
    for j in range(startValue,startValue + n):
        print(j,end=" ") 
    print() 
    #middle row
    if(i==n1):
        
        if((n%2)==0):
            startValue = n*(n-1)+1 
        else:
            startValue = n*(n-2) + 1 
    #lower half rows
    elif(i>n1):
        startValue = startValue - 2*n
    #second row
    else:
        startValue = startValue + 2*n

