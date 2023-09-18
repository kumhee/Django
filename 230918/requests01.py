from urllib.request import urlopen
f = urlopen("http://www.example.com")
print(f.read(500).decode('utf-8'))

data = "language=python&frameword=django"
f = urlopen('http://127.0.0.1:8000', bytes(data, encoding='utf-8'))
print(f.read().decode('utf-8'))

