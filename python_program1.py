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
