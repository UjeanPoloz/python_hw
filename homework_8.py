import homework_8_names as list_names

loc_list_names = list_names.list_full_names

index_loc_list = len(loc_list_names)

true_name = []

def separate (symbol = ' '):
    separate_symbol = str(symbol)
    return separate_symbol

for ind in range(index_loc_list):
    full_name = loc_list_names[ind]
    index_space = full_name.find(' ')
    first_name = full_name[:index_space]
    last_name = full_name[index_space + 1:]
    true_name.append(last_name + separate() + first_name)

print('Default name: %s\n\n'
      'Edited name:  %s' % (loc_list_names, true_name))

