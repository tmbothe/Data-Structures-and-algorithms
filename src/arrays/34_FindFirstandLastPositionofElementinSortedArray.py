
from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:

    def binarySearch(nums, low, high, target):

        while low <= high:
            mid = (low+high)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
            elif nums[mid] < target:
                low = mid+1

        return -1

    firstPos = binarySearch(nums, 0, len(nums)-1, target)

    if firstPos == -1:
        return [-1, -1]

    endPos = firstPos
    startPos = firstPos
    temp1 = None
    temp2 = None

    while startPos != -1:
        temp1 = startPos
        startPos = binarySearch(nums, 0, startPos-1, target)
    startPos = temp1

    while endPos != -1:
        temp2 = endPos
        endPos = binarySearch(nums, endPos+1, len(nums)-1, target)
    endPos = temp2

    return [startPos, endPos]


if __name__ == '__main__':

    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    #Output: [3,4]
    print(searchRange(nums, target))
