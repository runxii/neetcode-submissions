class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        compute={'+':lambda x,y:x+y,
        '-':lambda x,y:x-y,
        '*':lambda x,y:x*y,
        '/':lambda x,y:x/y
        }
        numbers=[]
        for t in tokens:
            if t in compute:
                # check if the numbers can be computed, if so, store new result
                if len(numbers)>=2:
                    b=numbers.pop()
                    a=numbers.pop()
                    numbers.append(int(compute[t](a,b)))
                    print(numbers)

            else:
                numbers.append(int(t))
                print(numbers)


        return numbers[0]