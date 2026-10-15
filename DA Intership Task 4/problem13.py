# hackerrank:-https://www.hackerrank.com/challenges/symmetric-difference/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
set_a = set(map(int, input().split()))
n = int(input())
set_b = set(map(int, input().split()))

sym_diff = set_a ^ set_b

sorted_result = sorted(list(sym_diff))

for num in sorted_result:
    print(num)
