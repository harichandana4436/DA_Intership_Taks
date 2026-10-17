#hackerrank:-https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
#Introduction to Sets
def average(array):
    # your code goes here
    distinct_heights = set(array)
    avg = sum(distinct_heights) / len(distinct_heights)
    return round(avg, 3)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
