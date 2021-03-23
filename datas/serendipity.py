
# https://blog.cloudflare.com/creating-serendipity-with-python/
# n//g (// is integer division), e.g.  if g == 4 and n == 17 then groups == [4, 4, 4, 4]
g = 5
n = 23

groups = [g] * (n//g)
print(groups)
r = n % g
print(r)
for e in range(0, r):
    groups[e % len(groups)] += 1
    
print(groups)