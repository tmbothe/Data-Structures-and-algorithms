def plus_one(nums):
    """write a program which takes as input an array of digits encoding a non negative
       decimal integer D and updates the array to represent D+1. For example (1,2,9)->(1,3,0)

    Args:
        nums (array): [array of integer]
    """
    nums[-1] += 1
    n = len(nums)
    for i in range(n-1, -1, -1):
        if nums[i] != 10:
            break
        nums[i] = 0
        nums[i-1] += 1
    if nums[0] == 10:
        nums[0] = 1
        nums.append(0)
    return nums


if __name__ == '__main__':
    nums = [1, 2, 9]
    print(plus_one(nums))  # [1,3,0]

    nums = [4, 3, 2, 1]  # Output: [4,3,2,2]
    print(plus_one(nums))
