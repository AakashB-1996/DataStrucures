def anagram(s1,s2):
    s1 = ''.join(s1.lower().split())
    s2 = ''.join(s2.lower().split())
    counts = {}
    if len(s1) != len(s2):
        return False
    for i in s1:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    for i in s2:
        if i in counts:
            counts[i] -= 1
        else:
            counts[i] = 1
    for key in counts:
        if counts[key] != 0:
            return False  
    
    return True
