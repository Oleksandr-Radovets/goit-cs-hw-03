from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://admin:password@localhost:27017/")
db = client["cat_database"]
collection = db["cats"]


def create_cat(name, age, features):
    cat = {"name": name, "age": age, "features": features}
    result = collection.insert_one(cat)
    print(f"Кіт {name} доданий з ID {result.inserted_id}")


def get_all_cats():
    cats = collection.find()
    for cat in cats:
        print(cat)


def find_cat_by_name(name):
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Кіт з ім'ям {name} не знайдений")


def update_cat_age(name, new_age):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.matched_count:
        print(f"Вік кота {name} оновлено до {new_age}")
    else:
        print(f"Кіт з ім'ям {name} не знайдений")


def add_feature_to_cat(name, new_feature):
    result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
    if result.matched_count:
        print(f"Характеристика '{new_feature}' додана коту {name}")
    else:
        print(f"Кіт з ім'ям {name} не знайдений")


def delete_cat(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count:
        print(f"Кіт {name} видалений")
    else:
        print(f"Кіт з ім'ям {name} не знайдений")


def delete_all_cats():
    result = collection.delete_many({})
    print(f"Видалено {result.deleted_count} котів")


# Тестові виклики функцій
if __name__ == "__main__":
    # Створення записів
    create_cat("Барсик", 3, ["рудий", "дає себе гладити"])
    create_cat("Мурчик", 5, ["сірий", "любить рибу"])

    # Читання записів
    print("\nВсі коти:")
    get_all_cats()

    print("\nЗнайти кота Барсика:")
    find_cat_by_name("Барсик")

    # Оновлення
    print("\nОновлення віку Барсика:")
    update_cat_age("Барсик", 4)

    print("\nДодавання характеристики для Барсика:")
    add_feature_to_cat("Барсик", "ходить в капці")

    # Видалення
    print("\nВидалення Мурчика:")
    delete_cat("Мурчик")

    print("\nВидалення всіх котів:")
    delete_all_cats()
