#hackerrank:-https://www.hackerrank.com/challenges/py-set-add/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
country_set = set()
for _ in range(n):
    country = input().strip()
    country_set.add(country)
print(len(country_set))
