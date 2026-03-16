def solution(n):
    n = str(n)
    n = sorted(n, reverse = True)
    return int("".join(n))