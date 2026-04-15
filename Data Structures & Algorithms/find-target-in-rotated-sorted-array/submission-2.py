class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)//2
            # if mid==target, found, and return index
            if nums[m]==target:
                return m
            # if mid<target:
            elif nums[m]<target:
                # 1. target<tail: shrink left bound to mid
                if target<nums[r]:
                    l=m+1
                # 2. target>tail: shrink right bound
                elif target>nums[r]:
                    r-=1
                elif target==nums[r]:
                    return r
            # if mid>target, two possible condition:
            elif nums[m]>target:
                # 1. target<tail, shrink right bound
                if target<nums[r]:
                    r-=1
                # 2. target>tail, shirnk right bound
                elif target>nums[r]:
                    r=m-1
                elif target==nums[r]:
                    return r

        return -1