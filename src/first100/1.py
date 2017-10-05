def sum_series(a, l):
    return (l / a) * (a + l) / 2


print(sum_series(3, 999) + sum_series(5, 995) - sum_series(15, 990))
