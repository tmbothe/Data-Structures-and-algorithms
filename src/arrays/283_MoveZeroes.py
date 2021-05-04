from typing import List


def moveZeroes(nums: List[int]) -> None:

    if len(nums) == 0:
        return
    j = 0
    n = len(nums)

    for num in nums:
        if num != 0:
            nums[j] = num
            j += 1

    while j < n:
        nums[j] = 0
        j += 1

    return nums


if __name__ == '__main__':

    nums = [0, 1, 0, 3, 12]
    print(moveZeroes(nums))
