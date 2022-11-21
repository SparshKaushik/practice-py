def max_of_three(a, b, c):
    if a>b:
        if a>c:
            print(f"{a} is the Largest")
        else:
            print("{} is the Largest".format(c))
    else:
        if b>c:
            print(f"{b} is the Largest")
        else:
            print("{} is the Largest".format(c))

if __name__ == "__main__":
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))
    c = int(input("Enter Third Number : "))
    max_of_three(a, b, c)