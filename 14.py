class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prf = strs[0]
        for x in strs:
            new_prf = ''
            for i in range(min(len(prf), len(x))):
                if prf[i] == x[i]:
                    new_prf += x[i]
                else:
                    break
            if new_prf:
                prf = new_prf
            else:
                prf = new_prf
                break

        return  prf

print(Solution().longestCommonPrefix(['1231231414', '12312314', '12312424']))