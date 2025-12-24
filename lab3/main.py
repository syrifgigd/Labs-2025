import requests  # внешний пакет
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

def main():
    N = 17

    rectangle = Rectangle(N, N, "синего")
    circle = Circle(N, "зеленого")
    square = Square(N, "красного")

    print(rectangle)
    print(circle)
    print(square)

    print("\nдемонстрация работы внешнего пакета (requests):")
    try:
        response = requests.get('https://httpbin.org/get')
        print(f"Статус код запроса: {response.status_code}")
        print("Запрос выполнен успешно!")
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")

if __name__ == "__main__":
    main()
