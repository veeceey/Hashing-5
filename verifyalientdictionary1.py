"""
https://leetcode.com/problems/verifying-an-alien-dictionary/submissions/
"""


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ###tc o(m+n) where m is the length of words, n is constant hashmap 26 values only
        ##space can also be treated constant
        hashmap = {}
        for i, o in enumerate(order):
            hashmap[o] = i
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(len(word1)):
                if j == len(word2):
                    ###we reached the end of word 2 while word1 is still left, this could mean word 2 is a prefix of word 1 whcih is false
                    return False
                if word1[j] != word2[j]:
                    ##found first differing char
                    if hashmap[word2[j]] < hashmap[word1[j]]:
                        return False
                    ##we might have more words left but no need, we should break as we found the first differing char
                    break

        return True



