class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max_pile = max(piles)
        l = 1
        r = max_pile
        res = r
        while l <= r:
            m = (l+r)//2
            time = sum(math.ceil(s/m) for s in piles)
            if time <= h:
                res = min(res,m)
                r = m-1
            else:
                l = m+1
        return res


        