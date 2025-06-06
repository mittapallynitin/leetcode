class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(1, numRows):
            previous = result[i-1]
            level = []
            for j in range(i+1):
                if j == 0 or j == i:
                    level.append(1)
                else:
                    level.append(previous[j-1] + previous[j])
            result.append(level)
        return result