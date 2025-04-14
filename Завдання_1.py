# Запитуємо дані у користувача
first_name = input("Введіть ім'я: ")
last_name = input("Введіть прізвище: ")
age = float(input("Введіть вік: "))
city = input("Введіть місто: ")

# Форматуємо та виводимо речення
formatted = f"Ім'я: {first_name:<10} | Вік: {age:.2f} | Місто: {city:>15}"
print(formatted)
