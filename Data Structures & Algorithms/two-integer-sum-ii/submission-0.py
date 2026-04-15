class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1=0
        p2=1
        
        for i in range(len(numbers)-1):
            rest=target-numbers[i]
            if rest in numbers[i+1:len(numbers):]:
                return [i+1,numbers.index(rest)+1]
            