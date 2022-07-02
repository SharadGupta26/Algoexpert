'''
Given a 'special' array, return its product sum

special array is arrays that contains either integer or other 'special' array.

product sum of special array = sum of array * depth

depth of [] = 1
depth [[]] = 2

e.g. -> [x,[y,z]] => x + 2 * (y+z)
'''

# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    return sum(array, 1)

def sum(array, depth) :
	total = 0
	for i in array :
		if type(i) == list :
			total += sum(i, depth + 1)
		else :
			total += i
	return total * depth

    