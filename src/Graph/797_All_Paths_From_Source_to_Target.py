from typing import List
from collections import defaultdict
def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:

    if not graph:
        return 

    l=[]
    stack=[[0]]
    n=len(graph)-1
    while stack:
        print(stack)
        if stack[0][-1] == n:
            l.append(stack.pop(0))
        else:
            c=stack.pop(0)
            for i in graph[c[-1]]:
                stack.append(c+[i])
    print(stack)
    return l


if __name__=='__main__':
    graph = [[1,2],[3],[3],[]]
    #Output: [[0,1,3],[0,2,3]]
    print(allPathsSourceTarget(graph))

    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    #Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
    print(allPathsSourceTarget(graph))