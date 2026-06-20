# Check if string is palindrome or not 
def rec1(s, start=0, end=None) -> bool:
    if end is None:
        end = len(s) - 1
    
    if start >= end:
        return True
    
    if s[start] != s[end]:
        return False
    
    return rec1(s, start + 1, end - 1)

s: str = input()
print(rec1(s))