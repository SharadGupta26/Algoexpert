def threeNumberSum(array, targetSum):
	array.sort()
	res = []
	for i in range(0, len(array)) :
		l = i+1
		r = len(array) - 1
		while l < r :
			val = array[i] + array[l] + array[r]
			if(val == targetSum) :
				res.append([array[i], array[l], array[r]])
				l += 1
				r -= 1
			elif val < targetSum :
				l+=1
			else :
				r -= 1
	return res
		
    