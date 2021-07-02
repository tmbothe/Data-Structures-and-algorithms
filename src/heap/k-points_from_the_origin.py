import heapq
from typing import List, final
import math


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
    The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
    You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in)
    """

    result = {}
    i = 0
    for point in points:
        current = round(math.sqrt(point[0]**2 + point[1]**2), 2)
        result[i] = [current]
        i += 1

    sorted_result = sorted(result.items(), key=lambda x: x[1])

    return [points[x[0]] for x in sorted_result[:k]]


if __name__ == '__main__':
    points = [[1, 3], [-2, 2]]
    k = 1
    #Output: [[-2,2]]
    #print(kClosest(points, k))

    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2  # Output: [[3,3],[-2,4]]
    print(kClosest(points, k))

    points = [[0, 1], [1, 0]]
    k = 2
    print(kClosest(points, k))
