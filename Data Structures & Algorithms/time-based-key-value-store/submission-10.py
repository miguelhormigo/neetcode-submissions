from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.d:
            self.d[key] = [[timestamp, value]]
        else:
            self.d[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.d.get(key, [])
        l, r = 0, len(values) - 1
        res = ''

        while l <= r:
            m = (l + r) // 2
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1

        return res