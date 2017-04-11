from odenarium import *
from numpy import zeros, array

class BrownRobinson:

    def starter(self):
        erprint('Метод Брауна - Робинсон')
        print('''\nДля данного метода:
m - количество стратегий игрока A
n - количество стратегий игрока B
E - погрешность\n''')
        # while True:
        #     self.m = inN("Введите m: ", "Число должно быть натуральным, больше 1.")
        #     if self.m <= 1:
        #         erprint('Число меньше или равно 1!')
        #     else:
        #         break
        # while True:
        #     self.n = inN("Введите n: ", "Число должно быть натуральным, больше 1.")
        #     if self.n <= 1:
        #         erprint('Число меньше или равно 1!')
        #     else:
        #         break
        # while True:
        #     self.E = inFl('Введите E: ', "E должно быть числом большем 0")
        #     if self.E <= 0:
        #         erprint('Число меньше или равно 0!')
        #     else:
        #         break
        self.m = 3
        self.n = 4
        self.E = 0.1
        while True:
            self.method()
            if not YorN('Продолжить работу с программой? (Yes/No) '):
                return

    def input_start_tab(self, m, n):
        start_tab = zeros((m, n))
        print('Ввод матрицы A:')
        for i in range(m):
            for j in range(n):
                while True:
                    vvod = inFl('Значение ячейки A{0}B{1}: '.format(i+1, j+1), 'Значение должно быть числом большим 0')
                    if vvod > 0:
                        break
                start_tab[i, j] = vvod

        return start_tab

    def method(self):
        m = self.m
        n = self.n
        E = self.E
        # while True:
        #     start_tab = self.input_start_tab(m, n)
        #     print('Получившаяся Таблица:')
        #     print('A = \n', start_tab)
        #     if YorN('Таблица верна? Yes/No' ):
        #         break
        start_tab = array([[2, 3, 2, 4],
                           [3, 2, 4, 1],
                           [4, 1, 3, 2]])

        print(start_tab)
        if YorN('Выбрать вручную стратегии A и B на первом шаге? (Yes/No) '):
            while True:
                numA = inN('Введите № стратегии игрока A: ')
                if numA >=
            while True:
                numB = inN('Введите № стратегии игрока B: ')
        return


start = BrownRobinson()
start.starter()
