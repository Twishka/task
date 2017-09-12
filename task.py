from math import sqrt


def check(result):
    l = str(result)
    for i in range(len(l)/2):
        if l[i] != l[-i - 1]:
            return False
    else:
        return True


def make_number_list():
    lst = []

    for number in range(10000, 99999):
        for i in range(2, int(sqrt(number))):
            if number % i == 0:
                break
        else:
            lst.append(number)
    return sorted(lst, reverse=True)


def multiply(factors):
    for i in factors:
        for j in factors:
            result = i * j
            if check(result) is True:
                return (result, (i, j))


def main():
    factors = make_number_list()
    results = multiply(factors)
    print(results)


main()