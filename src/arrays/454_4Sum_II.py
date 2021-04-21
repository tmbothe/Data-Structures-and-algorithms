from typing import List

def fourSumCount(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

    mapping = {}
    ans=0

    for i in range(len(nums1)):
        x = nums1[i] 
        for j in range(len(nums2)):
            y = nums2[j]
            if (x+y) not in mapping:
                mapping[x+y]=0
            mapping[x+y]+=1


    for i in range(len(nums3)):
        x=nums3[i]
        for j in range(len(nums4)):
            y = nums4[j]
            target=-(x+y)
            if target in mapping:
                ans+=mapping[target]
    #print(mapping)
    return ans






if __name__=='__main__':

    nums1 = [1,2]
    nums2 = [-2,-1]
    nums3 = [-1,2]
    nums4 = [0,2]
    #Output: 2
    print(fourSumCount(nums1,nums2,nums3,nums4))