def max_element(arr):
    max_el=arr[0]
    for i in range(0,len(arr)):
        if arr[i]>max_el:
            max_el=arr[i]
    return max_el

print(max_element([89,93093,98,100]))