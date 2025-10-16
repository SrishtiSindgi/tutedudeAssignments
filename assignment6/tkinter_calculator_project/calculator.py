import tkinter as tk

# Global variables to manage calculator state
display_var = None
first_num = None
operator = None

def button_click(number):
    """Appends the clicked number/operator to the display."""
    current = display_var.get()
    # Prevent multiple decimal points in one number
    if number == '.' and '.' in current:
        return
    display_var.set(current + str(number))

def button_clear():
    """Clears the calculator display and resets state."""
    display_var.set("")
    global first_num, operator
    first_num = None
    operator = None

def button_operation(op):
    """Handles operator (+, -, *, /) button clicks."""
    global first_num, operator
    try:
        # If display empty and user presses operator, do nothing
        current = display_var.get()
        if current == "":
            return
        first_num = float(current)  # Convert current display to float
        operator = op               # Store the operator
        display_var.set("")         # Clear display for the next number
    except ValueError:
        display_var.set("Error")
        first_num = None
        operator = None

def button_equals():
    """Performs the calculation when '=' is pressed."""
    global first_num, operator
    try:
        if display_var.get() == "":
            # If equals pressed with empty second operand, do nothing or show first
            if first_num is not None and operator is None:
                display_var.set(str(first_num))
            return

        second_num = float(display_var.get())  # Get the second number
        display_var.set("")  # Clear display for result

        if first_num is not None and operator is not None:
            result = 0
            if operator == '+':
                result = first_num + second_num
            elif operator == '-':
                result = first_num - second_num
            elif operator == '*':
                result = first_num * second_num
            elif operator == '/':
                if second_num == 0:
                    display_var.set("Error: Div by zero")
                    # Reset state
                    first_num = None
                    operator = None
                    return
                result = first_num / second_num

            # Display result: if integer-like, show without trailing .0
            if result == int(result):
                display_var.set(str(int(result)))
            else:
                display_var.set(str(result))

            # Reset for next calculation
            first_num = None
            operator = None
        else:
            # If '=' pressed without valid prior operation, just display the number entered
            display_var.set(str(second_num))

    except ValueError:
        display_var.set("Error")
    except Exception as e:
        display_var.set(f"Error: {e}")
    finally:
        # Ensure state is reset
        first_num = None
        operator = None

def create_calculator_gui():
    root = tk.Tk()
    root.title("TuteDude Python Calculator (Final)")
    root.geometry("320x450")  # Slightly larger for padding

    # Configure rows and columns to be responsive
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)
    for i in range(1, 6):
        root.grid_rowconfigure(i, weight=1)

    # Create the StringVar and link it to the Entry widget
    global display_var
    display_var = tk.StringVar()
    e = tk.Entry(root, width=35, borderwidth=5, font=('Arial', 20),
                 justify='right', textvariable=display_var)
    e.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    # --- Define Buttons and place them dynamically ---
    buttons_data = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3, 'operator'),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3, 'operator'),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3, 'operator'),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2, 'operator_long'),  # '+' spans 2 columns
        ('C', 5, 0, 'clear'), ('=', 5, 1, 'equals')  # '=' spans 3 columns
    ]

    button_font = ('Arial', 16)

    for item_data in buttons_data:
        button_text = item_data[0]
        r = item_data[1]
        c = item_data[2]
        button_type = item_data[3] if len(item_data) > 3 else 'number'  # Default to 'number'

        btn = None
        command_func = None
        column_span = 1

        if button_type == 'clear':
            command_func = button_clear
        elif button_type == 'equals':
            command_func = button_equals
            column_span = 3  # '=' spans 3 columns
        elif button_type == 'operator':
            command_func = lambda op=button_text: button_operation(op)
        elif button_type == 'operator_long':  # For '+'
            command_func = lambda op=button_text: button_operation(op)
            column_span = 2  # '+' spans 2 columns
        else:  # It's a number or decimal point
            command_func = lambda num=button_text: button_click(num)

        btn = tk.Button(root, text=button_text, font=button_font, padx=10, pady=10,
                        command=command_func)
        btn.grid(row=r, column=c, columnspan=column_span, padx=5, pady=5, sticky="nsew")

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    create_calculator_gui()
