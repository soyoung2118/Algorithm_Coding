import sys
input = sys.stdin.readline

R,C = map(int, input().split())
crossword = []

for _ in range(R):
  crossword.append(list(input()))

words = []

for i in range(R):
  word=[]
  for j in range(C):
    if crossword[i][j] != "#":
      word.append(crossword[i][j])
      if len(word) == R:
        words.append(word)
        word=[]
      if (j==C-1) and (len(word)>1):
        words.append(word)
    else:
      if len(word) > 1:
        words.append(word)
      word=[]

for l in range(C):
  word=[]
  for k in range(R):
    if crossword[k][l] != "#":
      word.append(crossword[k][l])
      if len(word) == C:
        words.append(word)
        word=[]
      if (k==R-1) and (len(word)>1):
        words.append(word)
    else:
      if len(word) > 1:
        words.append(word)
      word=[]
    
words.sort()
print("".join(words[0]))