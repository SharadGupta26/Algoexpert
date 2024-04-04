'''https://leetcode.com/problems/insert-interval/'''


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(intervals)) :
            a,b = intervals[i]
            c,d = newInterval
            if b < c :
                ans.append(intervals[i])
            elif d < a :
                ans.append(newInterval)
                newInterval = intervals[i]
            else :
                newInterval = [min(a,c), max(b,d)]
        ans.append(newInterval)
        return ans


        