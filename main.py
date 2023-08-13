from tkinter import *
from tkinter import ttk, messagebox

# Constants
GENERAL_FONT = ("Segoe UI", 14)
ENTRY_WIDTH = 15

def create_label(window, text, row):
    label = Label(window, text=text, font=GENERAL_FONT)
    label.grid(row=row, column=0, sticky=W, padx=8, pady=6)

    return label
def create_entry(window, var, row):
    entry = Entry(window, width=ENTRY_WIDTH, textvariable=var)
    entry.grid(row=row, column=1)

    return entry
def calculate_option_details():
    try:
        # Get the values from GUI entry fields and convert them to floats
        current_price = float(current_stock_price_var.get())
        target_price = float(target_price_var.get())
        strike_price = float(strike_price_var.get())
        premium_per_share = float(premium_per_share_var.get())
        premium_paid = premium_per_share * 100 # Convert per-share premium to total premium for 100 shares

        # Determine the intrinsic value and current option status
        tolerance = 0.05  # Define tolerance level for at-the-money options

        if abs(current_price - strike_price) <= tolerance:
            option_status = "At-the-Money (ATM)"
            intrinsic_value = 0
        elif current_price > strike_price:
            option_status = "In-the-Money (ITM)"
            intrinsic_value = current_price - strike_price
        else:
            option_status = "Out-of-the-Money (OTM)"
            intrinsic_value = 0


        if premium_per_share == 0:
            messagebox.showwarning(title="Input Warning", message="Premium paid, cannot be zero.")
            return

        # Intrinsic value is the amount by which an option is in-the-money.
        #  For a call option, it is cal. as the difference between the stock price and the strike price
        #  only when the stock price is above the strike price
        future_intrinsic_value = max(target_price - strike_price, 0)  *100

        # Compute future profitability of the option & net profit.
        profit = (future_intrinsic_value - premium_paid)
        net_profit = profit - premium_paid

        #Determine the percentage return
        percentage_return = (profit/premium_paid) * 100

        # Display results on GUI
        option_status_var.set(f"Option Status: {option_status}")
        intrinsic_value_var.set(f"Current Intrinsic Value: ${intrinsic_value: .2f}")
        profit_result_var.set(f"Projected Profit is: ${profit:.2f}")
        percentage_return_var.set(f"Projected % Return is: {round(percentage_return)}%")
        net_profit_var.set(f"Net Profit: ${net_profit}")

    except ValueError:
        messagebox.showwarning(title="Error", message="Please enter valid numbers.")
        return
# Setup main window
window = Tk()
window.title("Options Details Calculator")
window.minsize(width=400, height=300)
window.config(padx=10)
# window.configure(bg='black')
Label(window, text= "Option Status & Future Profitability Calculator" ,
      font=("Algerian", 20, "bold", "underline")).grid(row=0, column=0, columnspan=2,  pady=10)

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
create_label(window, "Current Stock Price:", 1)
create_entry(window, current_stock_price_var, 1).focus()

create_label(window, "Target Stock Price at Expiration:", 2)
create_entry(window, target_price_var, 2)

create_label(window, "Option Strike Price:", 3)
create_entry(window, strike_price_var, 3)

create_label(window, "Option Premium (Per Share):",4)
create_entry(window, premium_per_share_var, 4)

# Results are based on a standard option contract representing 100 shares
info_100shares_label = Label(window,
                             text="Note: Results are based on standard option contracts representing 100 shares.",
                             font=GENERAL_FONT, wraplength=350)
info_100shares_label.grid(row=5, column=0, columnspan=2, pady=5)
# Add button to trigger calculation
button = Button(window, text="Calculate", command=calculate_option_details)
button.grid(row=6, column=0, columnspan=2, pady=8)

# To display the profit results, percentage return, net profit and instrinsic value on GUI main window
profit_result_label = Label(window, textvariable=profit_result_var, font=GENERAL_FONT)
profit_result_label.grid(row=7, column=0, columnspan=2, pady=8)

percentage_return_label = Label(window, textvariable=percentage_return_var, font=GENERAL_FONT)
percentage_return_label.grid(row=8, column=0, columnspan=2, pady=8)

option_status_label = Label(window, textvariable=option_status_var, font=GENERAL_FONT)
option_status_label.grid(row=9, column=0, columnspan = 2, pady=8)

intrinsic_value_label = Label(window, textvariable=intrinsic_value_var, font=GENERAL_FONT)
intrinsic_value_label.grid(row=10, column=0, columnspan=2,pady=8)

net_profit_label = Label(window, textvariable=net_profit_var, font=GENERAL_FONT)
net_profit_label.grid(row=11, column=0, columnspan=2, pady=8)

window.mainloop()