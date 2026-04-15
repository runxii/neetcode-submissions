class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        c1=[0]*26
        c2=[0]*26
        
        l=r=0
        for i in range(len(s1)):
            c1[ord(s1[i])-97]+=1
            c2[ord(s2[i])-97]+=1
            r+=1
        if c2==c1:
                return True
        while r<len(s2):
            c2[ord(s2[r])-97]+=1
            c2[ord(s2[l])-97]-=1
            r+=1
            l+=1
            if c2==c1:
                return True

            
            
            #print(f'{s2[l]} count-1, now is {c2[s2[l]]}')
            
            
            
            #print(f'{s2[r]} count+1, now is {c2[s2[r]]}')
            
            
        return False