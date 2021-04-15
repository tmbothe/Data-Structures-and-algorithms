import collections

def invalidTransactions(transactions):

    seen = collections.defaultdict(list)
    invalid=set()
    

    for i,transaction in enumerate(transactions):

        name,time,amount,city = transaction.split(',')
        

        if int(amount)>1000:
            invalid.add((i,transaction))
            
        if name in seen:
            for element in seen[name]:
                name2,time2,amount2,city2 = element[1].split(',')
                j=element[0]
                if abs(int(time)-int(time2))<=60 and city!=city2:
                    invalid.add((j,element[1]))
                    invalid.add((i,transaction))
        
        seen[name].append((i,transaction))
        
    #print(invalid)
    return [t for i,t in invalid]  




if __name__ =='__main__':

    transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
    print(invalidTransactions(transactions))
    #Output: ["alice,20,800,mtv","alice,50,100,beijing"]

    transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
    print(invalidTransactions(transactions))
    #Output: ["alice,50,1200,mtv"]

    transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
    print(invalidTransactions(transactions))
    #Output: ["bob,50,1200,mtv"]

    transactions = ["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]
    #["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]
    #['alice,20,800,mtv', 'alice,51,100,frankfurt', 'alice,50,100,mtv', 'alice,51,100,frankfurt']
    print(invalidTransactions(transactions))

    transactions=["alice,20,800,mtv","bob,50,1200,mtv","alice,20,800,mtv","alice,50,1200,mtv","alice,20,800,mtv","alice,50,100,beijing"]
   
    print(invalidTransactions(transactions))

    transactions=["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]
    #["bob,689,1910,barcelona","bob,832,1726,barcelona","bob,832,1726,barcelona","bob,820,596,bangkok"]
    #['bob,689,1910,barcelona', 'bob,820,596,bangkok', 'bob,832,1726,barcelona', 'bob,832,1726,barcelona']
    print(invalidTransactions(transactions))

    transactions=["alice,20,800,mtv","bob,50,1200,mtv","alice,20,800,mtv","alice,50,1200,mtv","alice,20,800,mtv","alice,50,100,beijing"]
    #Expected : ["alice,20,800,mtv","bob,50,1200,mtv","alice,20,800,mtv","alice,50,1200,mtv","alice,20,800,mtv","alice,50,100,beijing"]
    #output   : ["alice,20,800,mtv","alice,50,100,beijing","alice,50,1200,mtv","bob,50,1200,mtv","alice,50,1200,mtv"]