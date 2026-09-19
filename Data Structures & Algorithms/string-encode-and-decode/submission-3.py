class Solution:

    def encode(self, strs: List[str]) -> str:
        res= ""
        for s in strs:
            res+= f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:

        c = ""
        list_s = []
        i = 0
        while i < len(s):
             j = i
             while s[j] != "#":
                j += 1
             length = int(s[i:j])
             start = j + 1
             end = j + length + 1
             
             list_s.append(s[start:end])
             i = end        
        return list_s



