import cowsay
from tabulate import tabulate
data = {
    "a": {"x": 1, "y": 2},
    "b": {"x": 6, "y": "u"},
    "c": {"x": 3, "y": 1},
    "d": {"x": 14, "y": 29},
}
rows = []

for key, values in data.items():
    rows.append([key, values["x"], values["y"]])

# print(tabulate(rows, headers=["", "x", "y"], tablefmt="grid"))

print(cowsay.tux("hello"))
