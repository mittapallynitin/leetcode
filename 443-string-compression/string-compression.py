class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = None
        count = 0
        l = 0
        for r in range(len(chars)):
            ch = chars[r]
            if ch == prev:
                count += 1
            else:
                if prev:
                    x = prev + ("" if count == 1 else str(count))
                    chars[l: l + len(x)] = x
                    l += len(x)
                   
                prev = ch
                count = 1
        x = prev + ("" if count == 1 else str(count))
        chars[l:l + len(x)] = x
        l += len(x)
        return l

        