import sys

class Equation:
    """Класс для биквадратного уравнения"""

    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.roots = []

    def input_coefficient(self, name, can_be_zero=True):
        """Ввод одного коэффициента"""
        while True:
            print(f"Введите {name}:")
            value = input()

            if value.replace('.', '').replace('-', '').isdigit():
                num = float(value)

                if not can_be_zero and num == 0:
                    print(f"{name} не может быть 0!")
                    continue

                return num
            else:
                print("Не число! Попробуйте снова.")

    def input_all(self):
        """Ввод всех коэффициентов"""
        print("Введите коэффициенты биквадратного уравнения A*x^4 + B*x^2 + C = 0")
        self.a = self.input_coefficient("A", can_be_zero=False)
        self.b = self.input_coefficient("B")
        self.c = self.input_coefficient("C")

    def solve(self):
        """Решение уравнения"""
        print(f"\nРешаем: {self.a}*x^4 + {self.b}*x^2 + {self.c} = 0")

        D = self.b**2 - 4*self.a*self.c
        print(f"Дискриминант: {D}")

        if D < 0:
            print("Корней нет")
            return

        if D == 0:
            y = -self.b / (2*self.a)
            if y > 0:
                self.roots = [y**0.5, -y**0.5]
            elif y == 0:
                self.roots = [0]
        else:
            y1 = (-self.b + D**0.5) / (2*self.a)
            y2 = (-self.b - D**0.5) / (2*self.a)

            self.roots = []
            if y1 > 0:
                self.roots.extend([y1**0.5, -y1**0.5])
            if y2 > 0:
                self.roots.extend([y2**0.5, -y2**0.5])
            if y1 == 0 or y2 == 0:
                self.roots.append(0)

            self.roots = list(set(self.roots))
            self.roots.sort()

    def show_roots(self):
        """Показ корней"""
        if self.roots:
            print(f"Найдено корней: {len(self.roots)}")
            for i, root in enumerate(self.roots, 1):
                print(f"x{i} = {root:.4f}")
        else:
            print("Действительных корней нет")

print("РЕШЕНИЕ БИКВАДРАТНОГО УРАВНЕНИЯ")

eq = Equation()

eq.input_all()

eq.solve()

eq.show_roots()
