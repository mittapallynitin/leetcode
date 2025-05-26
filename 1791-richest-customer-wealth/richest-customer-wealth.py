class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        i, j = len(accounts), len(accounts[0])
        amount = [0]*i
        for customer in range(i):
            for bank in range(j):
                amount[customer] += accounts[customer][bank]
        
        rich = float("-inf")
        for i, a in enumerate(amount):
            if a > rich:
                rich = a
        
        return rich
