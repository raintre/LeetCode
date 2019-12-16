class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            subsets += [s + [num] for s in subsets]
        return subsets