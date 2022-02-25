
def find(arr,key):
  low = 0
  high = len(arr)-1
  while(low <= high):
    mid = low + (high - low)//2
    if arr[mid] == key:
      return mid 
    if arr[mid] >= arr[low]:
      if key >= arr[low] and key <= arr[mid]:
        high = mid -1
      else:
        low = mid +1
    else:
      if key >= arr[mid] and key <= arr[high]:
        low = mid+1
      else:
        high = mid -1
  return -1      
arr = [17,20,22,23,11,12,15,16]
key = 15
print(find(arr,key))

