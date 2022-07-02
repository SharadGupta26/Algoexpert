
'''
Given three input, all of which are instance of OrgChart. DirectReports pointing to their direct reports.
The first input is top manager and other two inputs are reports in org chart.
Return the lowest common manager of two reports.
'''

def getLowestCommonManager(topManager, reportOne, reportTwo):
    return getLowestCommonManager_rec(topManager, reportOne, reportTwo)[1]
   

'''
Solution - 
We are cheching how many reports are mathing direct report of any manager including manager itself.
then we return no of given reports matching with either manager or its direct + indirect reports.
If we find any manager, for which the match count is == 2, then this is the lowest common manager.
So we keep returning this in stack.
else we return current manager and match that we have found till now.
'''
def getLowestCommonManager_rec(manager,  one, two) :
	
	match = 1 if manager == one or manager == two else 0
	for report in manager.directReports :
		i, j = getLowestCommonManager_rec(report, one,two)
		if i == 2 :
			return (i,j)
		match += i
	return (match, manager)
		

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []


