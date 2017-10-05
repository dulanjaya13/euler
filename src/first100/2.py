fx = 1
fy = 1
tot = 0
while fy < 4000000:
    fx, fy = fy, fx + fy
    if fy % 2 == 0:
        tot += fy
print(tot)
