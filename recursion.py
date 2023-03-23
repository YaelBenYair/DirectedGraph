def sum_digits(n):
    if n == 0:
        return n
    return n % 10 + sum_digits(n // 10)


def harmonic_sum(n):
    if n == 1:
        return 1

    return 1 / n + (harmonic_sum(n - 1))


def stars(n: int):
    if n < 1:
        return n
    print('* ' * n)
    if n > 2:
        print(n * stars(n - 2))
    return "* "


print(sum_digits(5264))
print(harmonic_sum(5))
stars(6)
stars(5)
