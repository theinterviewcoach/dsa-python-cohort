class BubbleSortOptimised:
    def sort(self, nums):
        n = len(nums)

        
        for i in range(n - 1):
            swapped = False
            for j in range(n - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                break
                    
        return nums


if __name__ == '__main__':
    nums = [3, 2, 9, 1, 4, 5]
 
    bubble_sort = BubbleSortOptimised()
    print(bubble_sort.sort(nums))