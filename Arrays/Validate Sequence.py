#given two integer arrays, find if 2nd arrays is subsequence of 1st array

def isValidSubsequence(array, sequence):
    # Write your code here.
	start = 0
	for i in array :
		if start < len(sequence) and i == sequence[start] :
			start += 1
	if start < len(sequence) :
		return False
	else :
		return True