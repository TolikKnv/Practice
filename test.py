from chardet import detect

path = r"C:\Users\Honor\Desktop\24.12.csv"

with open(path, "rb") as f:
    data = f.read(50000)  # кусок файла
enc = detect(data)
print(enc)
