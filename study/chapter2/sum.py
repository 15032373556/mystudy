def sum(max_num_1,max_num_2 ):
    list_1 = list(range(1, max_num_1 + 1))
    list_2 = list(range(1, max_num_2 + 1))
    results = []

    for num1 in list_1:
        for num2 in list_2:
            result = num1 + num2
            results.append(result)
    return results
    # print(set(results))

sum_6_8 = sum(6,8)
# for num in sum_6_8:
#     print(num)
sum_1 = set(sum_6_8)
for num in sum_1:
    print(num)
