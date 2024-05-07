from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        dict_of_chars = {}
        for x in arr:
            if x in dict_of_chars.keys():
                dict_of_chars.update({x: dict_of_chars[x] + 1})
            else:
                dict_of_chars.update({x: 1})
        if len(set(arr)) == len(set(dict_of_chars.values())):
            return True
        else:
            return False
    #Можно использовать Counter из стандартной библиотеки
    def uniqueOccurrences2(self, arr: list[int]) -> bool:
        return (len(set(Counter(arr).values())) == len(set(Counter(arr).keys())))



print(Solution().uniqueOccurrences2([-3,0,1,-3,1,1,1,-3,10,0]))
