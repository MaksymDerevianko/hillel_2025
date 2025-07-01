
# task 01
alice_in_wonderland = (
    "Alice was beginning to get very tired of sitting by her sister on the bank, "
    "and of having nothing to do: once or twice she had peeped into the book her sister was reading, "
    "but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice "
    "'without pictures or conversation?'"
)

# task 02
for char in alice_in_wonderland:
    if char == "'":
        print(char)

# task 03
print(alice_in_wonderland)

# task 04
black_sea = 436_402
azov_sea = 37_800
total_area = black_sea + azov_sea
print("Сумарна площа морів:", total_area, "км²")

# task 05
total = 375_291
AB = 250_449
BC = 222_950
B = AB + BC - total
A = AB - B
C = BC - B
print("Склад 1:", A)
print("Склад 2:", B)
print("Склад 3:", C)

# task 06
months = 1.5 * 12
monthly_payment = 1179
total_cost = months * monthly_payment
print("Загальна вартість комп'ютера:", total_cost, "грн")

# task 07
numbers = [8019, 9907, 2789, 7248, 7128, 19224]
divisors = [8, 9, 5, 6, 5, 9]
for num, div in zip(numbers, divisors):
    print(f"{num} % {div} = {num % div}")

# task 08
total = (
    4 * 274 + 2 * 218 + 4 * 35 + 1 * 350 + 3 * 21
)
print("Загальна сума замовлення:", total, "грн")

# task 09
photos = 232
per_page = 8
pages = photos // per_page
if photos % per_page != 0:
    pages += 1
print("Потрібно сторінок:", pages)

# task 10
distance = 1600
fuel_per_100km = 9
tank_capacity = 48
fuel_needed = distance * fuel_per_100km / 100
import math
refills_rounded = math.ceil(fuel_needed / tank_capacity)
print("Потрібно пального:", fuel_needed, "л")
print("Кількість заправок:", refills_rounded)
