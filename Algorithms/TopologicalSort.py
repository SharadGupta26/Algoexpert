'''
Given n jobs and their dependency, return order of jobs they can be executed.
Any job can be executed only if all of its depndenct jobs can be executed first.

i/p
jobs : [1, 2, 3, 4]
Dep :
[
  [1, 2],
  [1, 3],
  [3, 2],
  [4, 2],
  [4, 3]
]

o/p - [1, 4, 3, 2] or [4,3, 2, 1]
'''

def topologicalSort(jobs, deps):
    # Write your code here.
    matrix = [[] for i in range(len(jobs) + 1)]
    vis =   (len(jobs) + 1 )* ['BLACK']
    for i in deps :
        a,b = i[0], i[1]
        matrix[b].append(a)
    ans = []
    for node in jobs :
        traverse(node, matrix, vis, ans)
    for i in vis :
        if i == 'GRAY' :
            return []
    return ans

def traverse(node, matrix, vis, ans) :
    if vis[node] == 'GREEN' :
        return
    vis[node] = 'GRAY'
    for neighbour in matrix[node] :
        if 'BLACK' == vis[neighbour] :
            traverse(neighbour, matrix, vis, ans)
        if 'GRAY' == vis[neighbour] :
            return
    vis[node] = 'GREEN'
    ans.append(node)
    
        