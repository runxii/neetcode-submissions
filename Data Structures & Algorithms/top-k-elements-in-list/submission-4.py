class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={num:0 for num in nums}
        freq=[[] for i in range(len(nums))]
        res=[]
        # build a count dict, store frequencies
        for num in nums:
            counts[num] +=1
        for i in range(len(counts)):
            count=list(counts.values())[i]-1
            freq[count].append(list(counts.keys())[i])
        print(freq)
        for f in freq[::-1]:
            print(f)
            for i in range(len(f)):
                print(len(res))
                res.append(f[i])
                if len(res)>=k:
                    return res
                    