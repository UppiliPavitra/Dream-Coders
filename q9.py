#Team Coders:Dream Coders
def generate_threes(start: int, end: int) -> list[int]:
    if start >= end:
        return []
    return list(range(start, end, 3))
start = int(input( ))
end = int(input())
result = generate_threes(start, end)
print(result)
