# 198. House Robber

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

         # even = 0
        # odd = 0
        #
        # for i, num in enumerate(nums):
        #     if i % 2:
        #         odd += num
        #     else:
        #         even += num
        #
        # return max(even,odd)

        
        prev = 0
        prevnot = 0

        for num in nums:
            temp = max(prev, num + prevnot)
            prevnot = prev
            prev = temp
            
       
        return prev
