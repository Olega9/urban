def calculate_structure_sum(data):
    total = 0
    if isinstance(data, int):
        total += data
    elif isinstance(data, str):
        total += len(data)

    elif isinstance(data, (list, tuple, set)):
        for item in data:
            total += calculate_structure_sum(item)

    elif isinstance(data, dict):
        for key, value in data.items():
            total += calculate_structure_sum(key)
            total += calculate_structure_sum(value)

    return total
