import re
import json

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

prices = re.findall(r'\n([\d\s]+,\d{2})\nСтоимость', text)

products = re.findall(r'\d+\.\n(.+)', text)

total = re.search(r'ИТОГО:\n([\d\s,]+)', text)

datetime = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})', text)

payment = re.search(r'Банковская карта', text)

data = {
    "products": products,
    "prices": prices,
    "total": total.group(1) if total else None,
    "date": datetime.group(1) if datetime else None,
    "time": datetime.group(2) if datetime else None,
    "payment_method": "Банковская карта" if payment else None
}

print(json.dumps(data, indent=4, ensure_ascii=False))

print("\n" + "="*80)
print(f"{'№':3} {'Product':50} {'Price':>10}")
print("-"*80)

for i, (name, price) in enumerate(zip(data["products"], data["prices"]), 1):
    print(f"{i:<3} {name[:50]:50} {price:>10}")

print("-"*80)
print(f"{'TOTAL':53} {data['total'] if data['total'] else ''}")
print(f"{'DATE':53} {data['date'] if data['date'] else ''}")
print(f"{'TIME':53} {data['time'] if data['time'] else ''}")
print(f"{'PAYMENT':53} {data['payment_method'] if data['payment_method'] else ''}")
print("="*80)