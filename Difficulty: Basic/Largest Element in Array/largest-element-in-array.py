
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
        



