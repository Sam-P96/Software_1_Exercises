a = float(input("Enter talents: \n"))
print()
b = float(input("Enter pounds: \n"))
print()
c = float(input("Enter lots: \n"))
print()

a_talents_to_pound = a * 20
a_pound_to_lots = a_talents_to_pound * 32
a_lots_to_grams = a_pound_to_lots * 13.3

b_pound_to_lots = b * 32
b_lots_to_grams = b_pound_to_lots * 13.3

c_lots_to_grams = c * 13.3

modern_total_grams = a_lots_to_grams + b_lots_to_grams + c_lots_to_grams

kg_portion = modern_total_grams // 1000
grams_portion = modern_total_grams % 1000

print(f"""The weight in modern units:
{int(kg_portion)} kilograms and {round(grams_portion, 2)} grams.""")