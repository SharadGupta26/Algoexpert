

#BFS approach

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root :
            return ""
        ans = []
        data = deque([root])
        while data :
            size = len(data)
            while size :
                size -= 1
                e = data.popleft()
                ans.append(str(e.val) if e else "")
                if e :
                    data.append(e.left)
                    data.append(e.right)
        res = ",".join(ans)
        return res

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data :
            return None
        data = data.split(',')
        head= TreeNode(int(data[0]))
        arr = deque([head])
        i = 1
        while i < len(data) :
            size = len(arr)
            while size :
                size -= 1
                #root
                root = arr.popleft()
                if root :
                    left = TreeNode(int(data[i])) if data[i] else None
                    i += 1
                    right = TreeNode(int(data[i])) if data[i] else None
                    i += 1

                    root.left = left
                    root.right = right
                    arr.append(left)
                    arr.append(right)
        return head

        



from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        def dfs(root) :
            if not root :
                ans.append("")
                return
            ans.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        print(ans)
        return ",".join(ans)
    
        

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data :
            return None
        data = data.split(',')
        self.i = 0

        def dfs() :
            if not data[self.i] :
                return None
            root = TreeNode(int(data[self.i]))
            self.i += 1
            root.left = dfs()
            self.i += 1
            root.right = dfs()
            return root
        return dfs()