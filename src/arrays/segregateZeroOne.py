from collections import defaultdict


def segregate(nums):
    numberCount = defaultdict(int)

    for num in nums:
        numberCount[num] += 1

    zero = [0]*numberCount[0]
    one = [1]*numberCount[1]

    return zero+one


if __name__ == '__main__':
    array = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
    # Output array =  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    print(segregate(array))
