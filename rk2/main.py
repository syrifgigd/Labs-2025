from data_manager import DataManager

def main():
    manager = DataManager()

    print("=== ЗАПРОС 1 ===")
    print("Список всех связанных компьютеров и ОС (сортировка по компьютерам):")
    print("-" * 50)
    manager.display_one_to_many_relations()
    print()

    print("=== ЗАПРОС 2 ===")
    print("Список ОС с количеством компьютеров (сортировка по количеству):")
    print("-" * 50)
    manager.display_os_computer_count()
    print()

    print("=== ЗАПРОС 3 ===")
    print("Список компьютеров с брендом, заканчивающимся на 'ov', и их ОС:")
    print("-" * 50)
    manager.display_computers_with_ov_brand()

if __name__ == "__main__":
    main()
