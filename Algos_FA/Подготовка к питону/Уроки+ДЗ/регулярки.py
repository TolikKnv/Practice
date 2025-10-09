import re

# 1
# n = input()
# d = n.split()
# l = []
# p = re.compile(r"\b[eyuioa|EYUIOA|уеыаоэяию|УЕЫАОЭЯИЮ]\w*")
# for i in d:
#     if p.match(i):
#         l.append(i[::-1])
# print(l)

# 2
# n = "aaa--bbb==ccc__ddd"
# p = re.compile(r"[a-z]{3}")
# c = p.findall(n)
# print(c)

# 3
# st = input()
# p = re.compile(r"[a-zA-Z]+")
# print(p.findall(st)[0])


# 4
# st = input()
# p = re.compile(r"[a-zA-Z]+")
# print(p.findall(st)[-1])


# 5
# s = """My uncle -- hgh ideals inspire him;
# but when past joking he fell sick,
# he really forced one to admire him --
# and never played a shrewder trick.
# Let others learn from his example!
# But God, how deadly dull to sample
# sickroom attendance night and day
# and never stir a foot away!"""


# p = re.compile(r"\b[eyuioa|EYUIOA|уеыаоэяию|УЕЫАОЭЯИЮ]\w+")

# print(p.findall(s))


# 6
# s = """My uncle -- hgh ideals inspire him;
# but when past joking he fell sick,
# he really forced one to admire him --
# and never played a shrewder trick.
# Let others learn from his example!
# But God, how deadly dull to sample
# sickroom attendance night and day
# and never stir a foot away!"""

# s = s.split("\n")

# p = re.compile(r"\b[a-zA-z]\w+")

# for i in s:
#     print(p.findall(i)[0])


# 7
pattern = r'^\+7\s?[\(]?\d{3}[\)\s]?\s?\d{3}[-\s]?\d{2}[-\s]?\d{2}$'

numbers = [
    '+7(999)999-99-99',
    '+7 (999) 999-99-99олень',
    '+7 999 999-99-99',
    '+7 999 999 99 99',
    '+79999999999',
    '+7-999-999-9999',  # неправильный формат
]

for num in numbers:
    print(num, '—', 'OK' if re.match(pattern, num) else 'INVALID')
a = 3+2
print(a)
