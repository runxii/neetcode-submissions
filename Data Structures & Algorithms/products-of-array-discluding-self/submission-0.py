class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1 for i in range(len(nums))]
        print(res)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i!=j):
                    res[i]*=nums[j]
                else:
                    res[i]*=1
        return res