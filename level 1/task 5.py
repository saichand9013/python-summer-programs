#level1-T5
#Task: Palindrome Checker
#Write a Python function that checks whether a given string is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backward as forward (e.g.,"madam" or "racecar").
def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = "123"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
