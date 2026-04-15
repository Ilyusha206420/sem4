import math

with open("../inputText", "r", encoding="utf-8") as f:
  inpStr = f.readline()
  f.close()

msgBlocks = []
for i in range(0, len(inpStr) - len(inpStr)%6, 6):
  msgBlocks.append(inpStr[i:i+6])

dArrs = []

for l in range(0, 3):
  d = {}
  N = 0
  for i in range(0, len(inpStr) - l, l+1):
    comb = inpStr[i:i+l+1]
    if comb in d:
      d[comb][0] += 1
    else:
      d[comb] = [1, 0, 0, 0] # ** N, p, I, q
    N += 1
    
  dArrs.append([d, N, l, 0])

for d, l, it, _ in dArrs:
  q = 0
  for key in d:
    p = d[key][0] / l
    I = -math.log2(p)
    d[key][1] = p
    d[key][2] = I
    d[key][3] = q
    q += p

for i in range(0, 3):
  for msg in msgBlocks:
    F = 0
    G = 1
    Fd = {}
    Gd = {}
    codyngSymbols = []
    for s in range(0, 6, i+1):
      sym = msg[s:s+i+1]
      codyngSymbols.append(sym)
      F += dArrs[i][0][sym][3] * G
      G *= dArrs[i][0][sym][1]
      Fd[sym] = F
      Gd[sym] = G
    for sym in codyngSymbols:
      print(f'|{sym:^5}| {dArrs[i][0][sym][1]:.5f} | {dArrs[i][0][sym][3]:.5f} | {Fd[sym]:.10f} | {Gd[sym]:.10f} |')
    l = -math.ceil(math.log2(G)) + 1
    cv = F + (G/2)
    code = ""
    for n in range(0, l):
      p2 = math.pow(2, -n)
      if p2 <= cv:
        cv -= p2
        code += '1'
      else:
        code += '0'
    print(f'\n{msg} : {code}\n\n')
