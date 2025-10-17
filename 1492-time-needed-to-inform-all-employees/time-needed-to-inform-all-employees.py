class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                tree[manager[i]].append(i)

        def dfs(emp):
            if not tree[emp]:
                return 0
            return max(dfs(sub) for sub in tree[emp]) + informTime[emp]

        return dfs(headID)