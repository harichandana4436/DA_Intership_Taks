#hackerrank:-https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    largest_number=arr[0]
    second_largest=arr[0]
    for i in arr:
        if i > largest_number:
            second_largest= largest_number
            largest_number=i
        elif i > second_largest and i != largest_number:
            second_largest=i
        elif second_largest == largest_number and i < largest_number:
            second_largest=i
    print(second_largest)