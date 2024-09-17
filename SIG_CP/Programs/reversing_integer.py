def reverse_integer(n):
    reversed_n = 0
    sign = 1 if n >= 0 else -1
    n = abs(n)
    
    while n != 0:
        remainder = n % 10
        reversed_n = reversed_n * 10 + remainder
        n = n // 10
    
    return sign * reversed_n

def main():
    number = int(input())
    print("Original Integer:", number)
    print("Reversed Integer:", reverse_integer(number))

if __name__ == "__main__":
    main()