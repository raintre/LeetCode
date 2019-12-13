class Solution:
	def rotate(self, nums: List[int], k: int) -> None:
		length = len(nums)
		rotated = [0] * length
		for index in range(length):
			rotated[(index + k) % length] = nums[index]
		for index in range(length):
			nums[index] = rotated[index]