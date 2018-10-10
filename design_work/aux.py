def get_table_list(flat_list, columns=4, rows=3):
    table_list = []
    table = []
    row = []
    max = len(flat_list)
    for i, el in enumerate(flat_list, 1):
        if i > 1 and (i - 1) % (columns * rows) == 0:
            table.append(row.copy())
            table_list.append(table.copy())
            table = []
            row = []
        elif i > 1 and (i - 1) % columns == 0:
            table.append(row.copy())
            row = []
        row.append(el)
        if i == max:
            table.append(row.copy())
            table_list.append(table.copy())
    return table_list


if __name__ == '__main__':

    arr = range(1, 20)
    print(arr)



    print(get_table_list(arr))