'''https://leetcode.com/problems/trapping-rain-water/description/'''

class Solution:
    def trap_withspace(self, height: List[int]) -> int:
        ans = 0
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        for i in range(1, len(height)) :
            maxLeft[i] = max(maxLeft[i-1], height[i-1])

        for i in reversed(range(len(height)-1)) :
            maxRight[i] = max(maxRight[i+1], height[i+1])

        for i in range(len(height)) :
            minVal = min(maxLeft[i], maxRight[i])
            if minVal - height[i] >= 0 :
                ans += (minVal - height[i])

        return ans

    #wihtout extra space
    def trap(self, height: List[int]) -> int:
        if not height :
            return 0
        
        l,r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        ans = 0

        while l < r :
            if maxLeft < maxRight :
                l += 1
                maxLeft = max(maxLeft, height[l])
                ans += (maxLeft - height[l])
            else :
                r -= 1
                maxRight = max(maxRight, height[r])
                ans += (maxRight - height[r])
        return ans

