class Solution(object):
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Generate all valid rows
        def generate_rows(m):
            rows = []
            def backtrack(row):
                if len(row) == m:
                    rows.append(tuple(row))
                    return
                for color in range(3):
                    if not row or row[-1] != color:
                        row.append(color)
                        backtrack(row)
                        row.pop()
            backtrack([])
            return rows
        
        valid_rows = generate_rows(m)
        
        # Precompute compatible rows
        compatible = {}
        for r1 in valid_rows:
            compatible[r1] = []
            for r2 in valid_rows:
                if all(c1 != c2 for c1, c2 in zip(r1, r2)):
                    compatible[r1].append(r2)
        
        # DP
        dp = {row: 1 for row in valid_rows}  # first column
        for _ in range(1, n):
            new_dp = {row: 0 for row in valid_rows}
            for curr in valid_rows:
                for prev in compatible[curr]:
                    new_dp[curr] = (new_dp[curr] + dp[prev]) % MOD
            dp = new_dp
        
        return sum(dp.values()) % MOD
