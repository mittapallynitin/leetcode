class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for op in operations:
            if op == "C" and score:
                score.pop()
            elif op == "+" and score:
                score.append(
                    score[-2] + score[-1]
                )
            elif op == "D" and score:
                score.append(
                    score[-1]*2
                )
            else:
                score.append(int(op))
        return sum(score)