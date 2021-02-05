
from nose.tools import assert_equal

def mergetwolist(l1,l2):
    """
      This function merges items in two sorted arrays
    """
    n = len(l1)
    m = len(l2)

    if not (l1 and l2):
        return 
    elif not l1 or n==0:
        return l2
    elif not l2 or m==0:
        return l1

    
    l3 = []
    j=i=0

    while i<n and j<m:
        if l1[i]==l2[j]:
            l3.append(l1[i])
            l3.append(l2[j])
            i+=1
            j+=1
        elif l1[i] < l2[j]:
            l3.append(l1[i])
            i+=1
        elif l2[j] < l1[i]:
            l3.append(l2[j])
            j+=1
    
    while i<n:
        l3.append(l1[i])
        i+=1

    while j<m:
        l3.append(l2[j])
        j+=1
    
    return l3

class mergeTwoListTest(object):
    def test(self,sol):
        assert_equal(sol( [1,2,4],[1,3,4]),[1,1,2,3,4,4])
        assert_equal(sol( [0,3,4,31],[4,6,30]),[0,3,4,4,6,30,31])

        print('ALL TEST CASES PASSED')

if __name__=='__main__':
    
    t = mergeTwoListTest()
    t.test(mergetwolist)