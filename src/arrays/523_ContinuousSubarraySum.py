from typing import List

def checkSubarraySum(nums: List[int], k: int) -> bool:
    
    if k==0:
        return False
    sum=0
    result={}

    for i in range(len(nums)):
        sum+=nums[i]
        sum=sum%k
        if sum in result:
            if (i-result[sum]) >=1:
                return True
        else:
            result[sum]=i
    print(result)
    return False


if __name__=='__main__':
    nums = [23,2,6,4,7]
    k = 6 #True
    print(checkSubarraySum(nums,k))
    nums = [23,2,6,4,7]
    k = 13 #False
    print(checkSubarraySum(nums,k))

    nums=[23,6,9]
    k= 6
    #print(checkSubarraySum(nums,k))
    nums=[5,0,0,0]
    k= 3

    nums=[0,1,0,3,0,4,0,4,0]
    k = 5
    print(checkSubarraySum(nums,k))