def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                line = line.strip()
                if not line:
                    continue 
                try:
                    name, salary_str = line.split(',')
                    salary = float(salary_str)
                    salaries.append(salary)
                except ValueError:
                    print(f"Помилка обробки рядка: '{line}' — пропущено.")
                    continue

            if not salaries:
                return 0, 0

            total = sum(salaries)
            average = total / len(salaries)
            return total, average

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0
    

total, average = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
