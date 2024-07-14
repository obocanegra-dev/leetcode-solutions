class Solution(object):
    def searchRange(self, nums, target):
        def find_first_position(nums, target):
            left, right = 0, len(nums) - 1
            first_position = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first_position = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first_position

        def find_last_position(nums, target):
            left, right = 0, len(nums) - 1
            last_position = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    last_position = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last_position

        first = find_first_position(nums, target)
        last = find_last_position(nums, target)

        if first == -1:
            return [-1, -1]

        return [first, last]
