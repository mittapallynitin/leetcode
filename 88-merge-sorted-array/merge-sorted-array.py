class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n - 1
        p = m + n - 1

        while i > - 1 and j > -1:
            if nums1[i] >= nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1
        while i > -1:
            nums1[p] = nums1[i]
            p -= 1
            i -= 1
        while j >-1:
            nums1[p] = nums2[j]
            p -= 1
            j -= 1
