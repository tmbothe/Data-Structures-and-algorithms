def evalRPN(tokens):

    OPS = {
        "-" : lambda x,y : x-y,
        "+" : lambda x,y : x+y,
        "*" : lambda x,y : x*y,
        "/" : lambda x,y : int(x/y)
    }

    s= []
    for item in tokens:
        if len(s)>=2 and item in OPS:
            y = s.pop()
            x = s.pop()
            s.append(OPS[item](x,y))
        else:
            s.append(int(item))
        #print(s)
    return s.pop()


if __name__=='__main__':
    tokens = ["2","1","+","3","*"]
    #Output: 9
    #print(evalRPN(tokens))
    tokens = ["4","13","5","/","+"]  #6
    print(evalRPN(tokens))

    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    #Output: 22
    print(evalRPN(tokens))