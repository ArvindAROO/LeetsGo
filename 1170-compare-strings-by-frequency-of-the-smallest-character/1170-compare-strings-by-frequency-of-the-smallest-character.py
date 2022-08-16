from bisect import bisect
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        for i in range(len(words)):
            word = words[i]
            word = sorted(list(word))
            words[i] = word.count(word[0])
        for i in range(len(queries)):
            query = queries[i]
            query = sorted(list(query))
            queries[i] = query.count(query[0])
        
        words.sort()
        l = len(words)
        
        for i in range(len(queries)):
            queries[i] = l - bisect(words, queries[i])
        return queries
