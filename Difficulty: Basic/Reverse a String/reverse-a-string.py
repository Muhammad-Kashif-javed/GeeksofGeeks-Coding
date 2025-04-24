#User function Template for python3

class Solution:
    def reverseString(self, s: str) -> str:
        l = list(s)
        l.reverse()  # reverse function
        return "".join(l)  # joins the list into a string without spaces

         
       # k = s[ : :-1]   #slicing
        #return k
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        s = input()
        ob = Solution()
        print(ob.reverseString(s))
        t = t - 1

        print("~")

# } Driver Code Ends