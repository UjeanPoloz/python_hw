import random

def my_shuffle(lst):
    virtual_list = list(lst)
    len_list = len(lst)
    random_ind = [''] * len_list

    for i in range(len_list):
        while True:
            var = random.randint(0,len_list-1)
            if var not in random_ind:
                random_ind[i] = var
                break

    for ind, res in enumerate(random_ind):
        lst[ind] = virtual_list[res]


def pemrtuate(text, split_word_num = 3):
    permuted_text = []

    list_word = text.split(' ')

    for i in range(len(list_word)):
        permuted_word = ''

        work_word = list_word[i]

        if len(work_word) == 1:
            permuted_text.append(work_word + ' ')

        else:
            work_area = list(work_word[1:-1])
            len_work_area = len(work_area)
            count = len_work_area // split_word_num

            if len_work_area - count == split_word_num - 1:
                my_shuffle(work_area)

            else:
                split_groups = [work_area[x:x + split_word_num] for x in range(0, len(work_word[1:-1]), split_word_num)]
                work_area = ''

                for group in split_groups:
                    my_shuffle(group)
                    work_area += ''.join(group)

            permuted_word = work_word[0] + ''.join(work_area) + work_word[-1]

            permuted_text.append(permuted_word + ' ')

    return ''.join(permuted_text).strip()


text = 'Особенно подкупает простота работы с различными структурами данных'

print(pemrtuate(text))