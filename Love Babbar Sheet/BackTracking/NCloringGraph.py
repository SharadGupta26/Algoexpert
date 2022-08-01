

#DFS Solution
#backtracking
#time O(n^V)
def checkNColoring(graph, n) :
    colors = [-1 for i in range(len(graph))]
    ans = checkNColoringHelper(graph, colors, 0, n,n)
    print(colors)
    return ans

    
def checkNColoringHelper(graph, colors, i, color, totalColors) :
    n = len(graph)
    if i == n:
        return True
    
    if color == 0 :
        return False

    if safeToAssign(graph, colors, i, color) :
        colors[i] = color
        if checkNColoringHelper(graph, colors, i+1, totalColors, totalColors) :
            return True
        else :
            colors[i] = -1

    return checkNColoringHelper(graph, colors, i, color - 1, totalColors)

def safeToAssign(graph, colors, v, color) :
    for i in range(len(graph[v])) :
        if graph[v][i] == 1 :
            if colors[i] == color :
                return False
    return True



def test() :
    graph = [
        [0,1,1,1],
        [1,0,1,0],
        [1,1,0,1],
        [1,0,1,0]
    ]

    graph2 = [
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]

    ]

    print(checkNColoring(graph2, 3))

test()