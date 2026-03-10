import math

with open("./inputText", "r", encoding="utf-8") as f:
  inpStr = f.readline()
  f.close()

dArr = []
lens = []

for l in range(0, 3):
  dArr.append({})
  N = 0
  for i in range(len(inpStr) - l):
    comb = inpStr[i:i+l+1]
    if comb in dArr[l]:
      dArr[l][comb][0] += 1
    else:
      dArr[l][comb] = [1, 0]
    N += 1

  for elem in dArr[l]:
    dArr[l][elem][1] = dArr[l][elem][0] / N
  
  lens.append(N)

sortedDict = dict(sorted(dArr[0].items(), key= lambda item: item[1][1], reverse=True))

for elem in sortedDict:
  print(f'{elem} | {sortedDict[elem][1]:.5f}')