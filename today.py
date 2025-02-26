import customtkinter as ctk
import math

# Function to handle button clicks
def on_button_click(value):
    current_text = entry_field.get()
    
    if value == "=":
        try:
            # Evaluate the expression, replacing trigonometric functions
            modified_text = current_text.replace("√(", "math.sqrt(") \
                                           .replace("sin", "math.sin(math.radians(") \
                                           .replace("cos", "math.cos(math.radians(") \
                                           .replace("tan", "math.tan(math.radians(") \
                                           .replace("cot", "1/math.tan(math.radians(") + "))"
            result = eval(modified_text)
            entry_field.delete(0, ctk.END)
            entry_field.insert(ctk.END, str(result))
        except:
            entry_field.delete(0, ctk.END)
            entry_field.insert(ctk.END, "ERROR")
    
    elif value == "C":
        entry_field.delete(0, ctk.END)

    elif value == "DEL":
        entry_field.delete(len(current_text)-1, ctk.END)
    
    elif value == "√(":
        # Insert the square root symbol into the entry field
        entry_field.insert(ctk.END, "√(")
    
    elif value in ["sin", "cos", "tan"]:
        # Insert the trigonometric function symbol into the entry field
        entry_field.insert(ctk.END, value + "(")
    
    else:
        entry_field.insert(ctk.END, value)

# Initialize the CustomTkinter window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Calculator")

# Entry field
entry_field = ctk.CTkEntry(root, width=280, height=50, font=("Arial", 28, "bold"), justify="right", fg_color="#BBB", text_color="#000")
entry_field.grid(row=0, column=0, columnspan=4, pady=10, padx=5)

# Button layout
buttons = [
    ('C', 1, 0, "#db701f"), ('sin', 1, 1, "#3C3636"), ('cos', 1, 2, "#3C3636"), ('DEL', 1, 3, "#db701f"),
    ('tan', 2, 0, "#3C3636"), ('√(', 2, 1, "#3C3636"), ('(', 2, 2, "#3C3636"), (')', 2, 3, "#3C3636"),
    ('7', 3, 0, "#3C3636"), ('8', 3, 1, "#3C3636"), ('9', 3, 2, "#3C3636"), ('/', 3, 3, "#000"),
    ('4', 4, 0, "#3C3636"), ('5', 4, 1, "#3C3636"), ('6', 4, 2, "#3C3636"), ('*', 4, 3, "#000"),
    ('1', 5, 0, "#3C3636"), ('2', 5, 1, "#3C3636"), ('3', 5, 2, "#3C3636"), ('-', 5, 3, "#000"),
    ('0', 6, 0, "#3C3636"), ('.', 6, 1, "#3C3636"), ('=', 6, 2, "#db701f"), ('+', 6, 3, "#000")
]

# Create buttons
for (text, row, col, color) in buttons:
    btn = ctk.CTkButton(root, text=text, width=60, height=50, font=("Arial", 22, "bold"), fg_color=color, text_color="white",
                        command=lambda t=text: on_button_click(t))
    btn.grid(row=row, column=col, padx=3, pady=3)

# Run the application
root.mainloop()
