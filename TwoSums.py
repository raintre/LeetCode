#Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first in range(0, len(nums) - 1):
            for second in range(first + 1, len(nums)):
                if nums[first] + nums[second] == target:
                    return [first, second]

#O(n) time solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index in range(len(nums)):
            if (target - nums[index]) not in dic:
                dic[nums[index]] = index
            else:
                return [dic[target - nums[index]], index]
