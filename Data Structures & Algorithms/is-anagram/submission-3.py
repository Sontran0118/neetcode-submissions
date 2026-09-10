class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_dic1 = {}
        char_dic2 = {}

        for i in range(len(s)):
            char_dic1[s[i]] = char_dic1.get(s[i], 0) + 1
            char_dic2[t[i]] = char_dic2.get(t[i], 0) + 1

        return char_dic1 == char_dic2