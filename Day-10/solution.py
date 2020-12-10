# --- Day 10: Adapter Array ---

ratings = sorted([int(line) for line in open('input.txt')])

ratings.insert(0, 0)
ratings.append(ratings[-1] + 3)

differences = []

for i in range(1, len(ratings)):
    differences.append(ratings[i] - ratings[i - 1])

print "First part: ", differences.count(1) * differences.count(3)

ratings = sorted([int(line) for line in open('input.txt')])
ratings.append(ratings[-1] + 3)

arr = {0: 1}

for r in ratings:
    arr[r] = arr.get(r - 1, 0) + arr.get(r - 2, 0) + arr.get(r - 3, 0)

print "Second part: ", arr[ratings[-1]]
