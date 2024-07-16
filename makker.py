from random import choice


def make_class(students):
    return_dict = {}
    for i in students:
        return_dict[i] = [i]

    return return_dict


def init_list(size, students):
    groups = []
    for i in range(len(students)):
        if i % size == 0:
            groups.append({})
        elif i > len(students) - size - 1:
            groups.append({})
            break
    return groups


def make_groups(size, students):
    groups = init_list(size, students)
    available = list(students)
    for i in groups:
        if len(available) == 0:
            return groups, students
        tmp_choice = choice(available)
        i[tmp_choice] = students[tmp_choice]
        del available[available.index(tmp_choice)]
        unavailable = i[tmp_choice]

        for j in range(1, size):
            if len(available) == 0:
                break
            try:
                tmp_choice = choice(
                    [elem for elem in available if elem not in unavailable]
                )
            except IndexError:
                tmp_choice = choice(available)

            i[tmp_choice] = students[tmp_choice]
            del available[available.index(tmp_choice)]
            unavailable = list(set(unavailable + i[tmp_choice]))

        for j in i:
            students[j] = list(set(list(j) + unavailable))

    return groups, students
