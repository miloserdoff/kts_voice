n = input('Введите: ')
k = []
with open(f'{n}.txt') as f:
    k.append(f.read())


print(k)
