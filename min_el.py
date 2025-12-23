def find_min(arr):
    min_el=arr[0]
    for i in range(0, len(arr)):
        if arr[i]<min_el:
            min_el=arr[i]
    return min_el

print(find_min([-1,0,7,-3]))