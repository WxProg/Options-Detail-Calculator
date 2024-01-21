# Optionated

## Overview

The Options Details Calculator is a GUI-based tool designed to assist users in understanding the intrinsic value and potential profitability of standard option contracts. While this tool offers a simplistic view into the world of options trading, it provides a foundational understanding for novices and those looking to quickly gauge option profitability.

Please note, this tool currently operates as a Minimum Viable Product (MVP). It offers a streamlined set of features with the aim of expanding based on user feedback and further iterations.

![optionated1](https://github.com/WxProg/Options-Detail-Calculator/assets/101136336/228bf434-f146-4e78-befa-70b84b1c1cbc)

## Features

- Input fields for:
  - Current Stock Price
  - Target Stock Price at Expiration
  - Option Strike Price
  - Option Premium (Per Share)
- Results display:
  - Option status (In-the-Money, At-the-Money, Out-of-the-Money)
  - Current intrinsic value
  - Projected profit based on target stock price
  - Projected percentage return
  - Net profit after accounting for premium paid

## Disclaimer

The Options Details Calculator offers a simplified view of options trading. Real-world options trading involves various complex factors such as implied volatility, time decay, interest rates, dividends, and more, which this tool does not currently account for. This tool is meant for educational purposes and should not be the sole determinant for any trading decisions.

Always consult with a financial advisor or conduct comprehensive research before making investment decisions.

## Future Roadmap

- Incorporate real-time stock data to automatically populate current stock price.
- Factor in time decay (Theta) for options nearing expiration.
- Consider implied volatility in option pricing.
- Integrate popular options valuation models like Black-Scholes.
- Introduce analytics for American options concerning early exercise considerations.

## Technologies Used
Python: The main programming language used to develop the application logic.
Tkinter: A standard GUI library in Python, used to create the user interface for the application.

## Installation & Usage

1. Ensure you have Python and `tkinter` installed.
2. Clone this repository.
3. Navigate to the directory and run `python calculator.py` (or appropriate filename).
4. Enter the relevant stock and option details and click on "Calculate" to get results.

## Contribution

Feedback and pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
