n = int(input())
i = 1
while(i<=n):
  j = 1
  while(j<=i):
    print(j,end='')
    j = j+1

  space = 1
  while(space<=2*n-2*i):
    print(' ',end='')
    space = space + 1

  z = i
  while(z>=1):
    print(z,end='')
    z = z-1
  print()
  i = i+1
  
