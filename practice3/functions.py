#1
#The function displays what kind of feed it is and its name.
"""
def describe_pet(name, animal_type="dog"):
    print(f"I have a pet — {animal_type} name is {name}.")
n=input()
describe_pet("Bella")
describe_pet("Charlie", "cat")
describe_pet(n)
"""
#2
# Returns two values:the total sum of all prices the average price (if there are no products → 0)
"""
def total_cost(shop_name, *prices):
    if not prices:
        return 0, 0
    #The function calculates the total amount and average price of goods
    total = sum(prices)
    average = total / len(prices)
    return total, average

name=input("Enter store name:")
cost=list(map(int, input("Please enter prices separated by spaces:").split()))
summa,avg=total_cost(name,*cost)
print(f"In {name}: total {summa} tg, average price {avg:.0f} tg")
"""
#3
#Creates a user profile based on provided information.
"""
def create_profile(username, **kwargs):
    profile = {"username": username}
    
    # Add only the fields we care about
    if "age" in kwargs:
        profile["age"] = kwargs["age"]
    if "city" in kwargs:
        profile["city"] = kwargs["city"]
    if "hobbies" in kwargs and isinstance(kwargs["hobbies"], (list, tuple)):
        profile["hobbies"] = kwargs["hobbies"]
    
    return profile

username = input("Enter username: ")

# Optional inputs
age_input = input("Enter age (or leave blank): ")
if age_input:
    age = int(age_input)
else:
    age = None
city = input("Enter city (or leave blank): ")

hobbies_input = input("Enter hobbies separated by commas (or leave blank): ")
if hobbies_input:
    hobbies = [h.strip() for h in hobbies_input.split(",")]
else:
    hobbies = None
# Prepare keyword arguments
kwargs = {}
if age is not None:
    kwargs["age"] = age
if city:
    kwargs["city"] = city
if hobbies:
    kwargs["hobbies"] = hobbies

# Create profile
profile = create_profile(username, **kwargs)

# Print profile
print("\nUser profile:")
print(profile)
"""
#4
#The function takes a list of items, adds "cookies" if "tea" is present, 
# calculates the total price, applies any discount, and returns the final order, 
# total before discount, and total after discount.
"""
def process_order(items, discount_percent=0):
    order = items.copy()
    
    # Promotion: if there is tea → add cookies as a gift
    if "tea" in order:
        order.append("cookies")
    
    price_per_item = 1500
    total_before_discount = len(order) * price_per_item
    
    discount_amount = total_before_discount * (discount_percent / 100)
    total_after_discount = total_before_discount - discount_amount
    
    return order, total_before_discount, total_after_discount


items_input = input("Enter items separated by commas or spaces: ")


items = [item.strip() for item in items_input.replace(",", " ").split() if item.strip()]

discount_input = input("Enter discount percent (press Enter for 0): ")
if discount_input == "":
    discount = 0
else:
    discount = float(discount_input)

# Call function
final_order, total_before, total_after = process_order(items, discount)

# Print results
print("\nFinal order:", final_order)
print("Total before discount:", total_before, "tg")
print("Total after discount:", total_after, "tg")
print("Original items list:", items)
#'bread', 'milk', 'tea', 'apples'
"""



