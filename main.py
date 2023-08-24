from tkinter import *
from tkinter import ttk, messagebox

# Constants
PRIMARY_FONT = ("Segoe UI", 14)
HEADING_FONT = ("Algerian", 20, "underline")
RESULT_FONT = ("Segeo UI", 14, "bold")
ENTRY_WIDTH = 15

# Dark theme colors
BACKGROUND_COLOR = '#2E2E2E'
FOREGROUND_COLOR = '#FFFFFF'
BUTTON_COLOR = "#4E4E4E"
BUTTON_HOVER_COLOR = '#5E5E5E'
ENTRY_BG = '#3E3E3E'
FRAME_BG = '#2E2E2E'

# Color contrast for the exit button
EXIT_BUTTON_COLOR = '#D32F2F'
EXIT_BUTTON_HOVER_COLOR = '#C62828'


# Function to terminate the GUI
def close_app():
    window.destroy()


def reset_fields():
    """Reset all entry fields and result variables."""
    current_stock_price_var.set("")
    target_price_var.set("")
    strike_price_var.set("")
    premium_per_share_var.set("")
    option_status_var.set("")
    intrinsic_value_var.set("")
    profit_result_var.set("")
    percentage_return_var.set("")
    net_profit_var.set("")
    option_combobox.set("Make a selection")


def create_label(window_to_use, text, row):
    label = ttk.Label(window_to_use, text=text, font=PRIMARY_FONT)
    label.grid(row=row, column=0, sticky=W + E, padx=8, pady=6)

    return label


def create_entry(window_to_use, var, row):
    entry = ttk.Entry(window_to_use, width=ENTRY_WIDTH, textvariable=var)
    entry.grid(row=row, column=1, sticky=E)

    return entry


def calculate_option_details():
    global future_intrinsic_value, option_status, intrinsic_value
    try:
        option_type = option_combobox.get().strip()

        if option_type not in ['Call', 'Put']:
            messagebox.showwarning(title="Input Warning",
                                   message="Invalid option type selected. Please choose either 'Call' or 'Put'.")
            return

        # Get the values from GUI entry fields and convert them to floats
        current_price = float(current_stock_price_var.get())
        target_price = float(target_price_var.get())
        strike_price = float(strike_price_var.get())
        premium_per_share = float(premium_per_share_var.get())
        premium_paid = premium_per_share * 100  # Convert per-share premium to total premium for 100 shares

        tolerance = 0.05  # Define tolerance level for at-the-money options

        # Based on option type selection. Determine the intrinsic value and current option status
        if option_type == 'Call':
            intrinsic_value = max(current_price - strike_price, 0)

            if abs(current_price - strike_price) <= tolerance:
                option_status = "At-the-Money (ATM)"
            elif current_price > strike_price:
                option_status = "In-the-Money (ITM)"
            else:
                option_status = "Out-of-the-Money (OTM)"

            # Intrinsic value is the amount by which an option is in-the-money.
            #  For a call option, it is cal. as the difference between the stock price and the strike price
            #  only when the stock price is above the strike price
            future_intrinsic_value = max(target_price - strike_price, 0) * 100

        elif option_type == 'Put':
            intrinsic_value = max(strike_price - current_price, 0)

            if abs(current_price - strike_price) <= tolerance:
                option_status = "At-the-Money (ATM)"
            elif current_price < strike_price:
                option_status = "In-the-Money (ITM)"
            else:
                option_status = "Out-of-the-Money (OTM)"

            future_intrinsic_value = max(strike_price - target_price, 0) * 100

        if premium_per_share == 0:
            messagebox.showwarning(title="Input Warning", message="Premium paid, cannot be zero.")
            return

        # Compute future profitability of the option & net profit.
        profit = (future_intrinsic_value - premium_paid)

        # Determine the percentage return
        percentage_return = (profit / premium_paid) * 100

        # Display results on GUI
        option_status_var.set(f"Option Status: {option_status}")
        intrinsic_value_var.set(f"Current Intrinsic Value: ${intrinsic_value: .2f}")
        profit_result_var.set(f"Projected Profit is: ${profit:.2f}")
        percentage_return_var.set(f"Projected % Return is: {round(percentage_return)}%")
        net_profit_var.set(f"Net Profit: ${profit}")

    except ValueError:
        messagebox.showwarning(title="Error", message="Please enter valid numbers.")
        return


# Setup main window
window = Tk()
window.title("Options Details Calculator")
window.minsize(width=400, height=400)
window.resizable(False, False)
window.config(bg=BACKGROUND_COLOR, padx=10, pady=10)

# Main heading
Label(window, text="Option Status & Future Profitability Calculator",
      font=HEADING_FONT, bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR).grid(row=0, column=0, columnspan=2, pady=10)

# Variables for storing inputs
current_stock_price_var = StringVar()
target_price_var = StringVar()
strike_price_var = StringVar()
premium_per_share_var = StringVar()
option_status_var = StringVar()
intrinsic_value_var = StringVar()
profit_result_var = StringVar()
percentage_return_var = StringVar()
net_profit_var = StringVar()

# ------------------------- CREATE GUI COMPONENTS, LABELS & BUTTONS --------------------------------------

