"""
Say you have an array prices for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""

def buy_stock(nums):
    n= len(nums)

    if n<2:
        return 0
        
    profit = 0
    min_so_far =nums[0]
    current_profit = 0
    for i in range(1,n):
        #print (f'min sofar={min_so_far} ')
        if nums[i]< min_so_far:
            min_so_far = nums[i]
        
        current_profit = nums[i] - min_so_far
        profit = current_profit + profit
        min_so_far=nums[i]
      

           
    return profit
       

if __name__=='__main__':

    nums =  [7,1,5,3,6,4]
    #Output: 7
    #Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 
    print(buy_stock(nums))
    nums =[1,2,3,4,5]
    print(buy_stock(nums))