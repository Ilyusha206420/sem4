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
      dArr[l][comb] += 1
    else:
      dArr[l][comb] = 1
    N += 1
  lens.append(N)

H = []

for i in range(len(dArr)):
  print(f"Комбинация из {i+1} элементов:\n| {f"xi":^3} | {f"Ni":^2} | {f"Ni/n":^7} | {f"p(x)":^22} | {f"I(x)":^22} | {f"p(x) * I(x)":^22} |")
  summ = 0
  for elem in dArr[i]:
    p = dArr[i][elem]/lens[i]
    I = -math.log2(p)
    pI = p * I
    print(f"| {elem:^3} | {dArr[i][elem]:^2} | {f"{dArr[i][elem]}/{lens[i]}":^7} | {p:.20f} | {I:.20f} | {pI:.20f} |")
    summ += pI
  print(f"\nN = {lens[i]}\n")
  H.append(summ)

hxx1 = H[1] - H[0]

print(f"\
H(X1)   = {H[0]}\n\
H1(X)   = {H[0]}\n\
H(X|X0) = {H[0]}\n\
\n\
H(X2)   = {H[1]}\n\
H2(X)   = {H[1]/2}\n\
H(X|X1) = {hxx1}\n\
\n\
H(X3)   = {H[2]}\n\
H3(X)   = {H[2]/3}\n\
H(X|X2) = {H[2] - hxx1 - H[0]}")