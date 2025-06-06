class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0 
        n = len(abbr)
        sub = []
        while i < n:
            if abbr[i].isdigit():
                if abbr[i] == "0":
                    return False
                num = ""
                while i < n and abbr[i].isdigit():
                    num += abbr[i]
                    i += 1
                if int(num) > len(word):
                    return False
                sub.append("-"*int(num))
            else:
                sub.append(abbr[i])
                i += 1
        sub = "".join(sub)
        print(sub)
        print(word)
        if len(sub) == len(word):
            for c1, c2 in zip(sub, word):
                if c1 != "-" and c1 != c2:
                    return False
        else:
            return False
        return True
        