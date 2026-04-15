class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        ma=0
        while left<right:
            a=(right-left)*min(heights[left],heights[right])
            #print(f'this area: {a}, current max area: {ma}')
            ma=max(ma,a)
            #print(f'new max area')
            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1
        
        return ma