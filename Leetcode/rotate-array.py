'''
Link: https://leetcode.com/problems/rotate-array/
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %=  len(nums) 
        if k == 0:
            return
        nums[:-k:], nums[-k::] = nums[-k::], nums[:-k:]
        
