# --- Day 21: Allergen Assessment ---

foods = []

all_ingredients = set()

with open('input.txt') as f:
    for line in f:
        if line != '\n':
            ingredients, allergens = line.split('(contains ')
            ingredients = ingredients.strip(' ').split(' ')
            allergens = allergens.strip('\n').strip(')').split(', ')

            foods.append([set(ingredients), set(allergens)])

            for i in ingredients:
                all_ingredients.add(i)


allergen_free = set()

for ingr in all_ingredients:
    free = True
    for food in foods:
        if ingr in food[0]:
            if len(food[0]) < len(food[1]) + 1:
                free = False
                break

    if free:
        for food in foods:
            if ingr in food[0]:
                food[0].remove(ingr)

        allergen_free.add(ingr)

        print(ingr)


print(foods)


print("First part: ", allergen_free)
print("Second part: ", )
