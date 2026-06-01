class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        subset=[]
        '''
        * main idea: for each element, only 2 possibilities
            - include the element
            - do not include the element
            -> binary tree for decision making
        * input: the index of current element that we're handling
        * output: subset, only return when reach the leaf node
            - how to find leaf node: when index>=len(nums)
        '''
        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            # include current element
            subset.append(nums[i])
            dfs(i+1)

            # do not include current element
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res