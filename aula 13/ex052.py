n = int(input('Digite um numero: '))
p = 0
for c in range(0, n+1):
    if c % n == 0:
        p += 1
print(p)
