

if __name__ == '__main__':
    a = True
    b = True
    c = [True, False, True, True]
    d = [True, True, True]

    for i in c:
        a *= i
    print(a)

    for i in d:
        b *= i
    print(b)
