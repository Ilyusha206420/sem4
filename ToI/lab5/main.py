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

entrops = [0, 0, 0]

for d, l, it, _ in dArrs:
  q = 0
  midLen = 0
  entropy = 0
  for key in d:
    p = d[key][0] / l
    I = -math.log2(p)
    lenght = math.ceil(I) + 1
    d[key][1] = p
    d[key][2] = I
    d[key][3] = q
    d[key][4] = lenght
    qc = q + p/2 
    s = ''
    for i in range(lenght):
      p2 = math.pow(2, -1 * (i + 1))
      if(qc >= p2):
        s += '1'
        qc -= p2
      else:
        s += '0'
    d[key][5] = s
    midLen += p * lenght
    q += p
    entropy += p * I
  dArrs[it][3] = midLen
  entrops[it] = entropy
    
for d, _, it, l in dArrs:
  for key in d:
    print(f'|{key:^5}|{d[key][0]:^4}| {d[key][1]:.10f} | {d[key][2]:.5f} | {d[key][3]:.5f} |{d[key][4]:^3}|{d[key][5]:^11}|')
  print(f'\nl = {l:.5f}\nR = {l/(it + 1):.5f}\nr = {(l - entrops[it])/(it + 1):.5f}\n')
