import sys
input = sys.stdin.readline

N, M = map(int, input().split())
add = {}
print(N, M)
for i in range(N):
    site, ps = input().split()
    add[site] = ps

for i in range(M):
    print("\n", add[input().rstrip()])