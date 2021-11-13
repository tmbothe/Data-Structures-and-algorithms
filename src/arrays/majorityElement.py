from collections import defaultdict


def majority_element(nums):
    result = defaultdict(int)

    for num in nums:
        result[num] += 1

    for num in result:
        if result[num] > len(nums)/2:
            return num
    return False


if __name__ == '__main__':

    nums = [1, 2, 3, 3, 3, 3, 10]  # , x = 3
    # Output: True (x appears more than n/2 times in the given array)
    print(majority_element(nums))

    nums = [1, 1, 2, 4, 4, 4, 6, 6]  # , x = 4
    # Output: False (x doesn't appear more than n/2 times in the given array)
    print(majority_element(nums))

    nums = [1, 1, 1, 2, 2]  # , x = 1
    # Output: True (x appears more than n/2 times in the given array)
    print(majority_element(nums))
