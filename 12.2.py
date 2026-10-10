import json

with open("products.json", encoding="utf-8") as f:
    data = json.load(f)

name = input("Введите название продукта:\n")
price = int(input("Введите цену:\n"))
weight = int(input("Введите вес:\n"))
answer = input("Товар в наличии? (да/нет):\n")

if answer.lower() == "да":
    available = True
else:
    available = False

new_product = {
    "name": name,
    "price": price,
    "available": available,
    "weight": weight
}

data["products"].append(new_product)

with open("products.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print()
print("Обновлённый файл:")
print()

for product in data["products"]:
    print("Название:", product["name"])
    print("Цена:", product["price"])
    print("Вес:", product["weight"])
    if product["available"]:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print()