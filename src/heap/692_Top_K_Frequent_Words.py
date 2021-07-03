import heapq

def topKFrequent(words,k):
    """
    Given a non-empty list of words, return the k most frequent elements.
    Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency,
    then the word with the lower alphabetical order comes first.
    """

    #1- define words count
    wordCount = {}

    for word in words:
        if word in wordCount:
            wordCount[word] +=1
        else:
            wordCount[word]=1

    word_count = [(-val,key) for key , val in wordCount.items()]

    #2 - sort result by count and alphabetical order

    heapq.heapify(word_count)

    
    #3 - return the result
    result = []
    for i in range(k):
        result.append(heapq.heappop(word_count)[1])

    return result







if __name__ == '__main__':
    words =  ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2   #Output: ["i", "love"]
    print(topKFrequent(words,k))