class TimeMap:

    def __init__(self):
        self.kvdict: dict[list[tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kvdict.setdefault(key, []).append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kvdict:
            return ""
        
        v = self.kvdict[key]
        l, r = 0, len(v) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if v[m][0] <= timestamp:
                res = v[m][1]
                l = m + 1
            else:
                r = m - 1
        return res