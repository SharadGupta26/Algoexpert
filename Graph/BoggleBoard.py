'''
Given a matrix of characters and list of words.
Find all words in matrix.

A word is constructed in board by connecting adjecent characters (horizontal, vertical, digonal).
Without using any single character at a given position more than once.
A word can have repeated letters, those repeated letters must come from different positions.
'''

def boggleBoard(board, words):
    head = buildTrie(words)
    ans = set()
    vis = [[False for col in row] for row in board]
    for i in range(len(board)) :
        for j in range(len(board[i])) :
            traverse(board, head, i, j, vis, ans)
    return ans
    
def traverse(board, node, i, j, vis, ans) :
    if boarder(board, i, j) or vis[i][j] :
        return
    s = board[i][j]
    if s not in node.childs :
        return
   
    child = node.childs[s]

    if child.isword :
        ans.add(child.word)
        
    vis[i][j] = True
    traverse(board, child, i+1, j, vis, ans)
    traverse(board, child, i-1, j, vis, ans)
    traverse(board, child, i, j+1, vis, ans)
    traverse(board, child, i, j-1, vis, ans)
    traverse(board, child, i+1, j+1, vis, ans)
    traverse(board, child, i-1, j+1, vis, ans)
    traverse(board, child, i+1, j-1, vis, ans)
    traverse(board, child, i-1, j-1, vis, ans)
    vis[i][j] = False
    
    

def boarder(board, i, j ) :
    return i < 0 or j < 0 or i >= len(board) or j >= len(board[i])

class TrieNode :
    def __init__(self) :
        self.childs = {}
        self.isword = False
        self.word = ''

def buildTrie(words) :
    head = TrieNode()
    for word in words :
        temp = head
        for c in word :
            if c in temp.childs :
                temp = temp.childs[c]
            else :
                node = TrieNode()
                temp.childs[c] = node
                temp = node
        temp.isword = True
        temp.word = word
    return head

    