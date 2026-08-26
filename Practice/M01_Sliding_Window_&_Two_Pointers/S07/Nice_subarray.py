'''leetcode 1763'''
from typing import List 
def longestNiceSubstring(s: str) -> str:
        if len(s)<2:
            return ""
        uniq=set(s)
        for i,ch in enumerate(s):
            if ch.lower() in uniq and ch.upper() in uniq:
                continue
            left_str = longestNiceSubstring(s[0:i])        
            right_str = longestNiceSubstring(s[i+1:])

            if len(left_str) >= len(right_str):
                return left_str
            else:
                return right_str
        return s    

s1 = "YazaAay"   
s2 = "Bb"            
s3 = "c"
print(longestNiceSubstring(s1))
print(longestNiceSubstring(s2))
print(longestNiceSubstring(s3))
