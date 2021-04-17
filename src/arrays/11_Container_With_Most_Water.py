from typing import List


def maxArea(height: List[int]) -> int:
    left, right = 0, len(height)-1

    n = len(height)

    if n <= 1:
        return 0
    maxarea = -float('inf')

    while left <= right:
        currentarea = min(height[left], height[right])*(right-left)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        maxarea = max(maxarea, currentarea)
    return maxarea


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]  # Output: 49
    print(maxArea(height))
