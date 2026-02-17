# Team Name: Dream Coders
def calculate_total_bill(amount: float, tip_percent: int) -> float:
    total = amount + (amount * tip_percent / 100)
    return round(total, 2)
amount = float(input())
tip_percent = int(input())
result = calculate_total_bill(amount, tip_percent)
print(result)
