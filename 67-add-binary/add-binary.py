class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1

        carry = 0 
        ans = ""

        while i >= 0 or j >= 0 or carry:
            if i >=0:
                carry += int(a[i])
                i -= 1
            if  j >= 0:
                carry += int(b[j])
                j -= 1
            
            ans += str(carry % 2)
            carry = carry // 2
        
        return ans[::-1]

        