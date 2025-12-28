rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'CAD': 1.25,
    'GBP': 0.75,
    'INR': 83.0,
    'JPY':148.0
}

amount =float(input("Enter the amount: "))
source = input("Enter the source currency (USD/EUR/CAD/GBP/INR/JPY): ").upper()
target = input("Enter the target currency (USD/EUR/CAD/GBP/INR/JPY): ").upper()

if source in rates and target in rates:
    converted_amount = amount * (rates[target] / rates[source])
    print(f"{amount} {source} is equal to {converted_amount:.2f} {target}")
else:
    print("Invalid input.")
