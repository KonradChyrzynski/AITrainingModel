import matplotlib.pyplot as plt

# Dane wejściowe
aktywa = {
    "Meble wolnostojące": 400,
    "Sprzęt elektroniczny (RTV)": 7850,
    "Inne środki transportu (rower, skuter)": 800,
    "Biżuteria": 2150,
    "Akcje, udziały w firmach": 13800,
    "Obligacje IKE": 23882,
    "Obligacje": 37168,
    "Lokaty w banku": 0,
    "Konto oszczędnościowe": 1200,
    "Rachunek bankowy": 3785,
    "Waluty obce": 600,
    "Gotówka": 50,
    "PPK": 3650,
}

zobowiazania = {
    "Pożyczka od rodziny": 0,
    "Księgowa": 0,
    "Podatki": 1,
    "Studia": 0,
}

wartosc_netto = [77288, 83288, 97467, 100000, 105000, 115000, 123000, 130000]

daty = [
    "05/06/2024", "06/07/2024", "07/08/2024",
    "08/09/2024", "09/10/2024", "11/10/2024",
    "11/11/2024", "12/12/2024"
]

# Obliczenia sum
suma_aktywa = sum(aktywa.values())
suma_zobowiazania = sum(zobowiazania.values())
wartosc_netto_obliczona = suma_aktywa - suma_zobowiazania

# Wykres 1: Kołowy aktywów i zobowiązań
fig1, ax1 = plt.subplots(1, 2, figsize=(12, 6))
ax1[0].pie(aktywa.values(), labels=aktywa.keys(), autopct='%1.1f%%', startangle=140)
ax1[0].set_title('Rozkład Aktywów')
ax1[1].pie(zobowiazania.values(), labels=zobowiazania.keys(), autopct='%1.1f%%', startangle=140)
ax1[1].set_title('Rozkład Zobowiązań')

# Wykres 2: Słupkowy aktywów i zobowiązań
fig2, ax2 = plt.subplots(figsize=(10, 6))
aktywa_keys = list(aktywa.keys())
aktywa_values = list(aktywa.values())
zobowiazania_keys = list(zobowiazania.keys())
zobowiazania_values = list(zobowiazania.values())

ax2.barh(aktywa_keys, aktywa_values, color='green', label='Aktywa')
ax2.barh(zobowiazania_keys, zobowiazania_values, color='red', label='Zobowiązania')
ax2.set_xlabel('Wartość (PLN)')
ax2.set_title('Porównanie Aktywów i Zobowiązań')
ax2.legend()

# Wykres 3: Wartość netto w czasie
fig3, ax3 = plt.subplots(figsize=(10, 6))
ax3.plot(daty, wartosc_netto, marker='o', color='blue')
ax3.set_xlabel('Data')
ax3.set_ylabel('Wartość netto (PLN)')
ax3.set_title('Zmiana Wartości Netto w Czasie')
ax3.grid(True)

# Wyświetlenie wszystkich wykresów
plt.tight_layout()
plt.show()

# Wypisanie sumy aktywów, zobowiązań i wartości netto
print(f"Suma aktywów: {suma_aktywa} zł")
print(f"Suma zobowiązań: {suma_zobowiazania} zł")
print(f"Twoja wartość netto wynosi: {wartosc_netto_obliczona} zł")
#Opis aplikacji:
#
#Funkcja `discounted_cash_flow` służy do obliczenia wartości wewnętrznej firmy na podstawie analizy zdyskontowanych przepływów pieniężnych (DCF).
#Analiza ta jest używana do oceny wartości inwestycji poprzez uwzględnienie przyszłych przepływów pieniężnych,
#które są zdyskontowane do wartości bieżącej. 
#
#Parametry wejściowe:
#- `free_cash_flows`: Lista przewidywanych wolnych przepływów pieniężnych w różnych latach.
#- `discount_rate`: Stopa dyskontowa, używana do przeliczenia przyszłych przepływów pieniężnych na ich wartość obecną.
#- `terminal_growth_rate`: Stopa wzrostu, używana do obliczenia wartości końcowej na podstawie ostatniego przepływu pieniężnego.
#
#Wyjście:
#- `intrinsic_value`: Wartość wewnętrzna firmy, obliczona jako suma zdyskontowanych przepływów pieniężnych i zdyskontowanej wartości końcowej.
#- `discounted_cash_flows`: Lista zdyskontowanych przepływów pieniężnych dla każdego roku.
#- `discounted_terminal_value`: Zdyskontowana wartość końcowa.
#
#Wizualizacja:
#Wykres przedstawia zarówno przewidywane przepływy pieniężne, jak i zdyskontowane przepływy pieniężne oraz wartość końcową. Pomaga to w ocenie, jak przyszłe przepływy pieniężne są wartościowane w bieżących dolarach oraz jakie jest ich znaczenie w kontekście całkowitej wartości firmy.
