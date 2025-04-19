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
            
Two separate loops over the array of size n, Each loop runs O(n) times, Total time = O(n + n) = O(n)
Time Complexity = O(n)

Space Complexity:
we use only a constant number of variables (largest, secondlargest, n), No additional data structures are used
Space Complexity = O(1) (constant space)

            


    

