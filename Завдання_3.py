# Дані про студентів
students = [
    ("Олена", 89.5, 95),
    ("Ігор", 76.2, 88),
    ("Марія", 92.1, 100),
    ("Дмитро", 68.3, 73)
]

# Заголовок звіту
print("ЗВІТ ПРО УСПІШНІСТЬ СТУДЕНТІВ")
print("=" * 50)
print("{:<15} {:>15} {:>15}".format("Ім'я", "Сер. бал", "Відвідуваність %"))
print("-" * 50)

# Підрахунок загального балу
total_score = 0
for name, score, attendance in students:
    print("{:<15} {:>15.2f} {:>15.0f}".format(name, score, attendance))
    total_score += score

# Підсумок
average_score = total_score / len(students)
print("=" * 50)
print(f"{'Середній бал по групі:':<30} {average_score:.2f}")
