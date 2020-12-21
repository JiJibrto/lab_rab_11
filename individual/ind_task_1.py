# !/usr/bin/evn python3
# -*- config: utf-8 -*-


# Дан список X из n вещественных чисел. Найти минимальный элемент списка,, используя
# вспомогательную рекурсивную функцию, находящую минимум среди последних элементов
# списка , начиная с n-гo.


def min_el_from(i, start):
    mini = start
    if i >= len(Lst):
        print(f"Minimal element is: {mini}")
        return mini
    elif Lst[i - 1] < mini:
        mini = Lst[i-1]
    min_el_from(i + 1, mini)


if __name__ == '__main__':
    Lst = list(map(float, input("Enter elements> ").split(" ")))
    frm = int(input("Enter number from start> "))
