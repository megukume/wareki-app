import tkinter as tk


def convert():
    year = int(entry.get())

    if year >= 2019:
        wareki = f"令和{year - 2018}年"

    elif year >= 1989:
        wareki = f"平成{year - 1988}年"

    elif year >= 1926:
        wareki = f"昭和{year - 1925}年"

    elif year >= 1912:
        wareki = f"大正{year - 1911}年"

    elif year >= 1868:
        wareki = f"明治{year - 1867}年"

    else:
        wareki = "明治以前"

    result_label.config(text=wareki)


root = tk.Tk()
root.title("西暦→和暦変換")
root.geometry("300x180")

title_label = tk.Label(
    root,
    text="西暦を入力してください",
    font=("Meiryo", 10)
)
title_label.pack(pady=10)

entry = tk.Entry(
    root,
    font=("Meiryo", 12),
    justify="center"
)
entry.pack()

button = tk.Button(
    root,
    text="変換",
    command=convert
)
button.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Meiryo", 14, "bold")
)
result_label.pack()

root.mainloop()