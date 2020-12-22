# --- Day 21: Allergen Assessment ---

foods = {}
all_ingredients = set()
freqs = {}

with open('input.txt') as f:
    for line in f:
        if line != '\n':
            ingredients, allergens = line.split('(contains ')
            ingredients = ingredients.strip(' ').split(' ')
            allergens = allergens.strip('\n').strip(')').split(', ')

            all_ingredients.update(set(ingredients))

            for i in ingredients:
                if i not in freqs:
                    freqs[i] = 1
                else:
                    freqs[i] = freqs[i] + 1

            for a in allergens:
                if a not in foods:
                    foods[a] = set(ingredients)
                else:
                    foods[a].intersection_update(set(ingredients))


free_ingredients = all_ingredients.copy()

for val in foods.values():
    free_ingredients.difference_update(val)

n = 0
for i in free_ingredients:
    n += freqs[i]

print("First part   :", n)

foods = dict(sorted(foods.items()))
while True:
    changed = False
    for allergen in foods.keys():
        if len(foods[allergen]) == 1:
            ingredient = list(foods[allergen])[0]
            for other_allergen in foods.keys():
                if allergen != other_allergen and ingredient in foods[other_allergen]:
                    foods[other_allergen].remove(ingredient)
                    changed = True

    if not changed:
        break

dangerous_list = ','.join(list(map(lambda x: str(list(x)[0]), foods.values())))

print("Second part  :", dangerous_list)
