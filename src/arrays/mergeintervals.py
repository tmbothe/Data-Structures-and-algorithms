def merge(intervals):
    """ [summary]
       Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
       and return an array of the non-overlapping intervals that cover all the intervals in the input.

        Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
        Example 2:

        Input: intervals = [[1,4],[4,5]]
        Output: [[1,5]]
        Explanation: Intervals [1,4] and [4,5] are considered overlapping.
    """
    n = len(intervals)
    if n<=1:
        return intervals
    intervals.sort(key=lambda x : x[0])

    result = []
    current = intervals[0]
    for i in range(1,len(intervals)):
        if (current[1]<intervals[i][0]):
            result.append(current)
            current = intervals[i]
        else:
            current[0] = min(current[0],intervals[i][0])
            current[1] = min(current[1],intervals[i][1])
    result.append(current)
    return result


if __name__=='__main__'    :

    intervals=[[1,3],[2,6],[8,10],[15,18]]

    print(merge(intervals))