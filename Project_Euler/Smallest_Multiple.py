import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def smallest_multiple(limit):
    multiple = 1
    for i in range(2, limit + 1):
        multiple = lcm(multiple, i)
    return multiple

if __name__ == "__main__":
    result = smallest_multiple(20)
    print(result)
