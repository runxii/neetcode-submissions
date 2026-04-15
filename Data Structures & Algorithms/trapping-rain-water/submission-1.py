class Solution:
    def trap(self, height: List[int]) -> int:
        sa=0
        n=len(height)
        l=0
        r=n-1
        hl=height[l]
        hr=height[r]

        while l<r:
            if height[l]<height[r]:
                
                a=max(0,min(hl,hr)-height[l])
                #print(f'{l}th bar, left max: {hl}, right max:{hr} contains {a} water')
                sa+=a
                l+=1
                hl=max(hl,height[l])
            else:
                a=max(0,min(hl,hr)-height[r])
                #print(f'{r}th bar, left max: {hl}, right max:{hr} contains {a} water')
                sa+=a
            
                r-=1
                hr=max(hr,height[r])

                
        return sa
        
