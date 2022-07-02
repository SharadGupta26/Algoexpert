'''
Given an array of unique integers, return an array of all permutations of those integers in no perticular order
'''

'''
Sultion - The idea is to pick one element (keeping it fixed) and then swap it with all elements one by one.
Do this recursively and add array to o/p when you have reached to end of array. This becomes one permutation.

so for array [1,2,3], by keeping 1 fixed we get two permutations. [[1,2,3] , [1,3,2]]
next 1 is swapped by 2 and again we get two permutations [[2,1,3] , [2,3,1]]
next 1 is swapped by 3 so next two permutations [[3,2,1], [3,1,2]]
'''
def getPermutations(array):
    return getPermutations_rec(array, 0, [])

def getPermutations_rec(array, i, res) :
	if i == len(array) -1:
		res.append(list(array))
		return res
	
	for k in range(i, len(array)) :
		array[i], array[k] = array[k], array[i]
		getPermutations_rec(array, i +1, res)
		array[i], array[k] = array[k], array[i]
	
	return res
	