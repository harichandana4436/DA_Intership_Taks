#hackerrank:-https://www.hackerrank.com/challenges/py-set-mutations/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set_a = set(map(int, input().split()))
num_other_sets = int(input())
for _ in range(num_other_sets):
    operation_name = input().split()[0]
    other_set = set(map(int, input().split()))
    getattr(set_a, operation_name)(other_set)

print(sum(set_a))
