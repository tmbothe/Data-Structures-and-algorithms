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
