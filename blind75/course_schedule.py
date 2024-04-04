'''https://leetcode.com/problems/course-schedule/description/
#topological sort
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dep = {}
        for i in prerequisites :
            if i[0] in dep :
                dep[i[0]].append(i[1])
            else :
                dep[i[0]] = [i[1]]
        states = [0] * numCourses
        for i in range(numCourses) :
            if states[i] == 0 :
                states[i] = 1
                ans = self.solve(i, dep, states)
                if not ans :
                    return False
        return True
        


    def solve(self, node, dep, states) :
        if node not in dep :
            states[node] = 2
            return True
        
        if states[node] == 2 :
            return True
        for i in dep[node] :
            if states[i] == 1 :
                return False
            if states[i] == 0 :
                states[i] = 1
                ans = self.solve(i, dep, states)
                if not ans :
                    return False
        states[node] = 2
        return True
