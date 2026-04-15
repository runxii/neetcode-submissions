class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count={n:0 for n in nums}
        print(count)
        for n in nums:
            count[n]+=1
            if count[n]>1:
                return n
        return 0