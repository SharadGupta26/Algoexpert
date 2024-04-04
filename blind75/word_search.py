'''https://leetcode.com/problems/word-search/description/

'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis = [[False for i in range(len(board[j]))] for j in range(len(board))]

        for i in range(len(board)) :
            for j in range(len(board[i])) :
                ans = self.find(i,j,board, word, "", vis)
                if ans :
                    return True
        return False

    def find(self, i, j, board, word, curr, vis) :
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]) :
            return False
        if vis[i][j] :
            return False
        curr = curr + board[i][j]
        if curr == word :
            return True
        
        vis[i][j] = True
        ans = False
        if word.startswith(curr) : #making sure we are moving in right dir
            ans = ans or self.find(i+1, j, board, word, curr, vis)
            ans = ans or self.find(i-1, j, board, word, curr, vis)
            ans = ans or self.find(i, j+1, board, word, curr, vis)
            ans = ans or self.find(i, j-1, board, word, curr, vis)
        vis[i][j] = False #backtracking
        return ans