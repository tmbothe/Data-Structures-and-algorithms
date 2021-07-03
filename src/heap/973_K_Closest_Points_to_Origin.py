from typing import List
import collections 
import math
import heapq

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
    The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
    You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
    """

    def point_distance(points):
        result = collections.defaultdict(int)

        i=0
        for point in points:
            result[i] = math.sqrt(point[0]**2+point[1]**2)
            i+=1

        return [(val,k) for k,val in result.items()]

    distance = point_distance(points)
    heapq.heapify(distance)

    final = []

    for k in range(k):
        current = heapq.heappop(distance)[1]
        final.append(points[current])


    print(distance)
    return final






if __name__ =='__main__':

    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    #Output: [[3,3],[-2,4]]
    print(kClosest(points,k))


