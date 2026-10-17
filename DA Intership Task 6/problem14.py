#hackerrank:-https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
english_count = input()
english_set = set(map(int, input().split()))
french_count = input()
french_set = set(map(int, input().split()))
both_subscriptions = english_set.intersection(french_set)
print(len(both_subscriptions))
