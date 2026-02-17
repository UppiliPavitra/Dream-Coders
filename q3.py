#Team Name: Dream Coders
def average_passing_grades(grades):
    total = 0
    count = 0
    for grade in grades:
        if grade >= 50:
            total += grade
            count += 1
    if count == 0:
        return 0.0
    else:
        return total / count
grades = list(map(int, input().split()))
result = average_passing_grades(grades)
print(result)
