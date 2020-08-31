sandwich_orders = ['vegetable sandwich','beef sandwich','cheese sandwich']
finished_sandwichs = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + ".")
    finished_sandwichs.append(current_sandwich)

print("\nThe following sandwichs have been finished:")
for finished_sandwich in finished_sandwichs:
    print(finished_sandwich.title())

