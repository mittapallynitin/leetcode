class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        total = len(s)
        chrs = sorted([(ch, cnt) for ch, cnt in Counter(s).items()], key=lambda x: x[1])
        deletions = 0
        index = 0
        uniq = len(chrs)
        while uniq > k and index < len(chrs):
            ch, cnt = chrs[index]
            deletions += cnt
            index += 1
            uniq -= 1
        return deletions
