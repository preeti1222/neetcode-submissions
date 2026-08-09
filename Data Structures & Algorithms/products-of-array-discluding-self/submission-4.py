class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n =  len(nums)
        res = [0] * n 

        for i in range(n):
            prod = 1 
            for j in  range(n):
                if i == j:
                    continue 
                prod *= nums[j]

            res[i] = prod
        return res            
        

        