def simplifyPath(path):

    if not path:
        return
    
    s = []
    #s.append('/')
    for item in path.split('/'):
        if s and item =='..':
            s.pop()
        if item in ['.','..'] or not item:
            continue
        else:
            s.append(item)
    final_str = "/"+"/".join(s)
    return final_str
    





if __name__=='__main__':
    path = "/home/"
    #Output: "/home"
    print(simplifyPath(path))
    path = "/../"
    print(simplifyPath(path))
    path = "/a/./b/../../c/"
    print(simplifyPath(path))
    path = "/home//foo/"
    print(simplifyPath(path))