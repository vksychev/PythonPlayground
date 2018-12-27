def solution(n):
    d = [0] * 30
    l = 0
    while (n > 0):
        d[l] = n % 2
        n //= 2
        l += 1
    print(d)
    for p in range(1, l//2+1):
        ok = True
        for i in range(l - p):
            if d[i] != d[i + p]:
                ok = False
                break
        if ok:
            return p
    return -1


def main():
    A = 536870913
    print("sol ",solution(A))
    print(2**29)

if (__name__ == "__main__"):
    main()
