class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        visited = dict()
        count = 0
        for n in nums:
            if k - n in visited:
                count += 1
                visited[k-n] -= 1
                if visited[k-n] == 0:
                    del visited[k-n]
                continue

            visited[n] = visited.get(n, 0) + 1
        return count
