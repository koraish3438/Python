# import modules
from tkinter import *
import math

# Functions
# Function to add in the entry of text display
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

# Function to clear in the entry of text display
def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

# Function to delete one by one from the last in the entry of text display
def button_delete():
    global calc_operator
    calc_operator = calc_operator[:-1]
    text_input.set(calc_operator)

# Function to calculate the factorial of a number
def button_factorial():
    global calc_operator
    try:
        value = int(eval(calc_operator))  # Evaluate the expression and convert it to an integer
        if value < 0:
            text_input.set("Error")  # Show "Error" if the number is negative
            calc_operator = ""
        else:
            calc_operator = str(math.factorial(value))  # Calculate factorial
            text_input.set(calc_operator)
    except:
        text_input.set("Error")  # Show "Error" if input is invalid
        calc_operator = ""

# Function to calculate trigonometric values (sin, cos, tan) of an angle
# Function to calculate sine of an angle
def trig_sin():
    global calc_operator
    try:
        angle = float(calc_operator)  # Convert input to float
        result = str(math.sin(math.radians(angle)))  # Calculate sine
        calc_operator = result
        text_input.set(result)
    except ValueError:
        text_input.set("Error")  # Handle invalid input

# Function to calculate cosine of an angle
def trig_cos():
    global calc_operator
    try:
        angle = float(calc_operator)  # Convert input to float
        result = str(math.cos(math.radians(angle)))  # Calculate cosine
        calc_operator = result
        text_input.set(result)
    except ValueError:
        text_input.set("Error")  # Handle invalid input

# Function to calculate tangent of an angle
def trig_tan():
    global calc_operator
    try:
        angle = float(calc_operator)  # Convert input to float
        result = str(math.tan(math.radians(angle)))  # Calculate tangent
        calc_operator = result
        text_input.set(result)
    except ValueError:
        text_input.set("Error")  # Handle invalid input


# Function to find the square root of a number
def square_root():
    global calc_operator
    try:
        number = float(calc_operator)
        if number >= 0:
            temp = str(number ** 0.5)  # Using **0.5 for square root
            calc_operator = temp
        else:
            temp = "ERROR"
    except ValueError:
        temp = "ERROR"
    
    text_input.set(temp)
    
def cube_root():
    global calc_operator
    try:
        number = float(calc_operator)
        temp = str(number ** (1/3))  # Using **(1/3) for cube root
        calc_operator = temp
    except ValueError:
        temp = "ERROR"
    
    text_input.set(temp)


# Function to calculate the percentage of a number
def percentage():
    global calc_operator
    try:
        number = float(calc_operator)
        temp = str(number / 100)  # Calculate percentage
        calc_operator = temp
    except (ValueError, ZeroDivisionError):
        temp = "ERROR"  # Handle invalid input
        calc_operator = temp

    text_input.set(calc_operator)

# Function to find the result of an operator
def button_equal():
    global calc_operator
    try:
        temp_op = str(eval(calc_operator))
        calc_operator = temp_op
        text_input.set(calc_operator)
    except Exception as e:
        text_input.set("Error")  # Show "Error" if evaluation fails
        calc_operator = ""

# Create main window
tk_calc = Tk()
tk_calc.configure(bg="#293C4A", bd=10)
tk_calc.title("Scientific Calculator")

calc_operator = ""
text_input = StringVar()

text_display = Entry(tk_calc, font=("sans-serif", 20, "bold"), textvariable=text_input, bd=5, insertwidth=5, bg="#BBB", justify="right").grid(columnspan=5, padx=10, pady=15)

button_params = {'bd': 5, 'fg': '#BBB', 'bg': '#3C3636', 'font': ('sans-serif', 20, 'bold')}
button_params_main = {'bd': 5, 'fg': '#000', 'bg': '#BBB', 'font': ('sans-serif', 20, 'bold')}

