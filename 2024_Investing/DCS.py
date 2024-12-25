import numpy as np
import matplotlib.pyplot as plt


def calculate_dcf(free_cash_flows, wacc, terminal_growth_rate, terminal_year):
    # Discount factor for each year

    discount_factors = [
            (1 / (1 + wacc) ** year) for year in
            range(1, len(free_cash_flows) + 1)]

    # Present value of free cash flows
    discounted_fcfs = [fcf * df for fcf, df in zip(free_cash_flows, discount_factors)]
    # Terminal value calculation
    terminal_value = free_cash_flows[-1] * (1 + terminal_growth_rate) / (wacc - terminal_growth_rate)
    # Present value of terminal value
    terminal_value_discounted = terminal_value / (1 + wacc) ** terminal_year
    # Enterprise value
    enterprise_value = sum(discounted_fcfs) + terminal_value_discounted
    return discounted_fcfs, terminal_value_discounted, enterprise_value

# Example inputs


free_cash_flows = [100, 120, 140, 160, 180]  # Forecasted free cash flows for 5 years
wacc = 0.10  # Discount rate (10%)
terminal_growth_rate = 0.02  # Terminal growth rate (2%)
terminal_year = len(free_cash_flows)

# Calculate DCF
discounted_fcfs, terminal_value_discounted, enterprise_value = calculate_dcf(
    free_cash_flows, wacc, terminal_growth_rate, terminal_year
)

# Visualization


def visualize_dcf(free_cash_flows,
                  discounted_fcfs,
                  terminal_value_discounted,
                  enterprise_value):
    years = list(range(1, len(free_cash_flows) + 1))
    fig, ax = plt.subplots(figsize=(10, 6))
    # Plotting free cash flows and discounted cash flows
    ax.plot(years, free_cash_flows, marker='o', linestyle='-', color='blue',
            label='Free Cash Flows')
    ax.plot(years, discounted_fcfs, marker='o', linestyle='--', color='orange',
            label='Discounted Cash Flows')
    # Adding terminal value to the last year
    ax.bar([terminal_year + 1], [terminal_value_discounted],
           color='green', label=f'Terminal Value (Discounted)')

    # Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Value ($)')
    ax.set_title('Discounted Cash Flow (DCF) Analysis')
    ax.legend()
    # Display enterprise value
    ax.text(0.5, 0.9, f'Enterprise Value: ${enterprise_value:.2f}',
            transform=ax.transAxes, fontsize=12, color='black')

    plt.grid(True)
    plt.show()

# Visualize DCF Analysis


visualize_dcf(free_cash_flows,
              discounted_fcfs,
              terminal_value_discounted,
              enterprise_value)
