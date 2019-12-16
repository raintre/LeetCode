class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            days = 1
            weight_pivot = 0
            for weight in weights:
                if weight_pivot + weight > mid:
                    days += 1
                    weight_pivot = 0
                weight_pivot += weight
            if days <= D:
                right = mid
            else:
                left = mid + 1
        return left