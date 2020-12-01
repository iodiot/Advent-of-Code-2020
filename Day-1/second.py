# coding=utf-8
# --- Day 1: Report Repair ---

f = open('input.txt', 'r')

arr = [int(line.strip()) for line in f]

arr.sort()

solution = -1

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            total = arr[i] + arr[j] + arr[k]
            if total >= 2020:
                if total == 2020:
                    solution = arr[i] * arr[j] * arr[k]
                break

print(solution)
