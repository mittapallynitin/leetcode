class Solution:
    def romanToInt(self, s: str) -> int:
        r_to_i = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50, 
            "XC": 90,
            "C": 100, 
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        i = 0 
        result = 0
        while i < len(s):
            if s[i: i+2] in r_to_i:
                result += r_to_i[s[i:i+2]]
                i += 2
            else:
                result += r_to_i[s[i:i+1]]
                i += 1
        
        return result 