class Solution:

    def findSubsets(self, subsets, subset, i, nums):
        # base case
        if i == len(nums):
            subsets.append(subset[:])
            return

        # recursive case

        # option 1 - left side
        subset.append(nums[i])
        self.findSubsets(subsets, subset, i + 1, nums)
        subset.pop() # backtracking step

        # option 2 - right side
        self.findSubsets(subsets, subset, i + 1, nums)

    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets = []
        subset = []
        self.findSubsets(subsets, subset, 0, nums)
        return subsets