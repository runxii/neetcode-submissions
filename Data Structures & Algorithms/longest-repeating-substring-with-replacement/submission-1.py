from collections import deque

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=r=0
        maxCount=0
        maxLen=0
        count={n:0 for n in s}
        while r<len(s):
            count[s[r]]+=1
            r+=1
            print('expand\n',count)
            maxCount=max(count.values())
            print(f'need replacement: {r-l-maxCount}')
            while l<r and r-l-maxCount>k:
                count[s[l]]-=1
                l+=1
                maxCount=max(count.values())
                print(f'max count: {maxCount}')
            maxLen=max(maxLen,r-l)
        return maxLen