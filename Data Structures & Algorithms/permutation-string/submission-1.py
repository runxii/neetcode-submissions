class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=sorted(s1)
        print(s1)
        l=0
        r=len(s1)-1
        while r<len(s2):
            clip=sorted(s2[l:r+1])

            print(clip)
            if clip==s1:
                return True
            r+=1
            l+=1

            
        return False