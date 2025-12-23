def reverse_list(els):
    print(els)
    els.reverse()
    print(els)

# reverse_list([1,2,4])


def rev_list(listt): #has bug fix this
    #[2,4,5]
    list_comp=[x for x in range(0,len(listt))]
    print(list_comp)
    for i in range(0,len(list_comp)):
        list_comp(len(list_comp)-i, listt[i])
    

# rev_list([1,2,3,4])

# working method
def reverse_actual(arr):
    left=0  #start index
    right = len(arr)-1 #end index

    while left<right:
        # left will be 0
        # right will be 4
        arr[left], arr[right] = arr[right], arr[left]

        left+=1
        right-=1
    
    return arr
print(reverse_actual([2,4,6,67]))
