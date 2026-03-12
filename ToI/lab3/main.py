import math
import heapq
from collections import namedtuple

class Node(namedtuple('Node', ['Freq', 'char', 'left', 'right'])):
  def __lt__(self, other):
    return self.Freq < other.Freq

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
      dArr[l][comb] = [1, "", 0]
    N += 1
  lens.append(N)

trees = []

for curDict in dArr:
  heap = [Node(val[0], char, None, None) for char, val in curDict.items()]
  heapq.heapify(heap)

  while len(heap) > 1:
    node1 = heapq.heappop(heap)
    node2 = heapq.heappop(heap)
    merg = Node(node1.Freq + node2.Freq, None, node1, node2)
    heapq.heappush(heap, merg)
  trees.append(heap[0])

def makeCodes(node, n, curCode = ""):
  if node is None: return

  if node.char is not None: 
    dArr[n][node.char][1] = curCode
    dArr[n][node.char][2] = len(curCode) * node.Freq / lens[n]
    return

  makeCodes(node.right, n, curCode + '1')
  makeCodes(node.left, n, curCode + '0')
  return

for i in range(len(trees)):
  makeCodes(trees[i], i)

H = (4.489072240657972, 3.3257138304664493, 2.392326831645251)

for n in range(len(dArr)):
  l = 0
  for elem in dArr[n]:
    print(f'|{elem:^5}|{dArr[n][elem][0]:^5}|{dArr[n][elem][1]:^11}| {dArr[n][elem][2]:.5f} |')
    l += dArr[n][elem][2]
  R = l / (n + 1)
  print(f'\nl = {l}\nR = {R}\n{R - H[n]}\n')