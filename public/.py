# Генерация базы данных с 1500 турами и запись в файл
import random
from datetime import datetime, timedelta
import json

# Список городов
cities = {
    "Китай": ["Пекин", "Шанхай", "Гуанчжоу", "Чэнду", "Шэньчжэнь"],
    "Россия": ["Москва", "Санкт-Петербург", "Ростов-на-Дону", "Казань", "Новосибирск"],
    "США": ["Нью-Йорк", "Лос-Анджелес", "Чикаго", "Сан-Франциско", "Майами"],
    "Франция": ["Париж", "Марсель"],
    "Италия": ["Рим", "Венеция"],
    "Германия": ["Берлин", "Мюнхен"],
    "Испания": ["Мадрид", "Барселона"],
    "Япония": ["Токио", "Осака"],
    "Индия": ["Дели", "Мумбаи"],
    "Великобритания": ["Лондон", "Эдинбург"],
}

# Функция генерации случайной даты
def random_date():
    today = datetime.now()
    return today + timedelta(days=random.randint(1, 30))

# Функция для генерации одного тура
def generate_tour(id, city):
    tour_title = f"Экскурсия по городу {city}"
    description = f"Обзорная экскурсия для знакомства с культурой и историей города {city}."
    full_description = f"Экскурсия включает в себя посещение достопримечательностей города {city}, рассказ о его истории, культуре и современной жизни. Проводится опытным гидом."
    date = random_date().strftime("%Y-%m-%d")
    time_start = (datetime.now() + timedelta(hours=random.randint(9, 18), minutes=random.randint(0, 60))).strftime("%H:%M")
    time_end = (datetime.strptime(time_start, "%H:%M") + timedelta(hours=random.randint(1, 5), minutes=random.randint(0, 60))).strftime("%H:%M")
    departure = f"Центральная площадь, {city}"
    arrival = f"Исторический центр, {city}"
    distance_km = random.randint(5, 20)
    transport = random.choice(["метро", "автобус", "пешком", "велосипед"])
    sights = random.sample([
        "Бурдж-Халифа", "Бруклинский мост", "Тадж-Махал", "Колизей", "Эйфелева башня", 
        "Статуя Свободы", "Великая Китайская стена", "Кёльнский собор", "Тауэрский мост", "Золотые ворота"
    ], k=3)
    price = random.randint(500, 1500)
    image = "https://example.com/tour_1.jpg"

    return {
        "id": id,
        "title": tour_title,
        "description": description,
        "full_description": full_description,
        "date": date,
        "time_start": time_start,
        "time_end": time_end,
        "departure": departure,
        "arrival": arrival,
        "distance_km": distance_km,
        "transport": transport,
        "sights": sights,
        "city": city,
        "price": price,
        "image": image
    }

# Функция для генерации базы данных с 1500 турами
def generate_database(num_tours):
    tours = []
    id_counter = 1

    for country, country_cities in cities.items():
        for city in country_cities:
            for _ in range(num_tours // len(cities)):
                tour = generate_tour(id_counter, city)
                tours.append(tour)
                id_counter += 1
    
    return tours

# Генерация базы данных из 1500 туров
database = generate_database(1500)

# Запись в файл
file_path = '/mnt/data/tour_database.json'

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(database, f, ensure_ascii=False, indent=4)

file_path
