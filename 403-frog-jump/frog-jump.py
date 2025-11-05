class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        dp = {stone: set() for stone in stones}
        dp[0].add(0)

        for stone in stones:
            for jump in dp[stone]:
                for next_jump in [jump - 1, jump, jump + 1]:
                    if next_jump > 0 and stone + next_jump in stone_set:
                        dp[stone + next_jump].add(next_jump)

        return any(dp[stones[-1]])
