n = int(input())
c1 = []
m = []
for i in range(n):
    c1 = input().split()[:n]
    m.append(c1)
nach, kon = map(int, input().split())
tf = [False] * n

for i in m:
    for l in range(len(i)):
        if type(i[l]) == str:
            i[l] = int(i[l])

w = []
for i in range(n):
    w.append(0)


def A(start):
    global m, w, tf, n
    dest = []
    for x in start:
        for j in range(n):
            if m[x][j] != 0 and tf[j] is False:
                if w[j] == 0:
                    w[j] = m[x][j] + w[x]

                else:
                    if w[j] > m[x][j] + w[x]:
                        w[j] = m[x][j] + w[x]

                dest.append(j)

        tf[x] = True

    dest.sort()

    if len(dest) != 0:
        A(dest)

    else:
        return


A([nach - 1])
print(w[kon - 1])
