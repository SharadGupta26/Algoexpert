
def sort(arr) :
    i = 0
    j = len(arr) - 1
    k = 0
    while k <= j :
        val = arr[k]
        if val == 0 :
            arr[i], arr[k] = arr[k], arr[i]
            i += 1
            k+=1
            continue
        if val == 2 :
            arr[j], arr[k] = arr[k], arr[j]
            j -= 1
            continue
        k += 1
    return arr

def test() :
    print(sort([1,0,2,1,0]))
    print(sort([1,1,1,0,0,0]))
    print(sort([2,2,2,2,2,1,1,0,0,0,0,1,1,1,1,2,2,2,0,0,0]))
    print(sort([2,1,0]))
test()
    
        
