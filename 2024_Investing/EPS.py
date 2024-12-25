import matplotlib.pyplot as plt

def oblicz_eps(zysk_netto, liczba_akcji):
    """
    Funkcja oblicza EPS (Earnings Per Share).
    
    :param zysk_netto: Zysk netto firmy.
    :param liczba_akcji: Liczba akcji firmy.
    :return: EPS (Earnings Per Share).
    """
    if liczba_akcji == 0:
        raise ValueError("Liczba akcji nie może być zerowa.")
    return zysk_netto / liczba_akcji

# Przykładowe dane


lata = ['2020', '2021', '2022', '2023', '2024']
zyski_netto = [500000, 600000, 700000, 800000, 900000]  # Zysk netto w PLN
liczba_akcji = 100000  # Liczba akcji firmy

# Obliczanie EPS dla każdego roku
eps = [oblicz_eps(zysk, liczba_akcji) for zysk in zyski_netto]

# Wizualizacja EPS
fig, ax1 = plt.subplots(figsize=(12, 6))

# Wykres EPS
ax1.plot(lata, eps, marker='o', color='blue', linestyle='-', linewidth=2, markersize=8, label='EPS (PLN)')
ax1.set_xlabel('Rok')
ax1.set_ylabel('EPS (PLN)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Dodawanie wartości EPS na wykresie
for i, txt in enumerate(eps):
    ax1.annotate(f'{txt:.2f}', (lata[i], eps[i]), textcoords="offset points", xytext=(0,5), ha='center', color='blue')

# Tworzenie drugiej osi Y dla wartości netto
ax2 = ax1.twinx()
ax2.plot(lata, zyski_netto, marker='s', color='green', linestyle='--', linewidth=2, markersize=8, label='Zysk Netto (PLN)')
ax2.set_ylabel('Zysk Netto (PLN)', color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Dodawanie wartości netto na wykresie
for i, txt in enumerate(zyski_netto):
    ax2.annotate(f'{txt:,}', (lata[i], zyski_netto[i]), textcoords="offset points", xytext=(0,-15), ha='center', color='green')

# Tytuł wykresu
fig.suptitle('EPS i Zysk Netto w latach')

# Legenda
fig.legend(loc='upper left', bbox_to_anchor=(0.1,0.9))

# Siatka
ax1.grid(True)

plt.tight_layout()
plt.show()

