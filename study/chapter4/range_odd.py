#奇数
odds = []

for number in range(1,21):
    if number % 2  != 0:
        odds.append(number)

for odd in odds:
    print(odd)