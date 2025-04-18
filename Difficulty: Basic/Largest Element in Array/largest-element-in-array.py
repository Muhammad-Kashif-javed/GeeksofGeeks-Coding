
from typing import List

class Solution:
    def largest(self, arr: List[int]) -> int:
        max = arr[0]
        for i in range(1 , len(arr)):
            if arr[i]>max:
                max = arr[i]
        return max
        

      '''Time Complexiety is O(n) because it iterates through the list once,
      performing a constant-time comparison at each step to find the maximum
      value. The space complexity is O(1) since it uses only a single variable 
      to store the maximum value and does not allocate any additional 
      data structures regardless of the input size'''
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().split()))

        obj = Solution()
        res = obj.largest(arr)

        print(res)
        print("~")

# } Driver Code Ends
