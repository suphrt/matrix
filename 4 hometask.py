# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
    n = int(input("n - "))
    m = int(input("m - "))
    A = []
    for _ in range(n):
        row = list(map(int, input().split()))
        assert len(row) == m
        A.append(row)

    for i in range(n - 1):
        for j in range(m - 1):
            cntrow = len([A[i][j] for A[i][j] in i if A[i][j] == 0])
            if cntrow == n:
                del A[i]
    for j in range(m - 1):
        for j in range(n - 1):
            cntrow = len([A[i][j] for A[i][j] in j if A[i][j] == 0])
            if cntrow == n:
                del A[j]
    print(A)