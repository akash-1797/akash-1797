def po(num,x):
  i = 1
  res = 1
  while(i<=x):
    res = res * num
    i = i+1
  return res

def count(num):
  count =0
  while(num != 0):
    count = count +1
    num = num//10
  return count

def check(number):
  y = count(number)
  rev = 1
  sum = 0 
  number_1 = number
  while(number_1 != 0):
    rev = number_1 % 10
    sum = sum + po(rev,y)
    number_1 = number_1//10
  if sum == number:
     print ('True')
  else:
    print('false')

n=int(input())
print(check(n))

