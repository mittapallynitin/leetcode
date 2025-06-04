class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Way 1 : Uses O(N) memory for O(N) time complexity
        # k = k % len(nums)
        # first = nums[:-k]
        # second = nums[-k:]
        # nums[::] = second + first

        # Way 2: Reverse the complete list, revese the first k and rest of elements. 
        def reverse_inplace(nums, start, stop):
            n_elemts = (stop - start)
            n = n_elemts // 2 + n_elemts % 2

            for i in range(n):
                nums[start + i], nums[stop-i-1] = nums[stop-i-1], nums[start + i]
        
        if len(nums) == 1:
            return
        k = k % len(nums)
        reverse_inplace(nums, 0, len(nums))
        reverse_inplace(nums, 0, k)
        reverse_inplace(nums, k, len(nums))
        print(nums)
            





        