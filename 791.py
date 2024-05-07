class Solution:
    def customSortString(self, order: str, s: str) -> str:
        answer = ""
        end = ""
        for x in order:
            try:
                answer += s.count(x) * x
            except NameError:
                pass
        for x in s:
            if x not in order:
                answer += x

        return answer


print(Solution().customSortString('acd', "asdqqfqf"))
