class Solution:
    
    # def printNumbers(self, start, end):
    #     if start > end:
    #         return
        
    #     print(start, end = " ")
    #     self.printNumbers(start + 1, end)
    
    def printTillN(self, n):
    # 	self.printNumbers(1, n)
        if n == 0:
            return
        
        self.printTillN(n - 1)
        print(n, end = " ")
        
    	