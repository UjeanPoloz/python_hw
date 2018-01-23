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


def pemrtuate(text):

    permuted_text = ''

    list_word = text.split(' ')

    for i in range(len(list_word)):
        permuted_word = ''

        work_word = list_word[i]

        if len(work_word) == 1:
            permuted_text = permuted_text + ' ' + work_word

        else:
            work_area = list(work_word[1:len(work_word) - 1])
            len_work_area = len(work_area)
            count = len_work_area // 3

            if len_work_area - count == 2:
                my_shuffle(work_area)

            else:
                separate_three = [work_area[x:x + 3] for x in range(0, len(work_word[1:-1]), 3)]

                for i in range(len(separate_three)):
                    my_shuffle(separate_three[i])
                    work_area = ''
                    for j in range(len(separate_three)):
                        work_area += ''.join(separate_three[j])

        permuted_word = work_word[0] + ''.join(work_area) + work_word[-1]

        permuted_text = permuted_text + ' ' + permuted_word

        if permuted_text[0] == ' ':
           permuted_text = permuted_text[1:]

    return permuted_text


text = 'Особенно подкупает простота работы с различными структурами данных'

print(pemrtuate(text))