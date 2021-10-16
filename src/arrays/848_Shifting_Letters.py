<<<<<<< HEAD
def shiftingLetters(s, shifts):

    char_index = {key: val for key, val in enumerate(s)}
    # print(char_index)
    for i in char_index:

        currentshit = shifts[i]
        # print(f'curent shif={currentshit} , sh={ord(char_index[i])+currentshit}')

        if i == 0:
            char_index[i] = chr((ord(char_index[i])+currentshit))
        else:
            j = i
            while j >= 0:
                char_index[j] = chr((ord(char_index[j])+currentshit))
                j -= 1
    return ''.join(char_index.values())


if __name__ == '__main__':
    s = "abc"
    shifts = [3, 5, 9]
    # Output: "rpl"
    print(shiftingLetters(s, shifts))
=======
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


>>>>>>> 7937dc76c60a57e5809d3457425c44542e446cf4
