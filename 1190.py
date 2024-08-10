class Solution:
    def reverseParentheses(self, s: str) -> str:
        while '(' in s:
            p1 = s.index('(')
            p2 = p1
            for x in range(p1, len(s)):
                if s[x] == '(':
                    p1 = x
                if s[x] == ')':
                    p2 = x
                    break

            s = s.replace(s[p1:p2 + 1:], s[p2 - 1:p1:-1])
        return s


print(Solution().reverseParentheses('lol(a(sd))'))