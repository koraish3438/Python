import tkinter as tk

def on_button_click(value):
    if value == "=":
        try:
            result = eval(entry_field.get())
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, str(result))
        except:
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, "ERROR")
    elif value == "C":
        entry_field.delete(0, tk.END)
    else:
        entry_field.insert(tk.END, value)

root = tk.Tk()
root.title("Calculator")

entry_field = tk.Entry(root, width=25, font=("Arial", 18, "bold"), bd=5, bg="aqua", fg="black")
entry_field.grid(row=0, column=0, columnspan=4, ipady=10)

buttons = [
    ('7', 1, 0, "gray"), ('8', 1, 1, "gray"), ('9', 1, 2, "gray"), ('/', 1, 3, "blue"),
    ('4', 2, 0, "gray"), ('5', 2, 1, "gray"), ('6', 2, 2, "gray"), ('*', 2, 3, "blue"),
    ('1', 3, 0, "gray"), ('2', 3, 1, "gray"), ('3', 3, 2, "gray"), ('-', 3, 3, "blue"),
    ('C', 4, 0, "red"), ('0', 4, 1, "gray"), ('=', 4, 2, "green"), ('+', 4, 3, "blue")
]

for (text, row, col, color) in buttons:
    button = tk.Button(root, text=text, width=5, height=3, font=("Arial",18), bg=color, fg="black", command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col)

root.mainloop()