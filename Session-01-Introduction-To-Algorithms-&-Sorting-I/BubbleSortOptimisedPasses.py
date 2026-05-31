class BubbleSortOptimisedPasses:
    def sort(self, nums):
        n = len(nums)
        passes = 0
        
        for i in range(n - 1):
            passes += 1
            swapped = False
            for j in range(n - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                break
                    
        return nums, passes


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
 
    bubble_sort = BubbleSortOptimisedPasses()
    print(bubble_sort.sort(nums))