'''https://leetcode.com/problems/top-k-frequent-elements/'''

from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = {}
        for i in nums :
            freq[i] = freq.get(i, 0) + 1
            
        for i in freq :
            if len(heap) < k :
                heappush(heap, freq[i])
            elif freq[i] > heap[0] :
                heappop(heap)
                heappush(heap, freq[i])

        ans = []
        for i in freq :
            if freq[i] in heap :
                ans.append(i)
        return ans
        

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        c = c.most_common(k)
        ans = []
        for i in c :
            ans.append(i[0])
        return ans