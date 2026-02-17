#Team Coders: Dream Coders
def organize_scores(scores: list[int], descending: bool) -> list[int]:
    return sorted(scores, reverse=descending)
scores = list(map(int, input().split()))
descending_input = input()
descending = descending_input.lower() == "true"
result = organize_scores(scores, descending)
print( result)
