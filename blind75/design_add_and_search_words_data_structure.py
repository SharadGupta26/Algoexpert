'''https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
'''

class Trie :
    def __init__(self, x) :
        self.isWord = False
        self.data = {}
        self.char = x

    def __str__(self) :
        return f"{self.char}, {self.isWord}, {self.data}"

class WordDictionary:

    def __init__(self):
        self.data = {}
        

    def addWord(self, word: str) -> None:
        temp  = self.data
        node = None
        for i in word :
            if i not in temp :
                node = Trie(i)
                temp[i] = node
            node = temp[i]
            temp = node.data
        node.isWord = True
        #print(node)

    def search(self, word: str) -> bool:
        return self.searchRec(word, self.data)

    def searchRec(self, word, data) :
        if not word :
            return False

        if len(word) == 1 :
            if word[0] == '.' :
                for i in data :
                    if data[i].isWord :
                        return True
                return False
            elif word[0] in data:
                return data[word[0]].isWord
            else :
                return False

        if word[0] == '.' :
            ans = False
            for i in data :
                ans = ans or self.searchRec(word[1:], data[i].data)
            return ans
        elif word[0] in data :
            return self.searchRec(word[1:], data[word[0]].data)
        else :
            return False

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)