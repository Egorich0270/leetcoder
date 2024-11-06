class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda z: z[0])
        deap = None
        arr = 0
        for x in points:
            if not deap:
                deap = x
            else:
                if x[0] <= deap[1]:
                    deap = [x[0], min(x[1], deap[1])]
                else:
                    deap = x
                    arr += 1
        return arr+1





        pass



print(Solution().findMinArrowShots([[2,3],[1,2],[3,4]]))