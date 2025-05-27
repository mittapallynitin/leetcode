class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        FIVEs = 0 
        TENs = 0 
        TWETs = 0 

        for bill in bills:
            
            if bill == 5:
                FIVEs += 1
            
            elif bill == 10:
                TENs += 1
                if FIVEs:
                    FIVEs -= 1
                else:
                    return False
            
            elif bill == 20:
                TWETs += 1
                if TENs and FIVEs:
                    TENs -= 1
                    FIVEs -= 1
                elif FIVEs >= 3:
                    FIVEs -= 3
                else: 
                    return False
        return True

