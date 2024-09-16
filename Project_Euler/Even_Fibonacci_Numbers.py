def main():
    limit = 4000000
    a, b = 1, 2
    sum = 0

    while a <= limit:
        if a%2 == 0:
            sum += a
        a, b = b, a+b
    
    print(sum)

if __name__ == "__main__":
    main()