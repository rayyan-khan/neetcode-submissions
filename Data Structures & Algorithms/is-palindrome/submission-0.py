class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_chars = "".join([ch for ch in s if ch.isalnum()]).lower()
        return valid_chars == valid_chars[::-1]
        