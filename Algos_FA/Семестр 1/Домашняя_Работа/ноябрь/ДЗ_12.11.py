peoples = {
    "участник 1": {"русский", "английский"},
    "участник 2": {"китайский", "английский"},
    "участник 3": {"китайский", "французский", "немецкий", "английский"},
    "участник 4": {"русский", "испанский", "английский"},
    "участник 5": {"испанский", "китайский", "английский"},
    "участник 6": {"итальянский", "португальский", "английский"},
}
# 1
print(
    peoples["участник 1"]
    & peoples["участник 2"]
    & peoples["участник 3"]
    & peoples["участник 4"]
    & peoples["участник 5"]
    & peoples["участник 6"]
)
# 2
for k, v in peoples.items():
    if v & {"русский"} == set():
        print(k)
# 3
translate_language = list(
    (
        peoples["участник 1"]
        | peoples["участник 2"]
        | peoples["участник 3"]
        | peoples["участник 4"]
        | peoples["участник 5"]
        | peoples["участник 6"]
    )
    - {"русский", "английский"}
)
print(translate_language)
for item in translate_language:
    kol=0
    for item_dict in peoples.values():
        if {item}&item_dict=={item}:
            kol+=1
    print(f'Перевод нужен на {item} язык, его знают {kol} участника')