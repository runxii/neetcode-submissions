class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)//2
            # mid>tail, rotated for (1,n-1) times, shrink left bound
            if nums[m]>nums[-1]:
                l=m+1
                #print(f'middle point: {nums[m]} is larger, shrink left bound to {nums[l]}')
            # mid<tail, shrink right found to find the min possible answer (left bound fixed)
            elif nums[m]<=nums[-1]:
                r=m-1
                #print(f'middle point: {nums[m]} is smaller, shrink left bound to {nums[r]}')

        return nums[l]