
# Чтение файла .ini и создание словаря
config_pairs = {}  # {'a': 'z', 'b': 'y', 'c': 'x'}
with open('settings.ini', 'r') as settings_file:
    for line in settings_file:
        key, value = line.strip().split('=')
        config_pairs[key] = value

# Чтение файла .txt и замена значений из файла конфигурации
changed_lines = []
with open('sample_text.txt', 'r') as text_file:
    for line in text_file:
        for key, value in config_pairs.items():
            line = line.replace(key, value)
        changed_lines.append(line)

# Сортировка измененных строк по общему количеству заменяемых символов
changed_lines.sort(key=lambda x: x[2], reverse=True)
print(''.join(changed_lines))