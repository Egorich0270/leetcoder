class Solution:
    def minOperations(self, logs: list[str]) -> int:
        deap = 0
        for command in logs:
            if command == '../':
                if deap > 0:
                    deap -= 1
            elif command == "./":
                continue
            else:
                deap += 1
        return deap



print(Solution().minOperations(["./","../","./"]))