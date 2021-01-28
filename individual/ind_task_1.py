# !/usr/bin/evn python3
# -*- config: utf-8 -*-


# Дан список X из n вещественных чисел. Найти минимальный элемент списка,, используя
# вспомогательную рекурсивную функцию, находящую минимум среди последних элементов
# списка , начиная с n-гo.


def min_el_from(i, mini, lis):
    if i == len(lis):
        return mini
    else:
        if lis[i] < mini:
            mini = lis[i]
        i += 1
    return min_el_from(i, mini, lis)


if __name__ == '__main__':
    Lst = [0.9, 9.8, 5.2, 7.5, 1.2]
    frm = 2
    print(min_el_from(frm - 1, Lst[frm - 1], Lst))
