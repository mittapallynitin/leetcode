class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = 'aeiou'
        vowels = vowels + vowels.upper()
        res = []
        for idx, word in enumerate(sentence.split()):
            idx += 1
            if word[0] not in vowels:
                word = word[1:] + word[0]
            
            word += "ma" + "a"*idx
            res.append(word)
        
        return " ".join(res)

        