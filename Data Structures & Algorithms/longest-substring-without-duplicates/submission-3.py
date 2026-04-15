from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sl=list(s)
        l=r=0
        visited=deque()
        maxLen=0
        while r<len(s):
            while l<r and sl[r] in visited:
                visited.popleft()
                l+=1
                print(f'left:{l}, right:{r}, visited:{visited}')
            visited.append(sl[r])
            r+=1
            print(f'left:{l}, right:{r}, visited:{visited}')
            maxLen=max(maxLen,len(visited))
            

            
            
        return maxLen