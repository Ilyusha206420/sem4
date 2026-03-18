import math

with open("../inputText", "r", encoding="utf-8") as f:
  inpStr = f.readline()
  f.close()

dArrs = []

for l in range(0, 3):
  d = {}
  N = 0
  for i in range(len(inpStr) - l):
    comb = inpStr[i:i+l+1]
    if comb in d:
      d[comb][0] += 1
    else:
      d[comb] = [1, "", 0, 0, 0] # ** N, code, p, q, len 
    N += 1
  dArrs.append([d, N])

for d, l in dArrs:
  sortedDict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
  q = 0
  for elem in sortedDict:
    p = sortedDict[elem][0] / l
    sortedDict[elem][2] = p
    sortedDict[elem][3] = q
    sortedDict[elem][4] = math.ceil(-math.log2(p))
    q += p



for d, _ in dArrs:
  for key in d:
    print(key, d[key])