class Solution:
    def isValid(self, s: str) -> bool:
        def anti(s):
            if s == '(':
                return ')'
            elif s == '{':
                return '}'
            elif s == '[':
                return ']'
            else:
                return ' '
        flag = True
        sc = []
        for x in s:
            if len(sc) == 0:
                sc.append(x)
                continue
            a = sc.pop()
            if anti(a) == x:
                continue
            else:
                sc.append(a)
                sc.append(x)
        return len(sc) == 0








print(Solution().isValid("([{{}}])"))