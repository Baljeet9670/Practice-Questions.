
arr = [5,4,3,56,3,4,3,6,56,9]
arr1 = []
for i in range(len(arr)):
    j=i+1
    for j in range(j+1,len(arr)):
        if arr[i] == arr[j] and arr[j] not in arr1:
            print(arr[j])
            arr1.append(arr[j])
print(arr)
