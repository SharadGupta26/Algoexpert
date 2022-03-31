#given an arrays of distinct integers and a number, find a pair whose sum is equal to given no,

def twoNumberSum(array, targetSum):
    # Write your code here.
    data = set()
    for i in array :
        if targetSum - i in data :
            return [targetSum - i, i]
        else :
            data.add(i)
    return []