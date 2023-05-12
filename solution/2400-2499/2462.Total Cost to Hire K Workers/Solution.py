class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        i, j = candidates - 1, n - candidates
        q = [(costs[h], h) for h in range(candidates)]
        q.extend((costs[h], h) for h in range(n - candidates, n) if h > i)
        heapify(q)
        ans = 0
        for _ in range(k):
            c, x = heappop(q)
            ans += c
            if x <= i:
                i += 1
                if i < j:
                    heappush(q, (costs[i], i))
            if x >= j:
                j -= 1
                if i < j:
                    heappush(q, (costs[j], j))
        return ans
