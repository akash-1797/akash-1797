
https://www.geeksforgeeks.org/python-string-exercise/

string = input('enter the string:')
index = len(string)
count = 0
i =0 
while(i < int(index)/2):
  if(string[i]==string[index-i-1]):
    count= count+1
  i = i+1
if count == i:
  print(f' the string {string} is palindrome')
else:
  print('no')    
(Palindrome string method 1)

2);
def sym(s):
  start = 0 
  mid = len(s)//2
  last = len(s)-1
  flag = 0
  while(start<mid):
    if s[start]==s[last]:
      start = start +1
      last = last -1
    else:
      flag = 1 
      break
  if flag == 0:
    return 'yes'
  else:
    return 'no'      
   
   

string = input('enter the string:\n')
print(sym(string))


3)..s = input('enter the string:\n')
result = "" 
i = 0
n = len(s)

while i < n:
  while i < n and s[i] == ' ': 
    i += 1
  if i >= n: 
    break
  j = i + 1
  while j < n and s[j] != ' ': 
    j += 1
  sub = s[i:j]
  if len(result) == 0: 
    result = sub
  else: 
    result = sub + " " + result
  i = j+1
print(result)

——
#)num = int(input('enter the num:\n'))
a =0 
b =1 
c = 0
i =1
while(c<num):
  a =b
  b=c
  c =a+b
  i = i+1
if c == num:
  print('yes' , i )
else:
  print('no')

#)arr = []
n = int(input('enter the size:\n'))
for i in range(n):
  i = int(input('enter the number:'))
  arr.append(i)

print(arr)
largest = arr[0]
smallest = arr[0]
b =1
while(b < len(arr)):
  if arr[b]< smallest:
    smallest = arr[b]
  if arr[b]> largest:
    largest = arr[b]
  b = b+1  
print(largest,smallest)      

Symmtrical :
string = input('enter the string:')
l = len(string)
start = 0
flag = 0
if l % 2 ==0:
  mid = l//2
else:
  mid=(l+1)//2
while(start<mid and mid < l ):
  if string[start]==string[mid]:
    start = start + 1
    mid = mid +1
  else:
    flag = 1
    break 

if flag == 0:
  print('yes')
else:
  print('no')  

3)Reverse the words in string;
string = input('enter the string:')
l = string.split(' ')
x = l[::-1]
print(x)

4)
s = input('enter the string:')
l = len(s)
result = ''
i=0
while(i<l):
  while( i<l and s[i]==' ' ):
    i = i+1
  if i>=l:
    break
  j =i+1
  while(j<l and s[j]!=' '):
    j = j+1
  sub_string = s[i:j]
  if (len(result) == 0):
    result = sub_string
  else:
    result = sub_string + ' ' + result
  i = j +1      
print(result) 

#)Count char 
s = input('enter the string:\n')
l=len(s)
i =0 
result = ''
while(i<l):
  if s[i] not in result:
    result = result + s[i]
    print(f'{s[i]}:{s.count(s[i])}')
  i = i+1  

Even no of words in string :
s = input('enter the string:\n')
l = len(s)
i = 0
result = ''
while(i<l):
  while(i<l and s[i]==' '):
    i = i+1
  if i>=l:
    break
  j = i+1
  while(j<l and s[j]!=' '):
    j = j+1
  w = s[i:j]
  if len(w)%2==0:
    result = result + " " + w
  i = j+1
print(result,end = ' ')  



import array as arr
def binary_search(a,key):
  low = 0
  high = len(a)-1
  mid = 0
  while(low<=high):
    mid = low + (high-low)//2
    if key == a[mid]:
      return mid
    elif key < a[mid]:
      high = mid-1
    else:
      low = mid +1
  return(-1) 



**import array as arr
def binary_search(a,key):
  low = 0
  high = len(a)-1
  mid = 0
  while(low<=high):
    mid = low + (high-low)//2
    if key == a[mid]:
      return mid
    elif key < a[mid]:
      low = mid+1
    else:
      high = mid -1
  return(-1)


def binary_acen_b_S(a,key):
  low = 0
  high = len(a)-1
  mid = 0
  while(low<=high):
    mid = low + (high-low)//2
    if key == a[mid]:
      return mid
    elif key < a[mid]:
      high = mid-1
    else:
      low = mid +1
  return(-1)


a = arr.array('i',[1,2,3,4,5,6,7,8,9,1,11])
key = 8
if a[0]>a[1]:
  print(binary_search(a,key))
else:
  **print(binary_acen_b_S(a,key))  


**import array as arr
lenght = int(input('enter the lenght of array'))
a = arr.array('i',[])
for i in range(lenght):
  x = int(input('enter the elements:'))
  a.append(x)
