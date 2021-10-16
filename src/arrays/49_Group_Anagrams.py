from collections import defaultdict


def groupAnagrams(s):

    if len(s) == 1:
        # print(s)
        return [s]
    anagram_map = defaultdict(list)
    for word in s:
        current = ''.join(sorted(word))
        anagram_map[current].append(word)

    return [val for key, val in anagram_map.items() if len(val) > 1]


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    #Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(groupAnagrams(strs))

    strs = [""]
    #Output: [[""]]
    print(groupAnagrams(strs))

    strs = ["a"]
    #Output: [["a"]]
    print(groupAnagrams(strs))
