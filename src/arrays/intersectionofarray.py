def intersect(nums1, nums2):
          
    inter=[]
    results = {}
    
    for num in nums1:
        
        if num in results:
            results[num] +=1
        else:
            results=1
            
    for num in nums2:
        if num in results and results[num]>0:
            results[num]-=1
            inter.append(num)
    return inter


if __name__=='__main__':
    nums1 = [1,2,2,1]
    nums2 = [2,2]

    print(intersect(nums1,nums2))