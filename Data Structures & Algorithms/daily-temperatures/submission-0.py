class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        n=len(temperatures)
        for i in range(n-1):
            for j in range(i+1,n):
                
                if temperatures[i]<temperatures[j]:
                    res.append(j-i)
                    break
                if j==n-1 and temperatures[i]>=temperatures[j]:
                    res.append(0)
        
            #print(res)            
                    
        res.append(0)
        return res