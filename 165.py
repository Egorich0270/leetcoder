class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = []
        for x in version1.split("."):
            v1.append(int(x))

        for i, x in enumerate(version2.split(".")):
            try:
                if v1[i] > int(x):
                    return 1
                if v1[i] < int(x):
                    return -1
            except IndexError:
                if int(x) != 0:
                    return -1

        for x in range(i + 1, len(v1)):
            if v1[x] != 0:
                return 1

        return 0

print(Solution().compareVersion("1.1.20", "1.1.2"))