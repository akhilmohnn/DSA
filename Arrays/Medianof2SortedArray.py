class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combine=sorted(nums1+nums2)
        
        n=len(combine)

        if n%2==1:
            return float(combine[n//2])
        else:
            mid1=combine[n//2-1]
            mid2=combine[n//2]
            return (mid1+mid2)/2   
        
