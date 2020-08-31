def sum_2(max_num_1,max_num_2 ):
    """两个数相加的和组成的列表"""
    list_1 = list(range(1, max_num_1 + 1))
    list_2 = list(range(1, max_num_2 + 1))
    results = []

    for num1 in list_1:
        for num2 in list_2:
            result = num1 + num2
            results.append(result)
    return set(results)

def sum_3(max_num_1,max_num_2,max_num_3 ):
    """三个数相加的和组成的列表"""
    list_1 = list(range(1, max_num_1 + 1))
    list_2 = list(range(1, max_num_2 + 1))
    list_3 = list(range(1, max_num_3 + 1))
    results = []

    for num1 in list_1:
        for num2 in list_2:
            for num3 in list_3:
                result = num1 + num2 + num3
                results.append(result)
    return set(results)

def multip(max_num_1,max_num_2):
    """两个数相乘的和组成的列表"""
    list_1 = list(range(1, max_num_1 + 1))
    list_2 = list(range(1, max_num_2 + 1))
    results = []

    for num1 in list_1:
        for num2 in list_2:
            result = num1 * num2
            results.append(result)
    return set(results)

sum_11 = multip(2,3)
print(sum_11)