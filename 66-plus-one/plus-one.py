class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = 1
        digits.reverse()
        for i in digits:
            res = i + carry
            carry = res // 10
            result.append(
                res % 10 
            )
        if carry:
            result.append(carry)
        return result[::-1]
        