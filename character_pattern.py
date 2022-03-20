n = int(input())
i = 1
s_c = chr(ord('A'))
while(i<=n):
  j = n-i+1
  k=1
  while(j>=i):
    char = chr(ord(s_c)+k-1)
    print(char,end='')
    k=k+1
    j = j-1
  print()
  i = i+1
  
