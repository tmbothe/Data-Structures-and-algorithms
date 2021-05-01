from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:

    cur = []
    ans = []
    index = 0
    n = len(nums)

    def solution(nums, ans, cur, index):
        if index >= len(nums):
            return ans.append(cur[:])

        if cur not in ans:
            ans.append(cur[:])

        for i in range(index, n):
            if i > index and nums[i-1] == nums[i]:
                continue

            cur.append(nums[i])
            solution(nums, ans, cur, i+1)
            # print(cur)
            cur.pop()

    solution(nums, ans, cur, index)

    return ans


if __name__ == '__main__':
    nums = [1, 2, 2]
    #Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
    print(subsetsWithDup(nums))
    nums = [0]
    #Output: [[],[0]]
    print(subsetsWithDup(nums))
