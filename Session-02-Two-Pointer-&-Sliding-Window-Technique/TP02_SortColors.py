class Solution:
    def sort(self, nums):
        left = 0
        right = len(nums) - 1
        i = 0

        while i <= right:

            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                i += 1
                left += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1

        return nums


if __name__ == '__main__':
    solution = Solution()
    
    nums = [1, 1, 0, 2, 0, 1, 2, 0, 2, 0]
    print(solution.sort(nums))