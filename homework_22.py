def group_by_surname(list_of_enrollees):

    groups = [['A', 'B', 'C', 'D', 'E', 'F', 'J', 'G', 'H', 'I'],
              ['J', ' K', 'L', 'M', 'N', 'O', 'P'],
              ['Q', 'R', 'S', 'T'],
              ['U', 'V', 'W', 'X', 'Y', 'Z']]

    count_groups = [0] * 4

    for i in range(len(list_of_enrollees)):
        var_i = list_of_enrollees[i].split(' ')
        letter = var_i[1][:1]

        for i in range(len(groups)):
            for j in range(len(groups[i])):
                if letter == groups[i][j]:
                    count_groups[i] += 1


    return count_groups



list_of_names = ['Jaz Z', 'Will Smith', 'Robby Williams', 'Ujean Poloz', 'Sabina Poloz',
                 'Jhon Doe', 'Ivan Petrenko', 'Gabe Didih']



print(group_by_surname(list_of_names))