def sumDigit(number):
    if (not number == 0): return number % 10 + sumDigit(number // 10)
    else: return 0

print(sumDigit(12345))