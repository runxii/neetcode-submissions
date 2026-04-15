class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s)<len(t):
            return ""
        need={n:0 for n in t}
        window={n:0 for n in t}
        for n in t:
            need[n]+=1
        print(need)
        
        l=r=0
        valid=0
        minRes=""
        minLen=len(s)
        print('min len: ',minRes)
        while r<len(s):
            c=s[r]
            r+=1
            if c in need:
                window[c]+=1
                if window[c]==need[c]:
                    valid+=1
            #print(f'expand: char {c}, current window: {window}, right moved to {r}th')
            
            while l<r and valid==len(need):
                if r-l<=minLen:
                    minRes=s[l:r]
                    minLen=r-l
                c=s[l]
                l+=1
                if c in need:
                    window[c]-=1
                    if window[c]<need[c]:
                        valid-=1
                print(f'shrink: char {c}, current window: {window}, left moved to {l}th')
        return minRes
