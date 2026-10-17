#hackerrank:-https://www.hackerrank.com/challenges/py-set-difference-operation/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
english_count = input()
english_set = set(map(int, input().split()))
french_count = input()
french_set = set(map(int, input().split()))
only_english = english_set.difference(french_set)
print(len(only_english))
