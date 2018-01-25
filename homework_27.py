import random, re

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

def permute_word(word):
    first_symbol = ''
    word_part_one = ''
    center_symbol = ''
    word_part_two = ''
    last_symbol = ''

    if re.match('([\W]+)', word):
        test = ''.join(re.match('([\W]+)', word).groups())
        first_symbol = test

    hard_word = re.match('([\W]*)([\w]+)([\W]+)([\w]+)([\W]*)', word)
    easy_word = re.match('([\W]*)([\w]+)([\W]*)', word)
    only_numbers = re.match('([\d]+)([\W]*)([\d]+)([\W]*)', word)

    if only_numbers:
        pemrtuate_word = ''.join(only_numbers.groups())
        return pemrtuate_word

    if easy_word:
        first_symbol, word_part_one, last_symbol = easy_word.groups()
        word_part_one = spliting_and_shuffling_word(word_part_one)

    if hard_word:
        first_symbol, word_part_one, center_symbol, word_part_two, last_symbol = hard_word.groups()
        word_part_one = spliting_and_shuffling_word(word_part_one)
        word_part_two = spliting_and_shuffling_word(word_part_two)

    pemrtuate_word = first_symbol + word_part_one + center_symbol + word_part_two + last_symbol

    return pemrtuate_word

def spliting_and_shuffling_word(work_word, split_word_num = 3):
    permuted_word = ''

    if len(work_word) == 1:
        permuted_word = work_word

    else:
        work_area = list(work_word[1:-1])
        len_work_area = len(work_area)
        count = len_work_area // split_word_num

        if len_work_area - count == split_word_num - 1:
            my_shuffle(work_area)

        else:
            split_groups = [work_area[x:x + split_word_num] \
                            for x in range(0, len(work_word[1:-1]), split_word_num)]
            work_area = ''

            for group in split_groups:
                my_shuffle(group)
                work_area += ''.join(group)

        permuted_word = work_word[0] + ''.join(work_area) + work_word[-1]
    return permuted_word

def permute_text(text):
    permuted_text = [permute_word(work_word) for work_word in text.split(' ')]

    return ' '.join(permuted_text).strip()

text = 'Может наконец-то заработало. И теперь "все отлавливаем" и 1990-2003 и -n + 23 и n=234. И просто - и 1990 - 2014. и :?№;'

print(permute_text(text))