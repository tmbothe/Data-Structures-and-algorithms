def leader_in_array(nums):
    """[summary]

    Args:
        nums ([type]): [description]
    """
    res = []
    n = len(nums)-1
    max_so_far = nums[n]
    res.append(max_so_far)

    for i in range(n-1, -1, -1):
        if nums[i] > max_so_far:
            max_so_far = nums[i]
            res.append(max_so_far)
    return res


if __name__ == '__main__':
    nums = [16, 17, 4, 3, 5, 2]
    # leaders are 17, 5 and 2.
    print(leader_in_array(nums))

    nums = [7, 6, 4, 5, 0, 1]
    print(leader_in_array(nums))
    #7, 6, 5 and 1
