'''https://leetcode.com/problems/group-anagrams/'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        for i in strs :
            j = str(sorted(i))
            if j in data :
                data[j].append(i)
            else :
                data[j] = [i]
        return data.values()


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        for i in strs :
            j = self.encode(i)
            if j in data :
                data[j].append(i)
            else :
                data[j] = [i]
        return data.values()
    def encode(self, word) :
        chars = [0] * 26 
        for i in word :
            chars[ord(i)-ord('a')] += 1
        return str(chars)