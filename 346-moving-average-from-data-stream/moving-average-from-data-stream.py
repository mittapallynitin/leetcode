class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.arr = [0]*size
        self.pos = 0
        self.curr_sum = 0
        self.ith_ele = 0
        

    def next(self, val: int) -> float:
        self.arr[self.pos] = val 
        self.pos = (self.pos + 1) % self.size
        self.ith_ele += 1
        return float(sum(self.arr)) / min(self.ith_ele, self.size)
        


        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)