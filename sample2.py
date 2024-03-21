# def hello_user(name,age):
#     return f"Hello {name} who is {age} years old"

# print(hello_user('Venkat',22))
from pathlib import Path

path = Path()
files = path.glob('*.py')

for file in files:
    print(file)