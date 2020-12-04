from functools import reduce

iA = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

iA = open('input4.txt').read()

keys = "byr iyr eyr hgt hcl ecl pid".split()
opt_key = "cid"
keys.sort()

iA = iA.split("\n\n")
passports = [paspo.split() for paspo in iA]

passes_ok = []
for paspo in passports:
    tags_exist = [False for _ in keys]

    pass_keys = [x.split(':')[0] for x in paspo]
    if opt_key in pass_keys:
        pass_keys.remove(opt_key)
    pass_keys.sort()

    pass_ok = pass_keys == keys
    passes_ok.append(pass_ok)

print(sum(passes_ok))