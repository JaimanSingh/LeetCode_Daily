1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        if not grid:
4            return 0
5
6        rows, cols = len(grid), len(grid[0])
7        visit = set()
8        islands = 0
9
10        def bfs(r, c):
11            q = collections.deque()
12            visit.add((r, c))
13            q.append((r, c))
14
15            while q:
16                row, col = q.popleft()
17                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
18
19                for dr, dc in directions:
20                    r, c = row + dr, col + dc
21
22                    if (
23                        r in range(rows)
24                        and c in range(cols)
25                        and grid[r][c] == "1"
26                        and (r, c) not in visit
27                    ):
28                        q.append((r, c))
29                        visit.add((r, c))
30
31        for r in range(rows):
32            for c in range(cols):
33                if grid[r][c] == "1" and (r, c) not in visit:
34                    bfs(r, c)
35                    islands += 1
36
37        return islands