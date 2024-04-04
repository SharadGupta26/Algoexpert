'''https://leetcode.com/problems/non-overlapping-intervals/description/'''


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x : x[0])
        curr = intervals[0]
        count = 0
        for i in range(1, len(intervals)) :
            a,b = intervals[i]
            c,d = curr
            if self.overlap(intervals[i], curr) :
                count += 1
                if b < d :
                    curr = intervals[i]
            else :
                curr = intervals[i]
               
        return count

    def overlap(self,i,j):
        a,b = i
        c,d = j
        ans = (b <= c) or (d <= a)
        return not ans

