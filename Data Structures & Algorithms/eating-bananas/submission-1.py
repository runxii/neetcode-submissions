from math import ceil
class Solution:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # from min to max, for each k, check totalTime(k)<h
        # in the monotonic ks, if true, it is the min val
        # if false, go on until find a true k, or meet max bound
        minK=1
        maxK=max(piles)
        def totalTime(k:int)->int:
            t=0
            for p in piles:
                t+=ceil(p/k)
            return t
        while minK<maxK:
            mK=(minK+maxK)//2
            # compute total time for middle k
            tmk=totalTime(mK)
            # find result k
            if tmk<=h:
                maxK=mK
            elif tmk>h:
                # k is too small, continue to find
                minK=mK+1
        return minK            
