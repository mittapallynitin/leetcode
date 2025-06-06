class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(1, numRows):
            previous = result[i-1]
            level = [1] + [previous[j-1] + previous[j] for j in range(1, i)] + [1]
            result.append(level)
        return result