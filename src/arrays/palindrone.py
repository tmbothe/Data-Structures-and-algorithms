def palindrone(s):

    start_index = 0
    end_index = len(s)-1

    while start_index < end_index:
        if s[start_index] != s[end_index]:
            return False
        start_index += 1
        end_index -= 1

    return True


if __name__ == '__main__':

    s = 'radar'
    print(palindrone(s))
    s = 'madam'
    print(palindrone(s))
