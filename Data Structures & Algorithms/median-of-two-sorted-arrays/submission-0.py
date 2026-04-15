class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=float('inf')
        ''' discussion
        1. brute-force: concatenate two array and sort it, find the median
           Time complexity: O((m+n)log(m+n))
        2. optimize: if it possible to not go through every element? (the two arrays
        are ascending separately)
        '''
        nums=sorted(nums1+nums2)
        l=len(nums1)+len(nums2)
        if l%2==0:
            return float((nums[l//2]+nums[(l//2)-1])/2)
        elif l%2!=0:
            return float(nums[(l-1)//2])
            