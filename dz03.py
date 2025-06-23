import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama
init(autoreset=True)

def print_directory_tree(path: Path, prefix: str = ""):
    """Рекурсивно виводить структуру директорії з кольоровим форматуванням."""
    try:
        items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
        for index, item in enumerate(items):
            connector = "┗━ " if index == len(items) - 1 else "┣━ "
            if item.is_dir():
                print(f"{prefix}{connector}{Fore.BLUE}{item.name}/")
                print_directory_tree(item, prefix + ("    " if index == len(items) - 1 else "┃   "))
            else:
                print(f"{prefix}{connector}{Fore.GREEN}{item.name}")
    except PermissionError:
        print(f"{prefix}{Fore.RED}[Permission Denied] {path}")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Помилка: Вкажіть шлях до директорії як єдиний аргумент.")
        print(f"{Fore.YELLOW}Приклад: python dz03.py /шлях/до/директорії")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if not input_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{input_path}' не існує.")
        sys.exit(1)

    if not input_path.is_dir():
        print(f"{Fore.RED}Помилка: Шлях '{input_path}' не є директорією.")
        sys.exit(1)

    print(f"{Fore.CYAN}Структура директорії: {input_path}\n")
    print_directory_tree(input_path)

if __name__ == "__main__":
    main()
