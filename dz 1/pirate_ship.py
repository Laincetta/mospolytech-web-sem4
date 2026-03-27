n, m = map(int, input().split())
items = []

for _ in range(m):
    name, weight, cost = input().split()
    weight = int(weight)
    cost = int(cost)
    value_per_unit = cost / weight
    items.append((name, weight, cost, value_per_unit))

items.sort(key=lambda x: x[3], reverse=True)

remaining_capacity = n
result = []

for name, weight, cost, _ in items:
    if remaining_capacity <= 0:
        break
    
    if weight <= remaining_capacity:
        result.append((name, float(weight), float(cost)))
        remaining_capacity -= weight
    else:
        part_weight = remaining_capacity
        part_cost = cost * (remaining_capacity / weight)
        result.append((name, part_weight, part_cost))
        remaining_capacity = 0

for name, weight, cost in result:
    print(f"{name} {weight:.2f} {cost:.2f}")