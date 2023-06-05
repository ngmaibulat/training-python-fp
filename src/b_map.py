double = lambda x: x * 2


# Example 2: Capitalizing names using map
names = ["alice", "bob", "charlie"]
capitalized = map(str.capitalize, names)

print(list(capitalized))  # Output: ["Alice", "Bob", "Charlie"]


# func: double array
def double_arr(arr: list) -> list:
    res = map(double, arr)
    return list(res)


# func: capitalize names
def capitalize_names(names: list) -> list:
    res = map(str.capitalize, names)
    return list(res)
