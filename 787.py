class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        prises = []
        for x in range(n):
            prises.append([float('inf')] * n)
        for flight in flights:
            prises[flight[0]][flight[1]] = flight[2]
        visited = []
        node = src
        neib = []
        for i in range(n):
            if prises[src][i] < float('inf'):
                neib.append(i)



        for l in range(k):
            print('k', l)
            new_neib = []
            while neib:
                node = neib.pop(0)
                print(node)
                if node in visited or node in neib:
                    continue
                else:
                    for x in range(len(prises[node])):
                        if prises[node][x] < float("inf"):
                            new_neib.append(x)
                            prises[src][x] = min(prises[src][x], prises[src][node] + prises[node][x])
                    visited.append(node)
            neib = new_neib
        if prises[src][dst] == float("inf"):
            return -1
        else:
            return prises[src][dst]










print(Solution().findCheapestPrice(n = 4, flights =[[0,1,1],[0,2,5],[1,2,1],[2,3,1]], src = 0, dst = 3, k = 1))