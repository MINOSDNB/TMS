m = int(input('enter m number - '))
n = int(input('enter n number - '))
dict = {}
for number in range(m, n + 1):
    dict[number] = []
    for i in range(2, number):
        if number % i == 0:
            dict[number].append(i)
for i in dict.items():
    print(i)

