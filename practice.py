import tkinter as tk
import math

# Function to handle button clicks
def on_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            exp = screen.get()
            exp = exp.replace("×", "*").replace("÷", "/").replace("^", "**")
            exp = exp.replace("sin(", "math.sin(math.radians(").replace("cos(", "math.cos(math.radians(").replace("tan(", "math.tan(math.radians(")
            exp = exp.replace("log(", "math.log10(")
            exp = exp.replace("√(", "math.sqrt(")
            result = eval(exp)
            screen.set(result)
        except Exception:
            screen.set("Error")

    elif text == "AC":
        screen.set("")

    elif text == "⌫":  # Backspace
        screen.set(screen.get()[:-1])

    else:
        screen.set(screen.get() + text)

# Creating main window
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("400x600")
root.configure(bg="#1e1e2e")  # Dark Purple background
root.resizable(True, True)  # Making the window resizable

# Screen Entry
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font=("Arial", 24), bg="#282a36", fg="white", bd=10, relief="flat", insertbackground='white', justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, ipady=10, padx=10, pady=10)

# Button styling
button_colors = {
    "default": {"bg": "#44475a", "fg": "white", "active_bg": "#6272a4"},
    "operators": {"bg": "#ff5555", "fg": "white", "active_bg": "#ff6e6e"},
    "special": {"bg": "#50fa7b", "fg": "black", "active_bg": "#69ff94"},
    "equal": {"bg": "#bd93f9", "fg": "black", "active_bg": "#d6acff"}
}

button_font = ("Arial", 18, "bold")

# Button Layout
buttons = [
    ["AC", "sin(", "cos(", "tan(", "⌫"],
    ["7", "8", "9", "÷", "log("],
    ["4", "5", "6", "×", "("],
    ["1", "2", "3", "-", ")"],
    ["0", ".", "√(", "+", "="]
]

for row in buttons:
    frame = tk.Frame(root, bg="#1e1e2e")
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        style = button_colors["default"]
        if btn_text in ["÷", "×", "-", "+"]:
            style = button_colors["operators"]
        elif btn_text in ["AC", "⌫", "sin(", "cos(", "tan(", "log(", "√("]:
            style = button_colors["special"]
        elif btn_text == "=":
            style = button_colors["equal"]
        
        btn = tk.Button(frame, text=btn_text, font=button_font, bg=style["bg"], fg=style["fg"],
                        activebackground=style["active_bg"], activeforeground=style["fg"],
                        height=2, width=5, relief="ridge", borderwidth=2)
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        btn.bind("<Button-1>", on_click)

# Run the application
root.mainloop()