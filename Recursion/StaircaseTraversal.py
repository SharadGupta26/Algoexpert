'''
Given two positive integers representing height of staircase and the maximum no of steps you can advance
up the staircase at a time. return no of ways in which you can climb the staircase.
'''

def staircaseTraversal(height, maxSteps):
    mem = [-1 for i in range(height + 1)]
    return traverse(height, maxSteps, mem)

def traverse(height, maxSteps, mem) :
	if height < 0 :
		return 0
	if height == 0 :
		return 1
	if mem[height] != -1 :
		return mem[height]
	ways = 0
	for i in range(1, maxSteps+1) :
		ways += traverse(height - i, maxSteps, mem)
	mem[height] = ways
	return ways