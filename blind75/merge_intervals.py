'''https://leetcode.com/problems/merge-intervals/description/'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals = sorted(intervals, key = lambda x : x[0])
        curr = intervals[0]
        for i in range(1, len(intervals)) :
            a,b = intervals[i]
            c,d = curr

            if b < c :
                ans.append(intervals[i])
            elif d < a :
                ans.append(curr)
                curr = intervals[i]
            else :
                curr = [min(a,c), max(b,d)]
        
        ans.append(curr)
        return ans
