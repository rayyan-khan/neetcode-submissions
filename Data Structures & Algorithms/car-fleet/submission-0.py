class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        times = []

        for car in cars:
            time_to_finish = (target - car[0]) / car[1]
            times.append(time_to_finish)
        
        fleets = []
        for time in times:
            if fleets and fleets[-1] >= time:
                continue
            else:
                fleets.append(time)

        return len(fleets)


        