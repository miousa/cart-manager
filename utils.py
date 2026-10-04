# Проверка на число
def numeric_check(prompt: str) -> str | int:
    while True:
        try:
            choice = int(input(prompt))
            break
        except ValueError as e:
            print(f"Ошибка: {e} (Введи число!)")
            continue

    return choice
