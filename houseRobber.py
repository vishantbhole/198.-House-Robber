class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = 0
        prevnot = 0

        for num in nums:
            temp = max(prev, num + prevnot)
            prevnot = prev
            prev = temp
            
       
        return prev
