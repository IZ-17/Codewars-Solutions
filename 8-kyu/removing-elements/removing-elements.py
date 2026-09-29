def remove_every_other(my_list):
    return [x for index, x in enumerate(my_list) if index % 2 == 0]