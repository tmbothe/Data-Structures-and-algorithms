'''
histogram([2, 3, 6, 5])
'''


def histogram(nums):
    if len(nums) == 0:
        return

    for num in nums:
        output = ''
        while num > 0:
            output += '*'
            num -= 1
        print(output)
    return ''


if __name__ == '__main__':
    print(histogram([2, 3, 6, 5]))
