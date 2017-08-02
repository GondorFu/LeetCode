class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        hints: use hash map to store unique numbers' index
        """
        d = {}
        rlt = []
        for i, val in enumerate(nums):
            if target-val in d:
                return [d[target-val], i]
            if val not in d:
                d[val] = i
            
                
        