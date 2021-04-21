from typing import List
def subsets(nums: List[int]) -> List[List[int]]:

    if len(nums)==0:
        return nums

    ans=[]
    cur=[]
    index=0

    def solution(nums,ans,cur,index):
        if index > len(nums):
            return

        ans.append(cur[:])
        for i in range(index,len(nums)):
            if nums[i] not in cur:
                cur.append(nums[i])
                solution(nums, ans, cur,i)
                cur.pop()
        return 

    solution(nums, ans, cur, index)

    return ans






if __name__=='__main__':
    nums = [1,2,3]
    # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    print(subsets(nums))