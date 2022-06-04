def find_short(s):
    shortest = min(s.split(), key=len)
    return len(shortest)