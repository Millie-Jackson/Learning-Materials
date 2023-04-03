my_list = [1, 2, 3, 3, 3, 4, 5]


def unique(original_list):
    unique_list = []

    for x in original_list:
        if x not in unique_list:
            unique_list.append(x)

    if unique_list == 0:
        print("All elements are unique")
    else:
        print("There are duplicate elements")
