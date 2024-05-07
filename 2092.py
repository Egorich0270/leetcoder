import queue
class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        peop = [x for x in range(n)]
        def find(x):
            if x != peop[x]:
                return find(peop[x])
            else:
                return x
        def union(x, y):
            peop[find(y)] = peop[x]

        union(0, firstPerson)

        meetings.sort(key=lambda meet: meet[2])
        pre = [meetings[0]]
        i = 0
        while i < len(meetings):
            if pre[0][2] == meetings[i][2]:
                pre.append(meetings[i])
            else:
                graph = []
                visited = {x: False for x in range(n + 1)}
                for x in pre:
                    graph.append((x[0], x[1]))
                q = queue.Queue()
                for x in graph:
                    if not visited[x[0]]:
                        own_flag = False
                        path = []
                        q.put(x[0])
                        while not q.empty():
                            node = q.get()
                            visited[node] = True
                            path.append(node)
                            if find(node) == 0:
                                own_flag = True
                            for v in graph:
                                if node == v[0]:
                                    if not visited[v[1]]:
                                        q.put(v[1])
                                if node == v[1]:
                                    if not visited[v[0]]:
                                        q.put(v[0])
                        if own_flag:
                            for y in path:
                                union(0, y)
                pre = [meetings[i]]
            i += 1
        graph = []
        visited = {x: False for x in range(n + 1)}
        for x in pre:
            graph.append((x[0], x[1]))
        q = queue.Queue()
        for x in graph:
            if not visited[x[0]]:
                own_flag = False
                path = []
                q.put(x[0])
                while not q.empty():
                    node = q.get()
                    visited[node] = True
                    path.append(node)
                    if find(node) == 0:
                        own_flag = True
                    for v in graph:
                        if node == v[0]:
                            if not visited[v[1]]:
                                q.put(v[1])
                        if node == v[1]:
                            if not visited[v[0]]:
                                q.put(v[0])
                if own_flag:
                    for y in path:
                        union(0, y)
        ans = []
        for x in range(n):
            if peop[x] == 0:
                ans.append(x)
        return ans

