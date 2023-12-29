def isPalindrome(string):
    try:
        if (string[0] == string[len(string)-1]): return isPalindrome(string[1:len(string)-1])
        else: return False
    except: return True
    
print(isPalindrome("xyxyx"))