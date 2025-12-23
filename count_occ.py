def count_occu(arr, target):
    count = 0
    for i in arr:
        if i == target:
            count=count+1
    return count

print(count_occu([2,3,5,2,5,2], 9))