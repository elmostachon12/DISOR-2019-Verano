ulam_i = [1,2,3]
ulam_j = [1,2,3]
for cand in range(4,1000):
    res = []
    for i in ulam_i:
        for j in ulam_j:
            if i == j or j > i: pass
            else:
                res.append(i+j)
    if res.count(cand) == 1:
        ulam_i.append(cand)
        ulam_j.append(cand)
print (ulam_i)