def rotation(arr,shift):
	temp = 0
	for i in range(0,shift):
		temp = arr[0]
		j = 0
		while(j<=len(arr)-2):
			arr[j] = arr[j+1]
			j = j+1
		arr[len(arr)-1] = temp
	return arr		

arr = [1,2,3,4,5,6]
shift = 4
print(rotation(arr,shift))
