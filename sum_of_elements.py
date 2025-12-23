# def sum_of_el(list):
#     print(sum(list))
# sum_of_el([3,4])

def sum_of_all(arr):
    total = 0

    for i in arr:
        total=total+i
    return total

print(sum_of_all([6,7,10]))