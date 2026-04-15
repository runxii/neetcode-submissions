class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for s in strs:
            res=res+s+'/'
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        # substring stack
        r=''
        for char in s:
            if char=='/':
                res.append(r)
                r=''
            else:
                r=r+char
            

        return res