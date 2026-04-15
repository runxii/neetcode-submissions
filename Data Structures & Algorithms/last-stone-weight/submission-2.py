class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        remain=len(stones)
        while remain>1:
            stones.sort()
            #print(f'original: {stones}')
            x=stones.pop()
            y=stones.pop()
            #print(f'x: {x}, y:{y}')
            if x==y:
                # both destoryed
                remain-=2
            else:
                stones.append(abs(x-y))
                remain-=1
        if remain==0:
            return 0
        return stones[0]