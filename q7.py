#Team Coders: Dream Coders
def count_inventory(fruit_list: list[str]) -> dict[str, int]:
    inventory = {}
    for fruit in fruit_list:
        if fruit in inventory:
            inventory[fruit] += 1
        else:
            inventory[fruit] = 1
    return inventory
fruits = input().split()
result = count_inventory(fruits)
print(result)
