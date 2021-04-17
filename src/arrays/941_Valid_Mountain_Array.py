from typing import List


def validMountainArray(arr: List[int]) -> bool:

    i = 1
    n = len(arr)
    if n < 3:
        return False

    while i < n and arr[i]-arr[i-1] > 0:
        i += 1

    if i == 1 or i == n:
        return False
    while i < n and arr[i]-arr[i-1] < 0:
        i += 1

    return i == n


if __name__ == '__main__':
    nums = [1, 3, 2]  # True
    print(validMountainArray(nums))
