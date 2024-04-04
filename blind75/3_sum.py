'''
https://leetcode.com/problems/3sum/description/
https://www.youtube.com/watch?v=jzZsG8n2R9A
'''
# O(nlogn) + O(n^2) -> O(n^2)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums) :
            if i > 0 and a == nums[i-1] :
                continue
            l,r =  i+1 ,len(nums) - 1
            while l < r :
                val = a + nums[l] + nums[r] 
                if val < 0 : 
                    l += 1
                elif val > 0 : 
                    r -= 1
                else :
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r :
                        l += 1
        return res