def group_by_surname(list_of_enrollees):
    list_of_groups = [["A", "B", "C", "D", "E", "F", "G", "H", "I"],
                      ["J", "K", "L", "M", "N", "O", "P"],
                      ["Q", "R", "S", "T"],
                      ["U", "V", "W", "X", "Y", "Z"]]

    count_groups = [0, 0, 0, 0]

    for i in range(len(list_of_enrollees)):
        enrollee_name = list_of_enrollees[i].split(" ")
        letter = enrollee_name[1][:1]

        for i in range(len(list_of_groups)):
            if letter in list_of_groups[i]:
                count_groups[i] += 1

    var_a, var_j, var_q, var_u = count_groups
    return var_a, var_j, var_q, var_u



list_of_names = ["Jaz Z", "Will Smith", "Robby Williams", "Ujean Poloz", "Sabina Poloz",
                 "Jhon Doe", "Ivan Petrenko", "Gabe Didih"]

list_of_names2 = ["A I", "B J", "C T", "D U"]


print(group_by_surname(list_of_names2))