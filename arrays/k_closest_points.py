import heapq
from typing import List


class KClosestPoints:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        i = 0
        while i < len(points):
            x = points[i][0] * points[i][0]
            y = points[i][1] * points[i][1]
            heapq.heappush(pq, (-(x+y), points[i][0], points[i][1]))
            if len(pq) > k:
                heapq.heappop(pq)
            i += 1

        return [[x,y]  for _,x,y in pq]