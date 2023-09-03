import sys
input = sys.stdin.readline
N, k = map(int, input().split())
a = list(map(int, input().split()))
a = list(reversed(sorted(a))) # 정렬한 후 뒤집는다 = 내림차순
# TypeError: 'list_reverseiterator' object is not subscriptable
# 리스트가 아닌데 왜 리스트로 사용하냐
print(a[k-1])