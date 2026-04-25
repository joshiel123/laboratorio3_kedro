import json

with open("data/08_reporting/resultado_analisis.json") as f:
    data = json.load(f)

print("Primeros valores del histograma:")
print(data["histograma"][0:255])