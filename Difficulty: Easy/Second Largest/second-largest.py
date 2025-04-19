class Solution:
    def getSecondLargest(self, arr):
        largest = -1
        secondlargest = -1
        n = len(arr)
        for i in range(n):
            if arr[i] > largest:
                largest = arr[i]
        for i in range(n):
            if largest != arr[i] and arr[i]>secondlargest:
                secondlargest = arr[i]
        return secondlargest
            
            


    


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends