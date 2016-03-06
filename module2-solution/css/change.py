def get_change(n):
    d10 = 0
    d5 = 0
    d1 = 0
    while n > 0:
        if n > 10:
            n -= 10
            d10 += 1
        elif n > 5:
            n -= 5
            d5 += 1
        elif n > 1:
            n -= 1
            d1 += 1
    if d10*10 + d5*5 + d1 == n:
        return d10 + d5 + d1
    else:
        return -1

# if __name__ == '__main__':
n = int(input('Enter the amount:'))
print(get_change(n))