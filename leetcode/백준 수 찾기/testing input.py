from sys import stdin, stdout

answer = []

n = stdin.readline()
N = set(map(int,stdin.readline().split()))
m = stdin.readline()
M = list(map(int, stdin.readline().split()))

# print(n)
# print(N)
# print(m)
# print(M)

for i in range(len(M)):
    if M[i] in N:
        print("1")
    else:
        print("0")