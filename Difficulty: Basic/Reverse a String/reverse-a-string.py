#User function Template for python3

class Solution:
    def reverseString(self, s: str) -> str:
        l = list(s)
        l.reverse()  # reverse function
        return "".join(l)  # joins the list into a string without spaces

 # Time complexiety O(n) 
 # Space Complexiety O(n) two extra copies: the list and the final reversed string
_________________________________________________________________________________________
# if we want Space Complexiety O(1). no extra space used except a few pointers
class Solution:
    def reverseString(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
_________________________________________________________________________________
  #slicing
class Solution:
    def reverseString(self, s: list[str]) -> None:
        k = s[ : :-1] 
        return k


Time Complexity: O(n)
s[::-1] traverses the entire list once to construct the reversed version.
 Space Complexity: O(n)
s[::-1] creates a new reversed list, so it needs extra space proportional to the input size.



