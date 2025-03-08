from collections import deque

N = int(input())

cards = deque(range(N ,0,-1))

while len(cards) != 1:
  cards.pop()
  cards.rotate()

print(*cards)