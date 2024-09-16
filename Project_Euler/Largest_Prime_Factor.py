def main(n):
    factor = 2
    while n%factor == 0:
        n //= factor

    factor = 3
    while factor * factor <= n:
        while n%factor == 0:
            n //= factor
        factor += 2

    if n > 2:
        return n
    return factor

if __name__ == "__main__":
    num = 600851475143
    result = main(num)
    print(result)