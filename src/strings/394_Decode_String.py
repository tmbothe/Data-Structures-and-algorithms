from typing import List


def decodeString(s: str) -> str:

    num_stack, word_stack, word, num = [], [], '', ''

    for symbol in s:
        if symbol.isdigit():
            num += symbol
        elif symbol.isalpha():
            word += symbol
        elif symbol == '[':
            num_stack.append(int(num))
            word_stack.append(word)
            word, num = '', ''
        elif symbol == ']':
            word = word_stack.pop() + num_stack.pop()*word
    return word


if __name__ == '__main__':
    s = "3[a]2[bc]"  # Output: "aaabcbc"
    print(decodeString(s))

    s = "3[a2[c]]"  # Output: "accaccacc"
    print(decodeString(s))

    s = "2[abc]3[cd]ef"  # Output: "abcabccdcdcdef"
    print(decodeString(s))
    s = "abc3[cd]xyz"  # Output: "abccdcdcdxyz"
    print(decodeString(s))
