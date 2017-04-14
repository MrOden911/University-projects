from odenarium import *
from numpy import zeros, array, dot
from sympy import Rational


class BrownRobinson:

    def starter(self):
        erprint('Метод Брауна - Робинсон')
        print('''\nДля данного метода:
m - количество стратегий игрока A
n - количество стратегий игрока B
E - погрешность
max_hod - максимальное количество шагов\n''')
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
        #     self.E = inFl('Введите E: ', "E должно быть числом большим 0")
        #     if self.E <= 0:
        #         erprint('Число меньше или равно 0!')
        #     else:
        #         break
        # while True:
        #     self.max_hod = inN('Введите max_hod: ', "max_hod должно быть натуральным числом большим 0")
        #     if self.E <= 0:
        #         erprint('Число меньше или равно 0!')
        #     else:
        #         break
        self.m = 3
        self.n = 4
        self.E = 0.1
        self.max_hod = 15
        while True:
            self.method()
            if not YorN('\nПродолжить работу с программой? (Yes/No) '):
                return

    def input_start_tab(self, m, n):
        start_tab = zeros((m, n))
        print('Ввод матрицы A:')
        for i in range(m):
            for j in range(n):
                while True:
                    vvod = inFl('Значение ячейки A{0}B{1}: '.format(i+1, j+1), 'Значение должно быть числом большим 0')
                    if vvod <= 0:
                        erprint('Введено число меньшее 0!')
                    else:
                        break
                start_tab[i, j] = vvod

        return start_tab

    def method(self):
        m = self.m
        n = self.n
        E = self.E
        max_hod = self.max_hod
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

        numA = ''
        numB = ''
        if YorN('Выбрать вручную стратегии A и B на первом шаге? (Yes/No) '):
            while True:
                numA = inN('Введите № стратегии игрока A: ')
                if numA > m:
                    erprint('Число вне заданного количества!')
                else:
                    break
            while True:
                numB = inN('Введите № стратегии игрока B: ')
                if numB > n:
                    erprint('Число вне заданного количества!')
                else:
                    break

        tab = ['k', 'A(k)', 'B(k)', 'P(k)', 'Q(k)', 'aP(k)', 'bQ(k)', 'a(k)', 'b(k)', 'd(k)', '2*E']
        res_tab = []
        a_summ = zeros(m)
        b_summ = zeros(n)
        a_list = []
        b_list = []
        for k in range(1, (max_hod+1)):
            counter = k

            res_tab.append(k)

            if numA == '':
                acct_list = []
                for i in range(m):
                    acct_list.append(start_tab[i, :].sum())
                numA = 1 + acct_list.index(max(acct_list))
                acct_list = []
                for i in range(n):
                    acct_list.append(start_tab[:, i].sum())
                numB = 1 + acct_list.index(min(acct_list))
            elif k != 1:
                acct_list.clear()
                for i in range(len(zn_qb_list)):
                    if zn_qb_list[i] == max(zn_qb_list):
                        acct_list.append(i+1)
                if len(acct_list) != 1:
                    print('\nНа шаге №', k, ' можно выбрать между:', sep='')
                    for i in acct_list:
                        print('A', i, sep='')
                    while True:
                        choose_a = inN('Выберите номер стратегии: ', 'Введите число из списка!')
                        if choose_a not in acct_list:
                            print('Неверное число!')
                        else:
                            break
                    numA = choose_a
                else:
                    numA = 1 + zn_qb_list.index(max(zn_qb_list))

                acct_list.clear()
                for i in range(len(zn_pa_list)):
                    if zn_pa_list[i] == min(zn_pa_list):
                        acct_list.append(i + 1)
                if len(acct_list) != 1:
                    print('\nНа шаге №', k, ' можно выбрать между:', sep='')
                    for i in acct_list:
                        print('B', i, sep='')
                    while True:
                        choose_b = inN('Выберите номер стратегии: ', 'Введите число из списка!')
                        if choose_b not in acct_list:
                            print('Неверное число!')
                        else:
                            break
                    numB = choose_b
                else:
                    numB = 1 + zn_pa_list.index(min(zn_pa_list))
            res_tab.extend([str(numA), str(numB)])
            a_summ[numA - 1] += 1
            b_summ[numB - 1] += 1

            pa_list = []
            qb_list = []
            for i in range(m):
                pa_list.append(Rational(a_summ[i], k))
            for i in range(n):
                qb_list.append(Rational(b_summ[i], k))
            res_tab.append('P(' + str(k) + ') = ' + str(pa_list))
            res_tab.append('Q(' + str(k) + ') = ' + str(qb_list))

            zn_pa_list = []
            zn_qb_list = []
            for i in range(n):
                zn_pa_list.append(dot(pa_list, start_tab[:, i]))
            for i in range(m):
                zn_qb_list.append(dot(qb_list, start_tab[i, :]))
            re_a = min(zn_pa_list)
            re_b = max(zn_qb_list)
            res_tab.append(str(re_a))
            res_tab.append(str(re_b))

            print('\nШаг №', k, ':', sep='')
            for i in range(len(zn_pa_list)):
                print('H(P({0}), B{1}) = {2}'.format(k, i+1, zn_pa_list[i]))
            print()
            for i in range(len(zn_qb_list)):
                print('H(A{1}, Q({0}) = {2}'.format(k, i+1, zn_qb_list[i]))


            a_list.append(re_a)
            b_list.append(re_b)
            maxa = max(a_list)
            minb = min(b_list)
            res_tab.extend([str(maxa), str(minb)])

            dk = minb - maxa
            res_tab.append(str(dk))
            if dk < 2*E:
                res_tab.append("<")
                break
            else:
                res_tab.append('>')
            print('\n|{0[0]:^3}|{0[1]:^6}|{0[2]:^6}|{0[3]:^40}|{0[4]:^40}|{0[5]:^7}|{0[6]:^7}|{0[7]:^6}|{0[8]:^6}|{0['
                  '9]:^6}|{0[10]:^5}|'.format(tab))
            for k in range(counter):
                print('|{0:^3}|{1:^6}|{2:^6}|{3:^40}|{4:^40}|{5:^7}|{6:^7}|{7:^6}|{8:^6}|{9:^6}|{10:^5}|'
                      .format(res_tab[k * 11],
                              res_tab[1 + k * 11],
                              res_tab[2 + k * 11],
                              res_tab[3 + k * 11],
                              res_tab[4 + k * 11],
                              res_tab[5 + k * 11],
                              res_tab[6 + k * 11],
                              res_tab[7 + k * 11],
                              res_tab[8 + k * 11],
                              res_tab[9 + k * 11],
                              res_tab[10 + k * 11]))

        print('\n|{0[0]:^3}|{0[1]:^6}|{0[2]:^6}|{0[3]:^40}|{0[4]:^40}|{0[5]:^7}|{0[6]:^7}|{0[7]:^6}|{0[8]:^6}|{0['
              '9]:^6}|{0[10]:^5}|'.format(tab))
        for k in range(counter):
            print('|{0:^3}|{1:^6}|{2:^6}|{3:^40}|{4:^40}|{5:^7}|{6:^7}|{7:^6}|{8:^6}|{9:^6}|{10:^5}|'
                .format(res_tab[k * 11],
                        res_tab[1 + k * 11],
                        res_tab[2 + k * 11],
                        res_tab[3 + k * 11],
                        res_tab[4 + k * 11],
                        res_tab[5 + k * 11],
                        res_tab[6 + k * 11],
                        res_tab[7 + k * 11],
                        res_tab[8 + k * 11],
                        res_tab[9 + k * 11],
                        res_tab[10 + k * 11]))

        return


start = BrownRobinson()
start.starter()
