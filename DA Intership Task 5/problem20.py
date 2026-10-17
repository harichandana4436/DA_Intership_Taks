#hackerrank:-https://www.hackerrank.com/challenges/piling-up/problem
num_test_cases = int(input())
for _ in range(num_test_cases):
    n = int(input())
    cubes = list(map(int, input().split()))
    left = 0
    right = n - 1
    last_stacked = float('inf')
    possible = "Yes"
    while left <= right:
        if cubes[left] >= cubes[right]:
            current_cube = cubes[left]
            left += 1
        else:
            current_cube = cubes[right]
            right -= 1
        if current_cube > last_stacked:
            possible = "No"
            break
            
        last_stacked = current_cube
        
    print(possible)
