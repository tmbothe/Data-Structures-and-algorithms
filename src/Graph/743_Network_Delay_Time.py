from typing import List
import heapq
import  collections 

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:

    g = collections.defaultdict(list)
    for u,v,cost in times:
        g[u].append((cost,v))
    
    min_heap=[(0,k)]
    visited=set()

    distance = {i:float('inf') for i in range(1,n+1)}

    distance[k]=0

    while min_heap:
        cur_dist,u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)

        if len(visited)==n:
            return cur_dist
        for direct_distance,v in g[u]:
            if cur_dist+direct_distance < distance[v] and v not in visited:
                distance[v] = cur_dist+direct_distance
                heapq.heappush(min_heap,(distance[v],v))
    return -1











if __name__=='__main__':
     times = [[2,1,1],[2,3,1],[3,4,1]]
     n = 4
     k = 2    #Output: 2
     print(networkDelayTime(times,n,k))
