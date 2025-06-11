class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ch_order = {}
        for idx, ch in enumerate(order):
            ch_order[ch] = idx
        idx += 1
        for ch in s:
            if ch not in ch_order:
                ch_order[ch] = idx
                idx += 1
        reverse_order = {i: ch for ch, i in ch_order.items()}
        s = sorted([ch_order[ch] for ch in s])
        s = [reverse_order[i] for i in s]
        return "".join(s)
