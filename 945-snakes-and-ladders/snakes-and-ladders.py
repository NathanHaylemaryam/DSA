class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        arr = [-1]
        left_to_right = True
        for r in range(n - 1, -1, -1):
            row = board[r]
            if not left_to_right:
                row = row[::-1]
            arr.extend(row)
            left_to_right = not left_to_right

        q = deque([(1, 0)])
        visited = {1}

        while q:
            square, moves = q.popleft()
            if square == n * n:
                return moves
            for dice in range(1, 7):
                next_square = square + dice
                if next_square > n * n:
                    continue
                if arr[next_square] != -1:
                    next_square = arr[next_square]
                if next_square not in visited:
                    visited.add(next_square)
                    q.append((next_square, moves + 1))
        return -1






