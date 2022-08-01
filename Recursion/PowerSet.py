'''
Given an array of unique integers, return its powerset
'''

#using BFS solution
from array import array
from collections import deque
def powerset(array):
    data = deque()
    data.append([])
    res = []
    i = 0
    for k in array:
        size = len(data)
        for i in range(size):
            elem = data[i]
            temp = list(elem)
            temp.append(k)
            data.append(temp)
        i+=1
    return list(data)



#using DFS solution
#the solution is to pick one element, and then once include it in the o/p and next time not inclue it in o/p and move to seconf element
#backtracking
def powerset2(array):
    ans = []
    ans.append([])
    powerset_rec(array, 0, [], ans)
    return ans

def powerset_rec(array, i, curr_op, ans) :
	if i == len(array) :
		return
    
    #including current element in o/p
	curr_op.append(array[i])
	ans.append(list(curr_op))

    #moving to next element
	powerset_rec(array, i+1, curr_op, ans)

    #not including current element in o/p and moving to next element
	curr_op.pop()
	powerset_rec(array, i+1, curr_op, ans)



#algoexpert solution
#O(n * 2^n)
def powerset_algo(array):
    ans = [[]]
    for i in array :
        for j in range(len(ans)) :
            curr = ans[j]
            curr.append(curr + [i])
    return ans


def test() :
    print(powerset2([1,2,2]))

test()
