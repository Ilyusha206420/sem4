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
      d[comb] = [1, 0, 0, 0, 0, ""] # ** N, p, I, q, l, c
    N += 1
    
  dArrs.append([d, N, l, 0])

for d, l, it, _ in dArrs:
  sortedDict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
  q = 0
  midLen = 0
  for key in sortedDict:
    p = sortedDict[key][0] / l
    I = -math.log2(p)
    lenght = math.ceil(I)
    sortedDict[key][1] = p
    sortedDict[key][2] = I
    sortedDict[key][3] = q
    sortedDict[key][4] = lenght
    qc = q
    s = ""
    for i in range(lenght):
      p2 = math.pow(2, -1 * (i + 1))
      if(qc >= p2):
        s += '1'
        qc -= p2
      else:
        s += '0'
    sortedDict[key][5] = s
    midLen += p * lenght
  dArrs[it][3] = midLen
  dArrs[it][0] = sortedDict
    
for d, _, it, l in dArrs:
  for key in d:
    print(f'|{key:^5}|{d[key][0]:^4}| {d[key][1]:.10f} | {d[key][2]:.5f} | {d[key][3]:.5f} |{d[key][4]:^3}|{d[key][5]:^10}|')
  print(f'\nl = {l:.5f}\nR = {l/(it + 1):.5f}\n\n')
