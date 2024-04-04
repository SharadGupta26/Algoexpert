'''https://leetcode.com/problems/jump-game/description/

'''

#DFS
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.recur(nums, 0, {})
    def recur(self, nums, i) :
        if i >= len(nums) - 1 :
            return True
        if nums[i] == 0 :
            return False
        if i in mem :
            return mem[i]
        ans = False
        val = nums[i]
        while not ans and val > 0 :
            ans = self.recur(nums, i+val, mem)
            val -= 1
        mem[i] = ans
        return ans
        
# iterative
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1 :
            return True
        poss = [False] * len(nums) 
        poss[0] = nums[0] != 0
        for i in range(len(nums)) :
            val = nums[i]
            if val == 0 :
                continue
            if poss[i] :
                for j in reversed(range(i+1, min(i+val+1, len(nums)))) :
                    if j == len(nums) - 1 :
                        return True
                    poss[j] = True

        return poss[len(nums) - 1]    
