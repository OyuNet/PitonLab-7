def power(base, exponent):
    if (exponent > 0): return base * power(base, exponent-1)
    else: return 1