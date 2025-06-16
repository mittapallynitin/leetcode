class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        total = len(s)
        chrs = sorted([(ch, cnt) for ch, cnt in Counter(s).items()], key=lambda x: x[1])
        deletions = 0
        while len(chrs) > k:
            ch, cnt = chrs.pop(0)
            deletions += cnt
        return deletions
