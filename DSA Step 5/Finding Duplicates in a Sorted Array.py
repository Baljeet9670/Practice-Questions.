arr = [1,3,5,5,7,9,9,11,11]
arr1 = []
for i in range(1, len(arr)):

    if arr[i]==arr[i-1] and arr[i] not in arr1:
        print(arr[i])
        arr1.append(arr[i])
