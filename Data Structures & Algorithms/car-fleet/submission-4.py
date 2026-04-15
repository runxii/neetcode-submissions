class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        
        cars={}
        for i in range(n):
            cars[position[i]]=speed[i]

        fleets=sorted(position)
        # current car
        c=n-1
        while c>0:
            p=fleets[c]
            pn=fleets[c-1]
            s=cars[p]
            sn=cars[pn]
            if s>=sn:
                # never reach
                c-=1
                continue
            
            print(f'car{p}:speed {cars[p]}; car{pn}: speed {cars[pn]}')
            # reach time
            rt=(target-p)/cars[p]
            # meet time
            
            mt=(p-pn)/(sn-s)
            if rt>=mt:
                # meet, 1 fleet
                print(f'car{pn} would meet car{p} at {s*mt+p}, time {mt}.')
                cars.pop(pn)
                fleets[c-1]=fleets[c]
                print(f'current fleet: {fleets}')

            c-=1

        return len(cars)