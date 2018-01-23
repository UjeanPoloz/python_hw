def group_by_surname(list_of_enrollees):
    list_of_groups = [["A", "B", "C", "D", "E", "F", "J", "G", "H", "I"],
                      ["J", "K", "L", "M", "N", "O", "P"],
                      ["Q", "R", "S", "T"],
                      ["U", "V", "W", "X", "Y", "Z"]]
    count_groups = [0, 0, 0, 0]
    for i in range(len(list_of_enrollees)):
        var_i = list_of_enrollees[i].split(' ')
        letter = var_i[1][:1]
        for i in range(len(list_of_groups)):
            for j in range(len(list_of_groups[i])):
                if letter == list_of_groups[i][j]:
                    count_groups[i] += 1
    var_a, var_j, var_q, var_u = count_groups
    return var_a, var_j, var_q, var_u



list_of_names = ["Jaz Z", "Will Smith", "Robby Williams", "Ujean Poloz", "Sabina Poloz",
                 "Jhon Doe", "Ivan Petrenko", "Gabe Didih"]

list_of_names2 = ["A A", "A B", "A C", "A D"]


print(group_by_surname(list_of_names2))