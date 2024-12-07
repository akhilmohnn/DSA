class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	nonZero=0
    	
    	for i in range(len(arr)):
    	    if arr[i]!=0:
    	        
    	        arr[nonZero],arr[i]=arr[i],arr[nonZero]
    	        nonZero+=1
        return arr	        
