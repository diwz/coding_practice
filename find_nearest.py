# For given 'center' point returns a subset of 'p' stored points
# that are closer to the center than others.

# E.g.
# Stored:
# (1, 1)
# (0, 3)
# (0, 4)
# (0, 5)
# (0, 6)
# (0, 7)

# findNearest(new Point(0, 0), 3) -> (1, 1), (0, 3), (0, 4)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

import heapq

class Plane:
    def __init__(self):
        self.points = {}

    def addPoint(self, point):
        self.points[point] = self.points.get(point, 0) + 1


    def findNearest(self, center, p):
        def getDistance(p):
            return (center.x-p.x)**2 + (center.y-p.y)**2

        heap = []
        for k, v in self.points.items():
            heapq.heappush(heap, (getDistance(k), k))
            if len(heap) > p:
                heap = heapq.nsmallest(p, heap)
        res = []
        k = p
        while p > 0:
            nearest = heapq.heappop(heap)[1]
            n = self.points[nearest]
            p -= n

            while n > 0:
                res.append(nearest)
                n -= 1

        return res[:k]

if __name__ == '__main__':
    plane = Plane()
    plane.addPoint(Point(1,1))
    plane.addPoint(Point(0,3))
    plane.addPoint(Point(0,3))
    plane.addPoint(Point(0,4))
    plane.addPoint(Point(0,5))
    plane.addPoint(Point(0,6))
    plane.addPoint(Point(0,7))

    for p in plane.findNearest(Point(0, 0), 4):
        print p

