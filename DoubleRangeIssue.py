val = 10000.0

for x in range(1000000):
    val = val + 0.000001

val = val - 10000.0

print(val)