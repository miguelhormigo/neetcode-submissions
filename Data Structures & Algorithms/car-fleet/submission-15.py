class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        last_time = None
        res = 0

        for c in cars:
            time = (target - c[0]) / c[1]

            if not last_time or time > last_time:
                last_time = time
                res += 1
        
        return res