print(a)  
len_1 = len(a)
i = 0
j = len_1-1
while(i<j):
  while(a[i]<0 and i<j):
    i = i+1
  while(a[j]>0 and i<j):
    j = j-1
  if (i<j):
    temp = a[i]
    a[i]=a[j]
    a[j]=temp
    i = i+1
    j = j-1
  else:
    break
print(a)        

**import array as arr
def merging_sort(a1,a2):
  i = 0
  j = 0
  len1= len(a1)
  len2 = len(a2)
  a = arr.array('i',[])
  while(i<len1 and j<len2):
    if a1[i]<a2[j]:
      a.append(a1[i])
      i = i+1
    else:
      a.append(a2[j])
      j= j+1
  while(i<len1):
    a.append(a1[i])
    i = i+1
  while(j<len2):
    a.append(a2[j])
    j = j+1
  return(a)

a = arr.array('i',[1,2,3,4,5,6,7,8,9])
b = arr.array('i',[77,88,99,100,101,10222])
print(merging_sort(a,b))


**unoin
import array as arr
def merging_sort(a1,a2):
  i = 0
  j = 0
  len1= len(a1)
  len2 = len(a2)
  a = arr.array('i',[])
  while(i<len1 and j<len2):
    if a1[i]<a2[j]:
      a.append(a1[i])
      i = i+1
    elif a1[i] == a2[j]:
      a.append(a2[j])
      i= i+1
      j= j+1
    else:
      a.append(a[j])
      j = j+1
  while(i<len1):
    a.append(a1[i])
    i = i+1
  while(j<len2):
    a.append(a2[j])
    j = j+1
  return(a)

a = arr.array('i',[1,2,3,4,5,6,7,8,9,10,11,12])
b = arr.array('i',[5,6,8])
print(merging_sort(a,b))

** intersection
import array as arr
def merging_sort(a1,a2):
  i = 0
  j = 0
  len1= len(a1)
  len2 = len(a2)
  a = arr.array('i',[])
  while(i<len1 and j<len2):
    if a1[i]<a2[j]:
         i = i+1
   elif a1[i] == a2[j]:
     a.append(a[I])
      i= i+1
      j= j+1
   else:
      j = j+1
  return(a)

a = arr.array('i',[1,2,3,4,5,6,7,8,9,10,11,12])
b = arr.array('i',[5,6,8,9])
print(merging_sort(a,b))


**import array as arr
def missing_number(a):
  i = 0
  sum2= 0
  l = len(a)
  while(i<len(a)):
    sum2 = sum2+a[i]
    i = i+1
  print(sum2)  
  sum1 = a[len(a)-1]*(a[len(a)-1]+1)//2 
  print(sum1)
  missing_num = sum1-sum2
  return (missing_num)


a = arr.array('i',[1,2,3,4,5,6,7,8,10])
print(missing_number(a))

  


  def missing_number(a):
  low = a[0]
  diff = low - 0
  i = 0
  while(i<len(a)):
    if a[i] - i != diff:
      missing = i + diff
    i = i+1
  return(missing)  


a = [3,4,5,6,7,9]
print(missing_number(a))


**import array as arr
def missing_number(a):
  low = a[0]
  diff = low-0
  i = 0
  x = 0
  a_1 = arr.array('i',[])
  while(i<len(a)):
    if a[i]-i != diff:
      while(diff<a[i]-i):
        x =  i+diff
        a_1.append(x)
        diff = diff+1
    i = i+1    
  return(a_1)

a = arr.array('i',[2,4,5,6,7,8,10,12,16])  
print(missing_number(a))





a = [1,2,3,4,4,55,6,7,8,9,9,9]
i = 0
last_dulpicate = 0
for i in range(0,len(a)-1):
  if a[i]==a[i+1] and a[i] != last_dulpicate:
    last_dulpicate = a[i]
    print(last_dulpicate)
    print(a[i],end = ' ')

  def check_anti_clockwise_rotation(arr,n):
  low = 0
  high = n -1
  while(low <= high):
    if arr[low] <= arr[high]:
      return low
    mid = low + (high-low)//2
    next = (mid-1)%n
    previous = (mid + n - 1)%n
    if arr[mid] <= arr[next] and arr[mid] <= arr[previous]:
      return mid
    if arr[mid] >= arr[low]:
      low = mid+1
    if arr[mid] <= arr[high]:
      high = mid -1
  return -1

arr = [11,12,15,18,19,20,21,2,5,6,8,9,10]
n = len(arr)
print(check_anti_clockwise_rotation(arr,n))

