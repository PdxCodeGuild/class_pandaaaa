class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = dict()
        for i in range(len(nums)):
            temp2 = target - nums[i]
            if(temp2 not in temp):
                temp.append(i)
            
        
        




mySolution = Solution()
print(mySolution.twoSum([5,2,11,4,3],5))
