import math


def genA(n):
    a = []
    for i in range(n):
        new_element = i
        a.append(math.sin(new_element))
    return a


def solution(A):
    direction = 0
    cur_direction = 0
    count = 0
    for i in range(len(A) - 1):
        if A[i] < A[i + 1]:
            cur_direction = 1
            if direction != cur_direction:
                direction = cur_direction
                count += 1
        elif A[i] > A[i + 1]:
            cur_direction = -1
            if direction != cur_direction:
                direction = cur_direction
                count += 1
    return count + 1


def main():
    A = [1, 2, 1, 2, 1, 2, 1, 2]
    print(solution(A))


if (__name__ == "__main__"):
    main()
