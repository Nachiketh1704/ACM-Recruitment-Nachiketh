def reverse_string(s):
    reversed_s = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_s += s[i]
    return reversed_s

def main():
    string = str(input())
    print("Original String:", string)
    print("Reversed String:", reverse_string(string))

if __name__ == "__main__":
    main()