class Solution:
    def findPair(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left != right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == target:
                return [left, right]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
        
        return [-1, -1]


if __name__ == '__main__':
    solution = Solution()
    
    nums = [2, 3, 8, 10, 12, 14, 15]
    target = 26
    print(solution.findPair(nums, target))

    nums = [2, 3, 8, 10, 12, 13, 15]
    target = 26
    print(solution.findPair(nums, target))

