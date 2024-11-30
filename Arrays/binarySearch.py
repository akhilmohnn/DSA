#User function template for Python

class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        n=len(arr)
        low=0
        high=n-1
        result=-1
        
        while low<=high:
            mid=(low+high)//2
            
            if arr[mid]==k:
                result=mid
                
            if arr[mid]<k:
                low=mid+1
                
            else:
                high=mid-1
                
        return result
