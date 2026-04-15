class Solution:
    def isPalindrome(self, s: str) -> bool:
        # boolean to check if the words are the same
        same=True
        # clean string, remove all spaces and signs
        s=s.lower()
        cs=""
        for i in s:
            if i.isalpha()==True or i.isnumeric()==True:
                cs+=i
        p1=0
        p2=len(cs)-1
        while(p1<p2):
            print(f"p1:{cs[p1]},p2:{cs[p2]}")
            if cs[p1]!=cs[p2]:
                same=False
            p1+=1
            p2-=1
        return same