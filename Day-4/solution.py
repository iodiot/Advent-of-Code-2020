# --- Day 4: Passport Processing ---

def isnumeric(s):
    for ch in s:
        if ch < '0' or ch > '9':
            return False

    return True


def check_year(year, least, most):
    return len(year) == 4 and isnumeric(year) and int(year) >= least and int(year) <= most


def check_height(height):
    h, u = height[0:-2], height[-2:]
    if u == "cm" and len(h) == 3 and isnumeric(h) and int(h) >= 150 and int(h) <= 193:
        return True
    elif u == "in" and len(h) == 2 and isnumeric(h) and int(h) >= 59 and int(h) <= 76:
        return True

    return False


def check_eye(color):
    return color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def check_hair(hex):
    if hex[0] != "#" or len(hex) != 7:
        return False

    try:
        int(hex[1:], 16)
        return True
    except:
        return False


def check_pid(pid):
    return len(pid) == 9 and isnumeric(pid)


fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

f = open("input.txt", "r")

lines = [line for line in f]

f.close()

passports = map(lambda x: x.replace("\n", " "), ''.join(lines).split("\n\n"))

valid_count_first = 0
valid_count_second = 0

for passport in passports:
    z = map(lambda x: x.split(":"), passport.strip().split(" "))
    d = dict(zip(map(lambda x: x[0], z), map(lambda x: x[1], z)))

    if "cid" in d:
        del d["cid"]

    if len(set(fields).difference(set(d.keys()))) == 0:
        valid_count_first += 1

        ok = check_year(d["byr"], 1920, 2002) and check_year(d["iyr"], 2010, 2020) and check_year(d["eyr"], 2020, 2030) \
             and check_height(d["hgt"]) and check_hair(d["hcl"]) \
             and check_eye(d["ecl"]) and check_pid(d["pid"])

        valid_count_second += 1 if ok else 0

print("First part: ", valid_count_first)
print("Second part: ", valid_count_second)
