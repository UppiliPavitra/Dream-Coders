# Team Name: Dream Coders
def calculate_total_bill(amount:float,tip_percent:int)->float:
    total=float(amount)+(float(amount)*(tip_percent/100))
    return round(total,2)
