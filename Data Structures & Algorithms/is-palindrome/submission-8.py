class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [caracter.lower() for caracter in s if caracter.isalnum()]
        j = -1
        for i in range(len(s)) :
            if s[i] != s[j]:
                return False
            j -= 1
        return True
                