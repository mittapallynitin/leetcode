class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        result = [0]*(len(digits)+1)
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            s = carry + digits[i]
            result[i+1] = s % 10
            carry = s // 10
        if carry > 0: 
            result[0] = carry
            return result
        else:
            return result[1:]
        