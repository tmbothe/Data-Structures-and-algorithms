def twoCitySchedCost(costs):

    result={'A':[],'B':[]} 
    costs.sort(key = lambda x: x[0]-x[1]) 
    print(costs)
    n=len(costs)//2

    total = 0

    for cost in costs[:n]:
        total+=cost[0]
    for cost in costs[n:]:
        total+=cost[1]

    return total


    



if __name__ =='__main__':
    costs = [[10,20],[30,200],[400,50],[30,20]]
    print(twoCitySchedCost(costs))  #110

    costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    print(twoCitySchedCost(costs)) #1859

    costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
    print(twoCitySchedCost(costs)) #3086





