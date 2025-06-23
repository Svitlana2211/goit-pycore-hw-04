def get_cats_info(path):
    cats_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                parts = line.split(',')
                if len(parts) == 3:
                    cat_dict = {
                        'id': parts[0],
                        'name': parts[1],
                        'age': parts[2]
                    }
                    cats_list.append(cat_dict)
    except FileNotFoundError:
        print(f"Файл не знайдено за шляхом: {path}")
    except Exception as e:
        print(f"Сталася помилка: {e}")

    return cats_list

cats_info = get_cats_info("cats.txt")
print(cats_info)
