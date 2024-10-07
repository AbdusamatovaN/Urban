def all_variants(text):
    i = 1
    while i <= len(text):
        l = 0
        r = i
        while r <= len(text):
            yield text[l:r]
            l += 1
            r += 1
        i += 1



a = all_variants("abc")
for i in a:
    print(i)