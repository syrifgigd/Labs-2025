import sys

print("Программа для решения биквадратного уравнения: A*x^4 + B*x^2 + C = 0")

a = b = c = None

if len(sys.argv) >= 4:
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
        print(f"Коэффициенты из командной строки: A={a}, B={b}, C={c}")
    except ValueError:
        print("Некорректные параметры командной строки. Вводим с клавиатуры.")
        a = b = c = None

if a is None:
    while True:
        try:
            print("Введите коэффициент A:")
            a = float(input())
            if a != 0:
                break
            else:
                print("A не может быть 0!")
        except ValueError:
            print("Ошибка! Введите число.")

if b is None:
    while True:
        try:
            print("Введите коэффициент B:")
            b = float(input())
            break
        except ValueError:
            print("Ошибка! Введите число.")

if c is None:
    while True:
        try:
            print("Введите коэффициент C:")
            c = float(input())
            break
        except ValueError:
            print("Ошибка! Введите число.")

print(f"\nУравнение: {a}*x^4 + {b}*x^2 + {c} = 0")

D = b*b - 4*a*c
print(f"Дискриминант: {D}")

roots = []

if D < 0:
    print("Действительных корней нет.")
elif D == 0:
    y = -b / (2*a)
    if y > 0:
        roots.extend([y**0.5, -y**0.5])
    elif y == 0:
        roots.append(0)
else:
    y1 = (-b + D**0.5) / (2*a)
    y2 = (-b - D**0.5) / (2*a)

    if y1 > 0:
        roots.extend([y1**0.5, -y1**0.5])
    elif y1 == 0:
        roots.append(0)

    if y2 > 0:
        roots.extend([y2**0.5, -y2**0.5])
    elif y2 == 0 and 0 not in roots:
        roots.append(0)

if roots:
    roots = sorted(list(set(roots)))
    print(f"Действительные корни: {[f'{x:.4f}' for x in roots]}")
else:
    print("Действительных корней нет.")
