import math


def rand():
    return random.random()


def pr(mu):
    if mu < 88:
        a = rand()
        p_it = exp(-10)
        m = 1
        while (a - p_it) >= 0:
            a = a - p_it
            p_it = p_it * (mu / m)
            m = m + 1
        return m
    else:
        h = exp(-mu)
        m = 0
        res = 1
        while res >= h:
            res *= rr(LOW, UP)
            m = m + 1
        return m


# формируем вектор частот


def countres(r, n):
    s < - 0

    for i in 1: r.__length__:

        if r[i] == n:
            s = s + 1

    return s


# формируем выборку из 10000 значений


if __name__ == "__main__":
    random.seed()
    num_of_intervals = 10
    mu = 10
    array = []
    for i in range(num_of_intervals):
        array.append(pr(mu))
    p = 0.5
    r = []
    for i in range(N):
        r < -c(r, IRNGEO_1(p))

    x < - 0: max(r)

    f < - c()

    for i in x:
        f < - c(f, countres(r, i))

    sum(f)

    hi < - data.frame(x, f)

    # выборочная средняя

    x.mean < - 1 / N * sum(x * f)

    hi < - data.frame(hi, x * f)

    # в качестве оценки:

    x.p < - 1 / (1 + x.mean)

    # теоретическое значение вероятности: p(k)=(1-x.p)^x*x.p

    x.px < - (1 - x.p) ^ x * x.p

    hi < - data.frame(hi, x.px)

    x.nk < - N * x.px

    hi < - data.frame(hi, x.nk)

    x.hi < - (f - x.nk) ^ 2 / (x.nk)

    hi < - data.frame(hi, x.hi)

    sum(x.hi)
