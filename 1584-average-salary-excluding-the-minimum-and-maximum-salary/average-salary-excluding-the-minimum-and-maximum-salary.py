class Solution:
    def average(self, salary: List[int]) -> float:
        min_sal, max_sal = float("inf"), float("-inf")
        total_sal = 0

        for sal in salary:
            total_sal += sal 

            if sal < min_sal:
                min_sal = sal
            
            if sal > max_sal:
                max_sal = sal
        
        return (total_sal - min_sal - max_sal) / (len(salary) - 2)
        