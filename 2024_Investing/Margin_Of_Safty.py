import matplotlib.pyplot as plt


def margin_of_safety(intrinsic_value, market_price):
    if intrinsic_value <= 0:
        return "Intrinsic value must be greater than 0."
    margin = (intrinsic_value - market_price) / intrinsic_value * 100
    return margin

# Example values
intrinsic_value = 100  # You can replace this with any value
market_price = 70      # You can replace this with any value

# Calculate the margin of safety
mos = margin_of_safety(intrinsic_value, market_price)

# Visualization


def visualize_margin_of_safety(intrinsic_value, market_price, margin_of_safety):
    fig, ax = plt.subplots(figsize=(8, 6))

    # Bar for intrinsic value
    ax.barh('Intrinsic Value', intrinsic_value, color='green', label='Intrinsic Value')

    # Bar for market price
    ax.barh('Market Price', market_price, color='blue', label='Market Price')

    # Bar for margin of safety
    ax.barh('Margin of Safety', intrinsic_value - market_price, left=market_price, color='orange', label=f'Margin of Safety ({margin_of_safety:.2f}%)')

    # Labels and title
    ax.set_xlabel('Value ($)')
    ax.set_title('Margin of Safety Visualization')
    ax.legend()

    # Show plot
    plt.show()

# Visualize the margin of safety
visualize_margin_of_safety(intrinsic_value, market_price, mos)

