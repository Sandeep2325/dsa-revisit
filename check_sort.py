def check_sort(arr):
    for i in range(len(arr)):
        try:
            if arr[i] > arr[i+1]:
                return False
        except:
            return True
    return True
print(check_sort([1,2,3]))