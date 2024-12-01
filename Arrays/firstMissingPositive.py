class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        maxNum=max(nums)
        minNum=min(nums)

        if minNum<1:
            minNum=1

        for i in range(1,maxNum+1):
            if i not in nums:
                return i
        return maxNum+1 
