from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # use a max heap, for every cycle, execute the heap top task
        '''
        * Res: total time to complete all tasks
        * What doesn't matter: Which letter(task) is handled this time
        * What matters: how many tasks are left
        '''
        c = Counter(tasks)
        # max heap
        
        h = [-x for x in c.values()]
        heapq.heapify(h)
        time = 0
        # queue, waiting to be added to the heap
        q = []
        while h or q:
            for task in q[:]:
                if task[1]==time:
                    heapq.heappush(h, task[0])
                    q.remove(task)
            if h:
                task=heapq.heappop(h)
                if task+1<0:
                    q.append((task+1, time+n+1))
                time+=1
                #print(f"time: {time}, task left: {task}, waiting queue: {q}")
                
            else:
                time+=1
                #print(f"time: {time}, idle")

        return time