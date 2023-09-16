
def Ternary_Search(arr,i,j,key):
    mid_1 = i + (j-i)//3
    mid_2 = j - (j-i)//3
    while i <= j:
        if arr[mid_1] == key:
            return mid_1
        elif arr[mid_2] == key:
            return mid_2
        elif key < arr[mid_1]:
            return Ternary_Search(arr,i,mid_1-1,key)
        elif key > arr[mid_2]:
            return Ternary_Search(arr,mid_2+1,j,key)
        else:
            return Ternary_Search(arr,mid_1+1,mid_2-1,key)
    return -1
            


arr = [20,25,47,56,63,65,79,82]
i = 0
j = len(arr)-1
key = 20
Result = Ternary_Search(arr,i,j,key)
print(Result)

