class Solution:
    def distance(self, point: List[int]) -> int:
        return sqrt(point[0]^2+point[1]^2)
    def swap(self, points: List[List[int]], i1: int, i2: int):
        points[i1], points[i2] = points[i2], points[i1]
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        maintain a max heap with size k
        0. if len(points)==0: return None
           if len==1 and k==1: return the point
        1. for every point in points:
            - push the point to the heap
            - bubble up the point
            - if heap.size>k: 
                * swap the root (index=0) and last
                * pop the last
                * bubble down the current root
        2. return all points in the heap

        bubble up:
        input: index
        output: None (in-place swap)
        1. calculate the distance of the point and the parent point:
        2. if distance>parent_distance: 
            - swap this and this.parent
            - bubble up this.parent

        bubble down:
        input: index
        output: None
        1. calculate the distance of this and this.left_child and this.right_child
        2. check if left and right exist
        3. find the index with smaller distance
        4. if this.distance<smaller distance:
            - swap this and smaller
            - bubble down smaller.index
        '''
        maxHeap=[]
        for x, y in points:
            dist = -(x**2+y**2)
            heapq.heappush(maxHeap, [dist, x, y])
            if len(maxHeap)>k:
                heapq.heappop(maxHeap)
        res=[]
        while maxHeap:
            dist, x, y=heapq.heappop(maxHeap)
            res.append([x,y])
        return res
        