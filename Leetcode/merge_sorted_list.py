'''
Link: https://leetcode.com/problems/merge-sorted-array/
'''

class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m]
        nums1.extend(nums2)
        nums1.sort()
    def merge_O(nums1, m, nums2, n):
      '''
      for O(m+n)
      '''
      # Start merging from the end of both arrays
      index1, index2, merge_index = m - 1, n - 1, m + n - 1

      while index1 >= 0 and index2 >= 0:
        # Compare and merge elements
        if nums1[index1] > nums2[index2]:
            nums1[merge_index] = nums1[index1]
            index1 -= 1
        else:
            nums1[merge_index] = nums2[index2]
            index2 -= 1
        merge_index -= 1
