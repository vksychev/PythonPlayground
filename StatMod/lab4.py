# Variant 7
import random
from math import log


def orx(*x):
    res = False
    for i in x:
        res = res | i
    return res


def andx(*x):
    res = True
    for i in x:
        res = res & i
    return res


def lfrs(x, T):
    s1 = orx(andx(x[0] > T, x[1] > T), andx(x[2] > T, x[3] > T))
    s2 = andx(x[4] > T, x[5] > T)
    s3 = orx(andx(x[6] > T, x[7] > T), andx(x[8] > T, x[9] > T), andx(x[10] > T, x[11] > T))
    s4 = orx(x[12] > T, x[13] > T)
    return not (andx(s1, s2, s3, s4))


def expn(l):
    r = random.uniform(0, 1)
    return -log(r) / l


def generate(n, L):
    lm = (4 * 10 ** -6, 10 ** -6, 8 * 10 ** -6, 3 * 10 ** -6)
    m = 4
    r = (4, 2, 6, 4)
    T = 8760
    count = 0
    for k in range(n):
        seq = []
        for i in range(m):
            temp = []
            for j in range(r[i]):
                temp.append(expn(lm[i]))
            for j in range(L[i]):
                s = min(temp)
                c = 0
                for t in temp:
                    if t == s:
                        s = c
                    c = c + 1
                temp[s] += expn(lm[i])
            seq += temp
        count += lfrs(seq, T)

    return 1 - count / N


if __name__ == "__main__":
    random.seed()
    Po = 0.995
    N = 33008
    L = [9, 9, 9, 9]
    print(generate(N, L))
    for i in range(10):
        L[0] = i
        for j in range(10):
            L[1] = j
            for k in range(10):
                L[2] = k
                for s in range(10):
                    L[3] = s
                    P = generate(N, L)
                    if P > Po:
                        print('P = {}'.format(P))
                        print(L)
                        print(sum(L))

    # generate(N, L)
