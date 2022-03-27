"""
단어정렬 
  - key, lambda를 이용해 단어 정렬하기 
"""
import sys
n = int(input())
words = []

for _ in range(n):
  words.append(input())

words = list(set(words))     # 같은 단어 여러개 입력된 경우 하나만 출력 
new = sorted(words, key=lambda x : (len(x), x))   # 길이가 짧은 것부터 > 같으면 사전순으로 정렬
for i in new:
  print(i)
