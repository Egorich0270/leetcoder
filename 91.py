class Solution:
    def numDecodings(self, s: str) -> int:
        def it_pair(pair):
            match pair:
                case '10':
                    return True
                case '11':
                    return True
                case '12':
                    return True
                case '13':
                    return True
                case '14':
                    return True
                case '15':
                    return True
                case '16':
                    return True
                case '17':
                    return True
                case '18':
                    return True
                case '19':
                    return True
                case '20':
                    return True
                case '21':
                    return True
                case '22':
                    return True
                case '23':
                    return True
                case '24':
                    return True
                case '25':
                    return True
                case '26':
                    return True

                case _:
                    return False

        a1 = 0
        a2 = 1
        a3 = 0
        char = s[0]
        if char != '0':
            a1 = 1
        else:
            return 0
        for i in range(1, len(s)):
            a3 = a2
            a2 = a1
            a1 = 0
            char = s[i]
            if char != '0':
                a1 += a2
            if it_pair(s[i - 1] + char):
                a1 += a3
            if a1 == 0:
                return 0



        return a1

print(Solution().numDecodings('1011'))