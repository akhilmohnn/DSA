class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        n=len(arr)
        result=False

        for i in range(n):
            for j in range(n):
                if i!=j and arr[i]==2*arr[j]:
                    result=True 

        if result:
            return True
        else:
            return False  
