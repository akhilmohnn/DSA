class Solution:
	def addBinary(self, s1, s2):
		# code here
		return bin(int(s1, 2) + int(s2, 2))[2:]
        #both string inputs are converted to integers of base 2
        #added both of these
        #now the result is changed back to string using bin
        #bin() add 'ob' infront of return so removing it using[2:]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends