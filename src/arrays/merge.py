def merge(nums1, nums2):
    # Write your code here
      
    n = len(nums1)
    m = len(nums2)

    print('The first is ', nums2)
    result =[]
    
    if n==0 and m==0:
        return result
    elif n==0 and m>0:
        return nums2
    else:
        return nums1
    
    
    i=0
    j=0
        
    while i<n and j<m:
        print(nums1)    
        print(nums2)
        if nums1[i]< nums2[j]:
            result.append(nums1[i])
            i+=1
        elif nums2[j]< nums1[i]:
            result.append(nums2[j])
            j+=1
        elif nums2[j]==nums1[i]:
            result.append(nums1[i])
            result.append(nums2[j])
            i+=1
            j+=1
    
    print('current result', result)        
    while i<n:
        result.append(nums1[i])
        i+=1
    
    while j<m:
        result.append(nums2[j])
        j+=1
        
    print('current result2', result)        
    print(nums1)    
    print(nums2)
    print(result)
    return result

if __name__=='__main__':
    nums1=[0]
    nums2=[1]

    print(merge(nums1,nums2))