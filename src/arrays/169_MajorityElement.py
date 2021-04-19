from collections import defaultdict
from typing import List


def majorityElement(nums: List[int]) -> int:

    majorityList =defaultdict(int)

    for num in nums:
        majorityList[num]+=1

    for num in majorityList:
        if majorityList[num] > len(nums)/2:
            return num



if  __name__=='__main__':
    nums = [3,2,3] #3
    print(majorityElement(nums))

    nums = [2,2,1,1,1,2,2] #2

    print(majorityElement(nums))