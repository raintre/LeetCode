#brute force
class Solution:
	def rotate(self, nums: List[int], k: int) -> None:
		size = len(nums)
		for i in range(k):
			previous = nums[size - 1]
			for j in range(size):
				temp = nums[j]
				nums[j] = previous
				previous = temp	
# -> TLE

class Solution:
	def rotate(self, nums: List[int], k: int) -> None:
		size, rotated = len(nums), []
		for i in range(size):
			rotated[(i + k) % size].append(nums[i])
		for j in range(size):
			nums[j].append(rotated[j])

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        rotated = [0] * len(nums)
        for i in range(len(nums)):
            rotated[(i + k) % len(nums)] = nums[i] #recycle

        for i in range(len(nums)):
            nums[i] = a[i]

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        count = 0
        start = 0
        while count < len(nums):
            current = start 
            prev = nums[start] #store the value in the position
            
            while True:
                next = (current + k) % len(nums) #
                temp = nums[next] #store it temporaly 
                nums[next] = prev #overide the next 
                prev = temp #reset prev
                current = next #reset current
                count += 1

                if start == current:
                    break 
            
            start += 1

class Solution:
    def rotate(self, nums, k) -> None:
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0, k-1)
        self.reverse(nums,k, len(nums)-1)

    def reverse(self, nums, start, end) -> None:
        """
        :type nums: List[int]
        :type start: int
        :type end: int
        :rtype: None
        """
        while start < end: #
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp 
            start += 1
            end -= 1