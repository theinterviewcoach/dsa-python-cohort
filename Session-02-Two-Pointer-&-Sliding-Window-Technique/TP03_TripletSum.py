# Problem Statement: 
# Find if there exists a triplet whose sum is equal to the given target.

# For example:

# Input:
# nums = [5,2,7,9,10,12,25,11,19], target = 27

# Output:
# True

class Solution:

    # this is the exact same method as Two Sum problem
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

    def findIfTripletExists(self, nums, target):
        sorted(nums) # sort the array so that we can apply 2 sum technique on this array
        N = len(nums)
        for i in range(N - 2):
            pairTarget = target - nums[i]
            ans = self.findPair(nums[i + 1:], pairTarget) # find pairTarget in the remaining array using 2 sum technique
            if ans[0] != -1:
                return True # or return [i, ans[0], ans[1]] 

        return False # or return [-1, -1, -1]

if __name__ == '__main__':
    solution = Solution()
    
    nums = [5, 2, 7, 9, 10, 12, 25, 11, 19]
    target = 10
    print(solution.findIfTripletExists(nums, target))