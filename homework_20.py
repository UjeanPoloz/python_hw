import random

def diff_positive_negative(num_limit, ind = 100, lower_bound = -100, upper_bound = 100):
    negative_var = 0
    positive_var = 0

    for i in range(ind):
        num_limit.append(random.randint(lower_bound, upper_bound))

        if num_limit[i] < 0:
            negative_var = negative_var + num_limit[i]
        elif num_limit[i] > 0:
            positive_var = positive_var + num_limit[i]

        diff = positive_var + negative_var

    print(num_limit)

    return diff

def diff_even_odd(num_limit, ind = 100, lower_bound = 0, upper_bound = 100):
    even = 0
    odd = 0
    zero = 0

    for i in range(ind):
        num_limit.append(random.randint(lower_bound, upper_bound))

        if num_limit[i] % 2:
            even += num_limit[i]
        elif num_limit[i] == 0:
            zero += 1
        else:
            odd += num_limit[i]

        diff = abs(even - odd)

    return diff

lst = []

print(diff_even_odd(lst))
