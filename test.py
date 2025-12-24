from chardet import detect

path = r'C:\Users\Honor\Downloads\123.csv'

with open(path, 'rb') as f:
    data = f.read(50000)          # кусок файла
enc = detect(data)
print(enc)
