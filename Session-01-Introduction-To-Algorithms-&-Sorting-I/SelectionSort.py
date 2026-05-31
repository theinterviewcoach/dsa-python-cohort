class SelectionSort:
    def sort(self, nums):
        n = len(nums)
        
        for i in range(n - 1):
            minimum_index = i
            for j in range(i, n):
                if nums[j] < nums[minimum_index]:
                    minimum_index = j
            nums[i], nums[minimum_index] = nums[minimum_index], nums[i]

        return nums

if __name__ == '__main__':
    nums = [3, 2, 9, 1, 4, 5]
 
    selection_sort = SelectionSort()
    print(selection_sort.sort(nums))