def main(n):
    return str(n) == str(n)[::-1]

def largest_palindrome():
    largest = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if main(product) and product > largest:
                largest = product
    return largest

if __name__ == "__main__":
    result = main()
    print(result)