# Buttons
# 1st row
Button(tk_calc, bd=5, bg='#db701f', fg='#000', font=('sans-serif', 20, 'bold'), text='AC', command=button_clear_all).grid(row=1, column=0, sticky="nsew")
Button(tk_calc, button_params, text='sin', command=trig_sin).grid(row=1, column=1, sticky="nsew")
Button(tk_calc, button_params, text='cos', command=trig_cos).grid(row=1, column=2, sticky="nsew")
Button(tk_calc, button_params, text='tan', command=trig_tan).grid(row=1, column=3, sticky="nsew")
Button(tk_calc, bd=5, bg='#db701f', fg='#000', font=('sans-serif', 20, 'bold'), text='DEL', command=button_delete).grid(row=1, column=4, sticky="nsew")

# 2nd row
Button(tk_calc, button_params, text='x²', command=lambda: button_click('**2')).grid(row=2, column=0, sticky="nsew")
Button(tk_calc, button_params, text='x^n', command=lambda: button_click('**')).grid(row=2, column=1, sticky="nsew")
Button(tk_calc, button_params, text='log₁₀', command=lambda: button_click('log(')).grid(row=2, column=2, sticky="nsew")
Button(tk_calc, button_params, text='%', command=percentage).grid(row=2, column=3, sticky="nsew")
Button(tk_calc, button_params, text='/', command=lambda: button_click('/')).grid(row=2, column=4, sticky="nsew")
Button(tk_calc, button_params, text='(', command=lambda: button_click('(')).grid(row=3, column=2, sticky="nsew")
Button(tk_calc, button_params, text=')', command=lambda: button_click(')')).grid(row=3, column=3, sticky="nsew")
Button(tk_calc, button_params, text='\u00B3\u221A', command=square_root).grid(row=3, column=0, sticky="nsew")
Button(tk_calc, button_params, text='\u221A', command=cube_root).grid(row=3, column=1, sticky="nsew")




# Add additional buttons for multiplication, subtraction, addition, and digits
Button(tk_calc, button_params, text='*', command=lambda: button_click('*')).grid(row=3, column=4, sticky="nsew")
Button(tk_calc, button_params, text='-', command=lambda: button_click('-')).grid(row=4, column=4, sticky="nsew")
Button(tk_calc, button_params, text='+', command=lambda: button_click('+')).grid(row=5, column=4, sticky="nsew")
Button(tk_calc, button_params, text='=', command=button_equal).grid(row=6, column=4, sticky="nsew")

# Digit buttons
Button(tk_calc, button_params, text='1', command=lambda: button_click('1')).grid(row=6, column=0, sticky="nsew")
Button(tk_calc, button_params, text='2', command=lambda: button_click('2')).grid(row=6, column=1, sticky="nsew")
Button(tk_calc, button_params, text='3', command=lambda: button_click('3')).grid(row=6, column=2, sticky="nsew")
Button(tk_calc, button_params, text='4', command=lambda: button_click('4')).grid(row=5, column=0, sticky="nsew")
Button(tk_calc, button_params, text='5', command=lambda: button_click('5')).grid(row=5, column=1, sticky="nsew")
Button(tk_calc, button_params, text='6', command=lambda: button_click('6')).grid(row=5, column=2, sticky="nsew")
Button(tk_calc, button_params, text='7', command=lambda: button_click('7')).grid(row=4, column=0, sticky="nsew")
Button(tk_calc, button_params, text='8', command=lambda: button_click('8')).grid(row=4, column=1, sticky="nsew")
Button(tk_calc, button_params, text='9', command=lambda: button_click('9')).grid(row=4, column=2, sticky="nsew")
Button(tk_calc, button_params, text='0', command=lambda: button_click('0')).grid(row=4, column=3, sticky="nsew")
Button(tk_calc, button_params, text='00', command=lambda: button_click('00')).grid(row=5, column=3, sticky="nsew")
Button(tk_calc, button_params, text='.', command=lambda: button_click('.')).grid(row=6, column=3, sticky="nsew")

tk_calc.mainloop()
