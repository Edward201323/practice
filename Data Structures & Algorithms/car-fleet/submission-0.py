class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we have to sort the list to detect fleets.
        # If we don't sort, we can only get the time it takes to reach target assuming that cars can go in front of another
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort()

        # (target - position[i]) / speed[i]
        # the time that I get should be greater than the minimum
        # if the time is faster, it implies that it merged with another existing fleet

        # im going to first take the top value in the array
        max_time = (target - cars[-1][0]) / cars[-1][1] # [0] is the position
        cars.pop()
        sol = 1
        while cars:
            curr = (target - cars[-1][0]) / cars[-1][1]
            if curr > max_time:
                max_time = curr
                sol += 1

            cars.pop()

        # (0, 1), (1, 2), (4, 2), (7,1)
        # 3, 3, 4.5, 10
        

        return sol