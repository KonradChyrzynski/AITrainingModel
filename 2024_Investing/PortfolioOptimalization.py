import numpy as np
from scipy.optimize import minimize

# Przykładowe dane: zwroty i macierz kowariancji
expected_returns = np.array([0.12, 0.18, 0.15])  # oczekiwane zwroty z inwestycji

cov_matrix = np.array([
    [0.005, -0.010, 0.004],
    [-0.010, 0.040, -0.002],
    [0.004, -0.002, 0.023]
])  # macierz kowariancji

# Funkcja celu do minimalizacji (zamiast maksymalizacji)


def portfolio_variance(weights, cov_matrix):
    return np.dot(weights.T, np.dot(cov_matrix, weights))

# Ograniczenia (całość inwestycji = 1)


constraints = ({
    'type': 'eq',
    'fun': lambda weights: np.sum(weights) - 1
})

# Ograniczenia dla wag (każda waga musi być między 0 a 1)
bounds = tuple((0, 1) for _ in range(len(expected_returns)))

# Początkowe wartości wag (równe rozłożenie na wszystkie aktywa)
initial_weights = np.array([1./len(expected_returns) for _ in range(len(expected_returns))])

# Optymalizacja portfela
optimal_solution = minimize(portfolio_variance, initial_weights,
                            args=(cov_matrix,), method='SLSQP',
                            bounds=bounds, constraints=constraints)

# Wynik
if optimal_solution.success:
    optimal_weights = optimal_solution.x
    expected_portfolio_return = np.dot(optimal_weights, expected_returns)
    portfolio_risk = np.sqrt(portfolio_variance(optimal_weights, cov_matrix))
    
    print("Optymalne wagi portfela (proporcje inwestycji):")
    for i, weight in enumerate(optimal_weights):
        print(f"Aktywo {i+1}: {weight:.2%}")
    
    print(f"\nOczekiwany zwrot portfela: {expected_portfolio_return:.2%}")
    print(f"Ryzyko portfela (odchylenie standardowe): {portfolio_risk:.2%}")
else:
    print("Nie udało się znaleźć optymalnego rozwiązania.")

