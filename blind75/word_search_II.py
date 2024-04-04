'''https://leetcode.com/problems/word-search-ii/description/'''


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def dfs(i, j, k, word, vis, mem) :
            
            if k >= len(word) :
                return True

            if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]) or vis[i][j]:
                return False

            if (i,j,word[k:]) in mem :
                return mem[(i,j,word[k:])]
            
            if board[i][j] == word[k] :
                vis[i][j] = True
                ans = False
                ans = ans or dfs(i+1, j, k +1, word, vis, mem)
                ans = ans or dfs(i-1, j, k +1, word, vis, mem)
                ans = ans or dfs(i, j+1, k +1, word, vis, mem)
                ans = ans or dfs(i, j-1, k +1, word, vis, mem)
                vis[i][j] = False
                mem[(i,j,word[k:])] = ans
                return ans
            return False
        
        vis = [[False for i in range(len(board[j]))] for j in range(len(board))]
        ans = []
        mem = {}
        for w in words :
            matched = False
            for i in range(len(board)) :
                for j in range(len(board[i])) :
                    if dfs(i,j,0,w,vis, mem) :
                        matched = True
            if matched :
                ans.append(w)
        
        return ans
                        

            
