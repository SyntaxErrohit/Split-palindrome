def splitp(s, memo = {}):
    if s in memo: return memo[s]
    if s == "": return []

    maxl, maxr = 0, 0
    for i in range(len(s)):
        l, r = i, i
        while l >=0 and r < len(s) and s[l] == s[r]:
            if r-l > maxr-maxl:
                maxl, maxr = l, r
            l -= 1
            r += 1

        l, r = i, i+1
        while l >=0 and r < len(s) and s[l] == s[r]:
            if r-l > maxr-maxl:
                maxl, maxr = l, r
            l -= 1
            r += 1

    memo[s] = splitp(s[:maxl]) + [s[maxl:maxr+1]] + splitp(s[maxr+1:])
    return memo[s]
        

print(splitp("2121212442142453664124421"))