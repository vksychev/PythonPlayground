import random


def get_seq(n, r):
    sq = []
    for i in range(n):
        sq.append(random.randint(0, 2 ** r - 1))
    return sq


def sum(n):
    sum = 0
    for i in n:
        sum += i
    return sum


def generate():
    n = 10
    m = 4
    seq = get_seq(n, m)
    d = 2 ** m - 1
    alpha = random.randint(0, d)
    betta = random.randint(0, d)
    if alpha > betta:
        alpha, betta = betta, alpha
    abseq = []
    nseq = []
    n = 0
    for i in seq:
        if alpha <= i <= betta:
            abseq.append(i)
            nseq.append(n)
        n = n + 1
    print("Вход: {}".format(seq))
    print("m = {}".format(m))
    print("a = {}, b = {}".format(alpha, betta))
    print("Интервалы: ".format(nseq))
    lenseq = []
    for i in range(nseq.__len__() - 1):
        lenseq.append(nseq[i + 1] - nseq[i] - 1)
    print(lenseq)
    u = sum(lenseq)
    x = []
    delta = (betta - alpha)
    s = 2 ** m
    for i in range(lenseq.__len__()):
        hi = ((lenseq[i] - u * delta * ((1 - delta / s) ** i) / s) ** 2) / (u * delta * ((1 - delta / s) ** i) / s)
        x.append(hi)
    print("hi: {}".format(sum(x)))


def cheat_gen(e, m, a, b):
    seq = e
    alpha = a
    betta = b
    if alpha > betta:
        alpha, betta = betta, alpha
    abseq = []
    nseq = []
    n = 0
    for i in seq:
        if alpha <= i <= betta:
            abseq.append(i)
            nseq.append(n)
        n = n + 1
    print("Вход: {}".format(seq))
    print("m = {}".format(m))
    print("a = {}, b = {}".format(alpha, betta))
    print("Интервалы: ".format(nseq))
    lenseq = []
    for i in range(nseq.__len__() - 1):
        lenseq.append(nseq[i + 1] - nseq[i] - 1)
    print(lenseq)
    u = sum(lenseq)
    x = []
    delta = (betta - alpha)
    s = 2 ** m
    for i in range(lenseq.__len__()):
        hi = ((lenseq[i] - u * delta * ((1 - delta / s) ** i) / s) ** 2) / (u * delta * ((1 - delta / s) ** i) / s)
        x.append(hi)
    print("hi: {}".format(sum(x)))


if __name__ == "__main__":
    random.seed()
    generate()
    #cheat_gen((0, 5, 4, 1, 0, 4, 6, 1),3,0,2)
