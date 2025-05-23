class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = 1

        for i in digits[::-1]:
            res = i + carry
            carry = res // 10
            res = res % 10 
            
            result.append(
                res
            )
        if carry:
            result.append(carry)
        return result[::-1]
        