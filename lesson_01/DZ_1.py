# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03 == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
bananas = apples * 4
print(f"Apples: {apples}, Bananas: {bananas}")

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimeter = storona_1 + storona_2 + storona_3 + storona_4
print(f"Периметр фігури: {perimeter}")

# task 07
# У саду посадили 4 яблуні. Груш на 5 більше, слив на 2 менше.
apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2
total_trees = apple_trees + pear_trees + plum_trees
print(f"Усього дерев у саду: {total_trees}")

# task 08
# Температура змінилася протягом дня
temperature = 5
temperature -= 10
temperature += 4
print(f"Температура надвечір: {temperature} градусів")

# task 09
# У театральному гуртку
boys = 24
girls = boys // 2
present_boys = boys - 1
present_girls = girls - 2
total_present = present_boys + present_girls
print(f"Сьогодні у театральному гуртку {total_present} дітей")

# task 10
# Вартість трьох книг
book_1 = 8
book_2 = book_1 + 2
book_3 = (book_1 + book_2) / 2
total_price = book_1 + book_2 + book_3
print(f"Усі книги разом коштують {total_price} грн")
