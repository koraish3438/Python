import tkinter as tk
import math

# ফাংশন: ইউজার ইনপুট হ্যান্ডেল করা
def on_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            exp = screen.get()
            exp = exp.replace("×", "*").replace("÷", "/").replace("^", "**")

            # ট্রিগনোমেট্রি ও লগ ফাংশন ঠিক করা
            exp = exp.replace("sin(", "math.sin(math.radians(").replace("cos(", "math.cos(math.radians(").replace("tan(", "math.tan(math.radians(")
            exp = exp.replace("log(", "math.log10(").replace("ln(", "math.log(")

            # √ (square root) ফিক্স করা
            exp = exp.replace("√", "math.sqrt(")  # এখন `√25` দিলে `5.0` আসবে

            # π ও e সঠিকভাবে পরিবর্তন করা
            exp = exp.replace("π", str(math.pi)).replace("e", str(math.e))

            result = eval(exp)  # Safe eval
            screen.set(result)

        except Exception:
            screen.set("Error")

    elif text == "AC":
        screen.set("")

    elif text == "⌫":  # Backspace
        screen.set(screen.get()[:-1])

    else:
        screen.set(screen.get() + text)

# উইন্ডো তৈরি
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("380x600")
root.configure(bg="black")

# স্ক্রিন তৈরি
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20", bg="black", fg="white", bd=10, insertbackground='white', justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)

# ক্যালকুলেটরের বোতাম
buttons = [
    ["sin(", "cos(", "tan(", "log(", "ln("],
    ["√(", "π", "e", "^", "AC"],
    ["7", "8", "9", "÷", "⌫"],
    ["4", "5", "6", "×", "("],
    ["1", "2", "3", "-", ")"],
    ["0", "00", ".", "+", "="]
]

for row in buttons:
    frame = tk.Frame(root, bg="black")
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 18", bg="#222", fg="white", height=2, width=4, relief="ridge")
        btn.pack(side="left", expand=True, fill="both")
        btn.bind("<Button-1>", on_click)

root.mainloop()