# Input frame
input_frame = ttk.LabelFrame(window, text="Input Fields", padding=(10, 5))
input_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
input_frame.grid_columnconfigure(1, weight=1)

# Add all the labels and inputs to the input frame
create_label(input_frame, "Current Stock Price:", 0)
create_entry(input_frame, current_stock_price_var, 0).focus()

create_label(input_frame, "Target Stock Price at Expiration:", 1)
create_entry(input_frame, target_price_var, 1)

create_label(input_frame, "Option Strike Price:", 2)
create_entry(input_frame, strike_price_var, 2)

create_label(input_frame, "Option Premium (Per Share):", 3)
create_entry(input_frame, premium_per_share_var, 3)

# To display the profit results, percentage return, net profit and intrinsic value on GUI main window
# Results frame
results_frame = ttk.LabelFrame(window, text="Results", padding=(10, 5))
results_frame.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
results_frame.grid_columnconfigure(1, weight=1)

# Add results to the results frame
profit_result_label = Label(results_frame, textvariable=profit_result_var, font=RESULT_FONT)
profit_result_label.grid(row=0, column=0, columnspan=2, pady=8, sticky=W + E)
profit_result_label.config(bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR)

percentage_return_label = Label(results_frame, textvariable=percentage_return_var, font=RESULT_FONT)
percentage_return_label.grid(row=1, column=0, columnspan=2, pady=8, sticky=W + E)
percentage_return_label.config(bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR)

option_status_label = Label(results_frame, textvariable=option_status_var, font=RESULT_FONT)
option_status_label.grid(row=2, column=0, columnspan=2, pady=8, sticky=W + E)
option_status_label.config(bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR)

intrinsic_value_label = Label(results_frame, textvariable=intrinsic_value_var, font=RESULT_FONT)
intrinsic_value_label.grid(row=3, column=0, columnspan=2, pady=8, sticky=W + E)
intrinsic_value_label.config(bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR)

net_profit_label = Label(results_frame, textvariable=net_profit_var, font=RESULT_FONT)
net_profit_label.grid(row=4, column=0, columnspan=2, pady=8, sticky=W + E)
net_profit_label.config(bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR)

# Results are based on a standard option contract representing 100 shares
info_100shares_label = Label(input_frame,
                             text="Note: Results are based on standard option contracts representing 100 shares.",
                             font=PRIMARY_FONT, wraplength=350)
info_100shares_label.grid(row=4, column=0, columnspan=2, pady=5)
info_100shares_label.config(bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR)

# Button used to trigger calculation
button = ttk.Button(window, text="Calculate", command=calculate_option_details, style='TButton')
button.grid(row=3, column=0, pady=8, padx=(0, 5), sticky=E)

# Button used to reset all entry fields
reset_button = ttk.Button(window, text="Reset", command=reset_fields, style='TButton')
reset_button.grid(row=3, column=1, pady=8, padx=(5, 0), sticky=W)

# Button used to close / terminate app
exit_button = ttk.Button(window, text="Exit", command=close_app, style='Exit.TButton')
exit_button.grid(row=1, column=1, sticky=E, padx=6)

# Combobox Button for call or put option
options = ['Call', 'Put']
option_combobox = ttk.Combobox(window, values=options, state="readonly")
option_combobox.grid(row=1, column=0, sticky=W, padx=(0, 6))
option_combobox.set("Make a selection")

# ------------------------------ STYLING OBJECTS ---------------------------------
style = ttk.Style()
style.configure('.', background=FRAME_BG, foreground=FOREGROUND_COLOR)

# Button styling
style.theme_use('clam')
style.configure('TButton', background=BUTTON_COLOR, foreground=FOREGROUND_COLOR, bordercolor=BUTTON_COLOR)
style.map('TButton',
          background=[('active', BUTTON_HOVER_COLOR)],
          foreground=[('active', FOREGROUND_COLOR)])
# Exit Button styling
style.configure('Exit.TButton', background=EXIT_BUTTON_COLOR, foreground=FOREGROUND_COLOR,
                bordercolor=EXIT_BUTTON_COLOR)
style.map('Exit.TButton',
          background=[('active', EXIT_BUTTON_HOVER_COLOR)],
          foreground=[('active', FOREGROUND_COLOR)])

# Combobox styling
style.configure('TCombobox', fieldbackground=BUTTON_COLOR, foreground=FOREGROUND_COLOR, background=FRAME_BG,
                selectbackground=BUTTON_HOVER_COLOR)
style.map('TCombobox',
          fieldbackground=[('readonly', BUTTON_COLOR), ('readonly focus', BUTTON_HOVER_COLOR)],
          selectbackground=[('readonly', BUTTON_COLOR), ('readonly focus', BUTTON_HOVER_COLOR)],
          selectforeground=[('readonly', FOREGROUND_COLOR)],
          background=[('readonly', BUTTON_COLOR), ('readonly focus', BUTTON_HOVER_COLOR)]
          )

# Label styling
style.configure('TLabelframe', background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
style.configure('TLabelframe.Label', background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)
style.configure('TLabel', background=FRAME_BG, foreground=FOREGROUND_COLOR)

# Entry styling
style.configure('TEntry', fieldbackground=ENTRY_BG, foreground=FOREGROUND_COLOR, background=FRAME_BG)

window.mainloop()
