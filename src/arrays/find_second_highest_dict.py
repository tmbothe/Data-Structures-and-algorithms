
def secondHighest(nums,n):
    '''Python program to find second maximum value in Dictionary
    '''
    sortednums=[(k, v) for k, v in sorted(nums.items(), key=lambda item: item[1])]
    
    print(sortednums)
    return sortednums[n]
    
if __name__=='__main__':
    nums ={"google":12, "amazon":9, "flipkart":4, "gfg":13}
    
    print(secondHighest(nums,-2))
    
    nums={'peter': 40,'mike': 90, 'sam': 60,'wohn': 90, 'jimmy': 32}
    print(secondHighest(nums,-3))