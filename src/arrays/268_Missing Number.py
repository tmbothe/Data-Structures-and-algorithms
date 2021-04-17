def missing_number(nums):
    n = len(nums)+1

    numset = set(nums)

    for num in range(n):
        if num not in numset:
            return num


if __name__ == '__main__':
    nums = [3, 0, 1]  # 2
    print(missing_number(nums))

    nums = [0, 1]  # 2
    print(missing_number(nums))
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]  # 8
    print(missing_number(nums))
    nums = [0]  # 1
    print(missing_number(nums))
