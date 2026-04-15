class Solution:
    def isValid(self, s: str) -> bool:
        valid=False
        stack=[]
        # parentheses mapping
        p={'(':')','{':'}','[':']'}
        
        n=len(s)
        for c in s:
            if c in p.keys():
                #print(f'{c} is left part.')
                stack.append(c)

            if c in p.values():
                #print(f'{c} is right part.')

                if len(stack)==0:
                    return False
                last=stack.pop()
                print(f'Find match "{last}"')
                if c==p[last]:
                    valid=True
                    print(f'Matched:{c}')
                else:
                    return False
        if len(stack)!=0:
            return False

        return valid