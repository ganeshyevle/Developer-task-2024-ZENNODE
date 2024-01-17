products = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}
discount_rules = {
    "flat_10_discount": 10,
    "bulk_5_discount": 0.05,
    "bulk_10_discount": 0.1,
    "tiered_50_discount": 0.5
}
gift_wrap_fee = 1
shipping_fee_per_package = 5
units_per_package = 10

quantities = {}
gift_wraps = {}
for product in products:
    quantities[product] = int(input(f"Enter quantity for {product}: "))
    gift_wraps[product] = input(f"Is {product} wrapped as a gift? (yes/no): ").lower() == 'yes'

subtotal = sum(quantities[product] * products[product] for product in products)
discount_name = ""
discount_amount = 0
for rule, value in discount_rules.items():
    if rule == "flat_10_discount" and subtotal > 200:
        discount_name, discount_amount = rule, value
    elif rule == "bulk_5_discount" and any(quantities[product] > 10 for product in products):
        discount_name, discount_amount = rule, value * subtotal
    elif rule == "bulk_10_discount" and sum(quantities.values()) > 20:
        discount_name, discount_amount = rule, value * subtotal
    elif rule == "tiered_50_discount" and sum(quantities.values()) > 30 and any(quantities[product] > 15 for product in products):
        discount_name, discount_amount = rule, value * (subtotal - sum(products[product] * 15 for product in products))

subtotal -= discount_amount
gift_wrap_fees = sum(gift_wrap_fee * quantities[product] for product in products if gift_wraps[product])
shipping_fees = (sum(quantities.values()) // units_per_package) * shipping_fee_per_package
total = subtotal + gift_wrap_fees + shipping_fees
print("\nProduct Details:")
for product in products:
    print(f"{product}: Quantity - {quantities[product]}, Total - {quantities[product] * products[product]}")

print("\nSubtotal:", subtotal)
print(f"Discount Applied ({discount_name}):", discount_amount)
print("Gift Wrap Fees:", gift_wrap_fees)
print("Shipping Fees:", shipping_fees)
print("\nTotal:", total)
