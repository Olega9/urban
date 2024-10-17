calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    list_lower = [item.lower() for item in list_to_search]
    return string_lower in list_lower

result1 = string_info("Hello World!")
print(result1)

result2 = is_contains("Urban", ["city", "suburban", "urban", "metropolitan"])
print(result2)

result3 = string_info("Python")
print(result3)

result4 = is_contains("python", ["C", "Java", "PYTHON", "Go"])
print(result4)

print(f"Количество вызовов функций: {calls}")
