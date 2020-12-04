from functools import reduce

iA = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

iA = open('input4.txt').read()

eye_colors = "amb blu brn gry grn hzl oth".split()

iA = iA.split("\n\n")
passports = [paspo.split() for paspo in iA]

def check_if(key, low, high, dct):
    if not key in dct.keys():
        return False
    try:
        if not low <= int(dict[key]) <= high:
            return False
    except:
        return False
    return True

mcs = [
    ["byr", 1920, 2002],
    ["iyr", 2010, 2020],
    ["eyr", 2020, 2030],
]

passes_ok = 0
for paspo in passports:

    passss = [x.split(':') for x in paspo]
    passss = {x[0] : x[1] for x in passss}
    
    # ugly, I know, but I won't rewrite it right now
    year_checks = [check_if(mcs[0], mcs[1], mcs[2], passss) for _ in mcs]

    if sum(year_checks) < 3:
        continue

    if not "hgt" in passss.keys():
        continue

    if passss["hgt"][-2:] != "cm":
        if 150 <= int(passss["hgt"][:-2]) <= 193:
            continue 
    elif passss["hgt"][-2:] != "in":
        if 59 <= int(passss["hgt"][:-2]) <= 76:
            continue
    else:
        continue

    if not "hcl" in passss.keys():
        continue

    if passss["hcl"][0] != "#":
        continue
    
    char_list = [str(x) for x in range(10)]
    char_list = char_list + ['a','b','c','d','e','f']
    matched_chars = [char in char_list for char in passss["hcl"][1:]]
    if sum(matched_chars) != 7:
        continue

    if not "ecl" in passss.keys():
        continue
    
    if passss["ecl"] not in eye_colors:
        continue

    if not "pid" in passss.keys():
        continue

    try:
        int(passss["pid"])
    except:
        continue

    if len(passss["pid"]) > 10:
        continue

print(sum(passes_ok))