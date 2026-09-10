class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dic1 = {}
        char_dic2 = {}
        len1 = len(s)
        len2= len(t)
        if len1 != len2:
            return False
        for i in range(len1):
            if s[i] in char_dic1:
                char_dic1[s[i]] += 1
            else:
                char_dic1[s[i]] = 1
            
            if t[i] in char_dic2:
                char_dic2[t[i]] += 1
            else:
                char_dic2[t[i]] = 1
        for i in range(len1):
            if  (s[i] not in char_dic2 or t[i] not in char_dic1) or (char_dic1[s[i]] != char_dic2[s[i]] and char_dic2[t[i]] != char_dic1[t[i]]):
                return False
        return True
            
        