def eval(x):
    s = []
    for c in x:
        if s and ((c.isupper() and c.lower() == s[-1]) or (c.islower() and c.upper() == s[-1])):
            s.pop()
        else:
            s.append(c)
    return ''.join(s)

x = raw_input()
print len(eval(x))
print min(len(eval(x.replace(c,'').replace(c.upper(),''))) for c in set(x.lower()))
