#hackerrank:-https://www.hackerrank.com/challenges/word-order/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
word_counts = {}

for _ in range(n):
    word = input().strip()
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(len(word_counts))
counts = [str(count) for count in word_counts.values()]
print(" ".join(counts))
