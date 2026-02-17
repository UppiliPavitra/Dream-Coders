#Team Name: Dream Coders
def get_ticket_price(age: int, is_student: bool) -> int:
    if age < 12:
        return 8
    elif age >= 65:
        return 10
    else: 
        if is_student:
            return 12
        else:
            return 15
age = int(input())
student_input = input().strip().lower()
is_student = student_input == "true"
price = get_ticket_price(age, is_student)
print( price)
