def add_numbers(x: int, y: int) -> int:
    "function to add two numbers"
    return x + y


print(add_numbers.__annotations__)
print(add_numbers.__doc__)

print("--- name/module ---")
print(add_numbers.__name__)
print(add_numbers.__module__)


print("--- defaults/kwargs ---")
print(add_numbers.__defaults__)
print(add_numbers.__kwdefaults__)

print("--- code/globals ---")
print(add_numbers.__code__)
print(add_numbers.__globals__)

print("--- dict/closure ---")
print(add_numbers.__dict__)
print(add_numbers.__closure__)
