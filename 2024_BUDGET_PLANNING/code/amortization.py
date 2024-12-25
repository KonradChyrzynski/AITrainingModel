import matplotlib.pyplot as plt


def calculate_depreciation(initial_value, annual_depreciation_rate, years):
    value = initial_value
    depreciation_values = [value]
    for year in range(1, years + 1):
        value -= value * annual_depreciation_rate
        depreciation_values.append(value)
    return depreciation_values


def plot_car_costs(initial_value_new,
                   initial_value_used,
                   annual_depreciation_rate_new,
                   annual_depreciation_rate_used, years):
    # Obliczanie wartości samochodów w czasie
    depreciation_new = calculate_depreciation(initial_value_new, annual_depreciation_rate_new, years)
    depreciation_used = calculate_depreciation(initial_value_used, annual_depreciation_rate_used, years)

    # Całkowity koszt samochodu
    total_cost_new = [initial_value_new - value for value in depreciation_new]
    total_cost_used = [initial_value_used - value for value in depreciation_used]
    # Wizualizacja danych
    plt.figure(figsize=(10, 6))
    # Wartości samochodów
    plt.plot(range(years + 1), depreciation_new, label='Wartość nowego samochodu', color='blue', marker='o')
    plt.plot(range(years + 1), depreciation_used, label='Wartość używanego samochodu', color='green', marker='o')
    # Całkowite koszty samochodów
    plt.plot(range(years + 1), total_cost_new, label='Całkowity koszt nowego samochodu', color='purple', linestyle='--')
    plt.plot(range(years + 1), total_cost_used, label='Całkowity koszt używanego samochodu', color='orange', linestyle='--')
    plt.title('Amortyzacja samochodów nowych i używanych')
    plt.xlabel('Lata')
    plt.ylabel('Wartość samochodu / Koszt [PLN]')
    plt.legend()
    plt.grid(True)
    plt.show()

# Parametry początkowe
initial_value_new = 180000  # Początkowa wartość nowego samochodu w PLN
initial_value_used = 100000  # Początkowa wartość używanego samochodu w PLN
annual_depreciation_rate_new = 0.2  # Roczny spadek wartości dla nowego samochodu (15%)
annual_depreciation_rate_used = 0.1  # Roczny spadek wartości dla używanego samochodu (10%)
years = 10  # Okres użytkowania w latach

# Wywołanie funkcji
plot_car_costs(initial_value_new, initial_value_used, annual_depreciation_rate_new, annual_depreciation_rate_used, years)


