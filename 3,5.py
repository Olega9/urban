def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) == 1:
        return int(str_number)
    first = int(str_number[0])
    if first == 0:
        return get_multiplied_digits(int(str_number[1:]))
    return first * get_multiplied_digits(int(str_number[1:]))
result = get_multiplied_digits(420)
print(result)
