def remove_dups(arr):
    result=[]
    for num in arr:
        found = False
        for x in result:
            if x==num:
                found=True
                break
        if not found:
            result.append(num)
    return result
