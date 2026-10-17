#hackerrank:-https://www.hackerrank.com/challenges/py-check-subset/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
num_test_cases = int(input())

for _ in range(num_test_cases):
    a_count = input()
    set_a = set(map(int, input().split()))
    b_count = input()
    set_b = set(map(int, input().split()))
    print(set_a.issubset(set_b))
