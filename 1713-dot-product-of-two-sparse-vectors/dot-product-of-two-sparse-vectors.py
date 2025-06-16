class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = {i:v for i, v in enumerate(nums) if v != 0}
       

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for idx in self.vector.keys():
            if idx in vec.vector.keys():
                total += self.vector[idx] * vec.vector[idx]
        return total
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)