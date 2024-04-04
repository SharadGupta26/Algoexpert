'''https://leetcode.com/problems/combination-sum/description/

For explanation, watch https://www.youtube.com/watch?v=GBKI9VSKdGg
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.recur(0, candidates, target, [], ans)
        return ans

    def recur(self, i, nums, target, running, ans) :
        if target < 0 or i >= len(nums):
            return 
        if target == 0 :
            ans.append(running[0:])
            return
        #we include current element
        running.append(nums[i])
        self.recur(i, nums, target - nums[i], running, ans)

        #backtrack. We don't include current element and start from next element
        running.pop()
        self.recur(i+1, nums, target, running, ans)
        

        