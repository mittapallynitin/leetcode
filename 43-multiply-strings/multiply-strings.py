class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def sub_product(idx):
            num = int(num2[idx])
            carry = 0
            res = ""
            for i in num1[::-1]:
                i = int(i)
                p = num * i + carry
                res += str(p % 10)
                carry = p // 10
            if carry:
                res += str(carry)
            return res[::-1]

        product = []
        for i in range(len(num2)-1, -1, -1):
            res = sub_product(i)
            print(res)
            product.append(res)
        
        total = 0 
        for i, n in enumerate(product):
            total += (10**i * int(n))
        return str(total)

    
    

