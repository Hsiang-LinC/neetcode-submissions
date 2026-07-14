class CountSquares:
    '''
        When query, check if there are diagnal points (abs(x1-x2) == abs(y1-y2)).
        If so, check if the rest 2 points exist as well.
        Since duplicate are allowed and counted as different points, use list instead of hashmap. 
    '''

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] = self.points.get(tuple(point), 0) + 1

    def count(self, point: List[int]) -> int:
        counts = 0
        for p in self.points.keys():
            # check diagnal
            if p != tuple(point) and abs(p[0] - point[0]) == abs(p[1] - point[1]):
                #check rest 2 points
                if (p[0], point[1]) in self.points.keys() and (point[0], p[1]) in self.points.keys():
                    counts += self.points[p] * self.points[(p[0], point[1])] * self.points[(point[0], p[1])]
        return counts