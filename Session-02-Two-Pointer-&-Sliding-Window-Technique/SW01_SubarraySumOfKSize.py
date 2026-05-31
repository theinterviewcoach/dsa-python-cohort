class Solution:

    def findSubarraySumOfSizeK(self, nums, k):
        windowStart = 0
        windowSum = 0
        result = []

        for windowEnd in range(len(nums)):
            windowSum = windowSum + nums[windowEnd]

            if windowEnd >= (k - 1):
                result.append(windowSum)

                windowSum = windowSum - nums[windowStart]
                windowStart += 1
        
        return result


if __name__ == '__main__':
    solution = Solution()
    
    nums = [4, 6, 2, 8, 1 ,9, 7, 3]
    k = 4
    print(solution.findSubarraySumOfSizeK(nums, k))