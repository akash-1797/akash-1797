#User function Template for python3
def getFloorAndCeil(arr, n, x):
    floor = -1
    ceil = max(arr)
    F=False
    C=False
    i = 0
    while(i<=n-1):
        if arr[i] <= x and arr[i] >= floor:
                floor = arr[i]
                F=True
        
        if arr[i] >= x and arr[i] <= ceil:
                ceil = arr[i]
                C=True
        i = i+1
    if C == False:
        ceil = -1
    if F == False:
        floor = -1
        
    return (floor,ceil)
