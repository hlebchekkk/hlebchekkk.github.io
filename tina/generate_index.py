import os
import json

# Название выходного файла
OUTPUT_FILENAME = "index.json"

# Получаем список файлов в текущей директории
files = [
    f for f in os.listdir(".")
    if os.path.isfile(f) and f != OUTPUT_FILENAME and f != "generate_index.py" and f != "random.html"
]

# Сортируем (по желанию)
files.sort()

# Записываем в JSON
with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
    json.dump(files, f, ensure_ascii=False, indent=2)

print(f"{OUTPUT_FILENAME} успешно создан с {len(files)} файлами.")