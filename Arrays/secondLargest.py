"""arr = [12, 35, 1, 10, 34, 1] o/p:34 , if same as largest not considered"""


def print2largest(self,arr):
    n=len(arr)

    if(n<2):
        return -1
    
    first=second=float('-inf')

    for num in arr:
        if num>first:
            second=first
            first=num
        elif num>second and num!=first:
            second=num

    if second==float('-inf'):
        return -1
    else:
        return second
