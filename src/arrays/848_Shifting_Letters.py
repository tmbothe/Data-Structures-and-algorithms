import string

def shiftingLetters(s, shifts):
    alphabet = string.ascii_lowercase

    sdict ={i:val for i,val in enumerate(s)}
    shift = 0
    
    for i in range(len(s)-1,-1,-1):
        shift = (shift+shifts[i])%26
        sdict[i] = chr((ord(sdict[i])-97+shift)%26+97)


       
    return ''.join(sdict.values())






if __name__ == '__main__':

    s = "abc"
    shifts = [3,5,9]
    #Output: "rpl"
    print(shiftingLetters(s,shifts))

    s = "aaa"
    shifts = [1,2,3]
    #Output: "gfd"
    print(shiftingLetters(s,shifts))

    s = "bad"
    shifts = [10,20,30]
    print(shiftingLetters(s,shifts))


