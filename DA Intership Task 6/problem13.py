#hackerrank:-https://www.hackerrank.com/challenges/py-set-union/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
english_count = input()
english_set = set(map(int, input().split()))
french_count = input()
french_set = set(map(int, input().split()))
at_least_one_subscription = english_set.union(french_set)
print(len(at_least_one_subscription))
