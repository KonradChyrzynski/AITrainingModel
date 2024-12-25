import matplotlib.pyplot as plt

def linear_depreciation(initial_value, annual_depreciation_rate, years):
    monthly_depreciation = (initial_value * annual_depreciation_rate) / 12
    depreciation_values = []
    value = initial_value
    
    for month in range(1, years * 12 + 1):
        value -= monthly_depreciation
        depreciation_values.append(value)
    
    return depreciation_values, monthly_depreciation

def plot_linear_depreciation(initial_value, annual_depreciation_rate, years):
    # Obliczanie wartości samochodu w czasie
    depreciation_values, monthly_depreciation = linear_depreciation(initial_value, annual_depreciation_rate, years)
    
    # Tworzenie osi czasu w miesiącach
    months = list(range(1, years * 12 + 1))
    
    # Tworzenie wykresów
    plt.figure(figsize=(14, 6))
    
    # Wykres wartości samochodu
    plt.subplot(1, 2, 1)
    plt.plot(months, depreciation_values, label='Wartość samochodu', color='blue', marker='o')
    plt.title('Wartość samochodu w czasie')
    plt.xlabel('Miesiące')
    plt.ylabel('Wartość samochodu [PLN]')
    plt.legend()
    plt.grid(True)
    
    # Wykres miesięcznej stawki amortyzacji
    plt.subplot(1, 2, 2)
    plt.plot(months, [monthly_depreciation] * len(months), label='Miesięczna stawka amortyzacji', color='red', linestyle='--')
    plt.title('Miesięczna stawka amortyzacji')
    plt.xlabel('Miesiące')
    plt.ylabel('Kwota amortyzacji [PLN]')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# Parametry początkowe
initial_value = 50000  # Początkowa wartość samochodu w PLN
annual_depreciation_rate = 0.20  # Roczna stawka amortyzacji (20%)
years = 5  # Okres amortyzacji w latach

# Wywołanie funkcji
plot_linear_depreciation(initial_value, annual_depreciation_rate, years)

