def find_mode(array):
    new_arr = set(array)
    max_count = 0
    mode = []
    for val in new_arr:
        i = array.count(val)
        if i > max_count:
            max_count = i
            mode = [val]
        elif i == max_count:
            mode.append(val)
    if len(mode) == 1:
        return mode[0]
    else:
        return mode


print(find_mode(["a", "b", "a", "a", 3, 3, 3, 2, "hello", "b"]))
