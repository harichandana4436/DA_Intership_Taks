#hackerrank:-https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
n = int(input())
s = set(map(int, input().split()))
num_commands = int(input())
for _ in range(num_commands):
    command_input = input().split()
    command_name = command_input[0]
    if command_name == "pop":
        s.pop()
    else:
        argument = int(command_input[1])
        getattr(s, command_name)(argument)
print(sum(s))
