class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1 = 0
        rob2 = 0

        for num in nums:
            temp = max( num + rob1,rob2)
            rob1 = rob2
            rob2 = temp
            
       
        return rob2


if __name__ == "__main__":
    sol = Solution()
    nums = [2,1,1,2]
    print("rob is:", sol.rob(nums))
