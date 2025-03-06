import json

data = {"ad": "Ali", "yaş": 15, "şehir": "İstanbul"}
with open("veri.json","w",encoding="utf-8") as dosya:
    json.dump(data,dosya,ensure_ascii=False,indent=4)