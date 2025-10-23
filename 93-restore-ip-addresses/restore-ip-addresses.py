class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []

        def backtrack(start, path):

            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break

                segment = s[start : start + length]

                if len(segment) > 1 and segment[0] == "0":
                    continue

                if int(segment) > 255:
                    continue

                backtrack(start + length, path + [segment])

        backtrack(0, [])
        return res
