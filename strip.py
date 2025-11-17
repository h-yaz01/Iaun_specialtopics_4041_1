def strp(text):
    start = 0
    end = len(text) - 1
    
    while start < len(text) and text[start] == " ":
        start += 1
    
    while end >= 0 and text[end] == " ":
        end -= 1
    
    if start > end:
        return ""  
    
    return text[start:end+1]

s = "   hello   "
print("[" + strp(s) + "]")