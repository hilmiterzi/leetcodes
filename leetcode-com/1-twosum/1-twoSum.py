class Solution:

    def twoSum(self, nums, target):

        num_at_index = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_at_index:
                return [num_at_index[complement], index]

            num_at_index[num] = index

        return []