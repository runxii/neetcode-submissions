class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        arr=[]
        for r in range(row):
            arr.extend(matrix[r])
        l=0
        r=len(arr)-1
        
        while l<=r:
            m=l+(r-l)//2
            # found target
            if arr[m]==target:
                return True
            # target is in bigger half
            elif arr[m]<target:
                l=m+1
            # target is in smaller half
            elif arr[m]>target:
                r=m-1
        return False