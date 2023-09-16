def Bubble_Sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr [j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [70,20,30,50,60,35,47]
result  = Bubble_Sort(arr)
print(result)

# Time complexity O(n^2)