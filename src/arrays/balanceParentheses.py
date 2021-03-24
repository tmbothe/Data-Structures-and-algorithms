"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

def balance_check(s):

    balance={')':'(',']':'[','}':'{'}
    stack=[]

    for symbol in s:
        if symbol not in balance:
            stack.append(symbol)
        else:
            current=stack.pop()
            if balance[symbol] != current:
                return False
    return stack==[]

  


class TestBalanceCheck(object):
    
    def test(self,sol):
        assert_equal(sol('[](){([[[]]])}('),False)
        assert_equal(sol('[{{{(())}}}]((()))'),True)
        assert_equal(sol('[[[]])]'),False)
        print ('ALL TEST CASES PASSED')
        
# Run Tests

t = TestBalanceCheck()
t.test(balance_check)