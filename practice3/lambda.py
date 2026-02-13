#1
# Add 12% VAT using map() and lambda, rounding to nearest integer
"""
prices = list(map(int,input().split("enter prices")))
prices_with_vat = list(map(lambda x: round(x * 1.12), prices))
print("Prices without VAT(ндс): ", prices)
print("Prices with 12% VAT(ндс):", prices_with_vat)
"""
#2
"""
cities_input = input("Enter city names separated by commas or spaces: ")

cities = [city.strip() for city in cities_input.replace(",", " ").split() if city.strip()]
cities_with_a = list(filter(lambda x: "а" in x.lower(), cities))

cities_long_name = list(filter(lambda x: len(x) >= 7, cities))
cities_same_start_end = list(filter(lambda x: x[0].lower() == x[-1].lower(), cities))

print(f"\nCities containing 'a' or 'А': {len(cities_with_a)} cities. Examples:", cities_with_a[:5])
print(f"Cities with length ≥ 7 letters: {len(cities_long_name)} cities. Examples:", cities_long_name[:5])
print(f"Cities starting and ending with the same letter: {len(cities_same_start_end)} cities. Examples:", cities_same_start_end[:5])
#Алматы, Астана, Шымкент, Актобе, Қарағанды
"""
#3
# Original list of orders (customer, product, price, quantity)
"""
orders = [
    ("Айжан",   "iPhone 14",     428000,  2),
    ("Данияр",  "MacBook Air",   589000,  1),
    ("Аружан",  "AirPods Pro",    95000,  3),
    ("Ербол",   "iPhone 14",     428000,  1),
    ("Софья",   "iPad Pro",      489000,  1),
    ("Мирлан",  "AirPods Pro",    95000,  5),
    ("Амина",   "MacBook Air",   589000,  2),
]
sorted_by_name = sorted(orders, key=lambda x: x[0])

sorted_by_total_price = sorted(orders, key=lambda x: x[2]*x[3], reverse=True)

sorted_by_product_qty = sorted(orders, key=lambda x: (x[1], -x[3]))

sorted_by_qty_name = sorted(orders, key=lambda x: (-x[3], x[0]), reverse=False)

sorted_by_qty_name = sorted(orders, key=lambda x: (-x[3], x[0][::-1]))

def print_top(title, lst, top=4):
    print(f"\n{title} (top {top}):")
    for row in lst[:top]:
        customer, product, price, qty = row
        total = price * qty
        print(f"{customer:10} | {product:12} | {price:7} | {qty:2} | total: {total}")

print_top("Sorted by customer name (А→Я)", sorted_by_name)
print_top("Sorted by total price descending", sorted_by_total_price)
print_top("Sorted by product name + quantity descending", sorted_by_product_qty)
print_top("Sorted by quantity descending + customer name reverse", sorted_by_qty_name)
"""
#4
"""
numbers = list(map(int,input().split()))

evens = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", evens)
"""




