#hackerrank:-https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for _ in range(n):
    mobile_number = input().strip()
    if re.match(r'^[789]\d{9}$', mobile_number):
        print("YES")
    else:
        print("NO")
