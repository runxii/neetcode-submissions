class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        res=[0]*n
        w=[0]
        for i in range(1,n):
            while len(w)!=0 and temperatures[i]>temperatures[w[-1]]:
                res[w[-1]]=i-w[-1]
                w.pop()
            w.append(i)

        # res.append(0)
        return res