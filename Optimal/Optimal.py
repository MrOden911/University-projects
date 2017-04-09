# Методы оптимизации
# Текущая версия 1.1

# TODO Оставив функционал выбора переменных функции, ограничить доступ пользователя к коду. Избавиться от "exec".

from math import *

from numpy import dot, array
from numpy.linalg import inv, det
from sympy import diff, Symbol, solve

from odenarium import warprint, inFu, inN0, YorN, inN, invar, inFl, erprint


class Dual_iteration:
    def Starter(self):
        Methods = {1: 'Метод градиентного спуска', 2: 'Метод наискорейшего спуска', 3: 'Метод Ньютона'}
        self.Method = 1
        self.ToMin = False
        self.NumOfIterations = 4
        self.H = 0.1
        self.StartPoint = [0, 0]
        self.DualFunction = None
        while True:
            while True:
                V = 'min' if self.ToMin else 'max'  # !!!
                if self.Method == 1:
                    print('''
Текущие параметры:
1) {0}
2) Стартовая точка {4}
3) К {1}
4) Количество итераций: {2}
5) h = {3}
'''.format(Methods[1], V, self.NumOfIterations, self.H, self.StartPoint))
                elif self.Method == 2:
                    print('''
Текущие параметры:
1) {0}
2) Стартовая точка {3}
3) К {1}
4) Количество итераций: {2}

'''.format(Methods[2], V, self.NumOfIterations, self.StartPoint))
                else:
                    print('''
Текущие параметры:
1) {0}
2) Стартовая точка {1}
'''.format(Methods[3], self.StartPoint))
                if YorN('Изменить параметры? (Yes/No) '):
                    while True:
                        i = inN0('\nВведите номер изменяемого параметра, или "0" для сохранения параметров: ',
                                 "Введен неверный номер!")
                        if i == 0:
                            break
                        elif i == 1:
                            while True:
                                self.Method = inN('''Выберите необходимый метод:
1) Метод градиентного спуска
2) Метод наискорейшего спуска
3) Метод Ньютона
Ваш выбор: ''', 'Введен неверный номер!')
                                if self.Method > 3:
                                    erprint('Введен неверный номер!')
                                else:
                                    break
                        elif i == 3:
                            while True:
                                r = inN('''Выберите направление:
1) min
2) max
Ваш выбор: ''', 'Введен неверный номер!')
                                if r > 2:
                                    erprint('Введен неверный номер!')
                                else:
                                    self.ToMin = r == 1  # !!!
                                    break
                        elif i == 4:
                            self.NumOfIterations = inN('Введите количество итераций: ',
                                                       'Должно быть введено натуральное значение')
                        elif i == 2:
                            self.StartPoint[0] = inFl('Введите стартовое значение x: ', 'Неверный ввод!')
                            self.StartPoint[1] = inFl('Введите стартовое значение y: ', 'Неверный ввод!')
                        elif i == 5:
                            self.H = inFl('Введите значение h: ', 'Неверное значение')
                        else:
                            erprint('Неверный параметр!')

                else:
                    if self.DualFunction is not None:
                        self.ChangeDualFunction()
                    else:
                        self.InputDualFunction()
                    if self.Method == 1 or self.Method == 2:
                        self.FirstMethod()
                    elif self.Method == 3:
                        self.newton()
                    break
            if not YorN("\nПродолжить работу с программой? (Yes/No) "):
                break

    def ChangeDualFunction(self):
        print('Предыдущая функция F({1},{2}) = {0}'.format(self.DualFunction, self.Prx, self.Pry))
        if YorN('Использовать предыдущую функцию? (Yes/No) '):
            return
        else:
            self.InputDualFunction()

    def InputDualFunction(self):
        if not self.InVar():
            return
        warprint('Внимание, при вводе неуказанных переменных возможны ошибочные результаты!')
        while True:
            self.DualFunction = inFu('Введите F({0},{1}) = '.format(self.Prx, self.Pry))
            if self.Prx not in str(self.DualFunction) or self.Pry not in str(self.DualFunction):
                erprint('Одной из заданных переменных нет в функции, повторите ввод.')
            else:
                return

    def InVar(self):
        try:
            if YorN('Использовать стандартные переменные "x" и "y"? (Yes/No) '):
                self.Prx = 'x'
                self.Pry = 'y'
            else:
                warprint(
                    'Вводимые переменные не должны содержать символов кроме цифр и латинских букв, а так же не начинаться с цифр.')
                while True:
                    self.Prx = invar('Первая переменная: ')
                    self.Pry = invar('Вторая переменная: ')
                    if self.Prx == self.Pry:
                        erprint('Введены одинаковые переменные, повторите ввод.')
                    elif self.Prx == 'h' or self.Pry == 'h':
                        erprint('Переменная h уже используется в программе, повторите ввод.')
                    else:
                        break

            return True
        except Exception:
            erprint('Упс, что то пошло не так! В случае повторения ошибки обратитесь к автору программы.')
            return False

    def FirstMethod(self):
        Prx = self.Prx
        Pry = self.Pry
        exec(Prx + '=Symbol(Prx)')
        exec(Pry + '=Symbol(Pry)')
        if not self.CheckMin():
            return
        FUN = self.DualFunction
        Fx = diff(FUN, Prx)
        Fy = diff(FUN, Pry)
        print("""F'{0} = {1}""".format(Prx, Fx))
        print("""F'{0} = {1}""".format(Pry, Fy))
        Table = ['№', Prx, Pry, "F'" + Prx, "F'" + Pry, '||dF||', 'h', 'F({},{})'.format(Prx, Pry)]
        znach_x = self.StartPoint[0]
        znach_y = self.StartPoint[1]
        result_table = [0, round(znach_x, 3), round(znach_y, 3)]
        for i in range(1, int(self.NumOfIterations) + 1):
            exec(Prx + "=znach_x")
            exec(Pry + "=znach_y")
            ANX = znach_x
            ANY = znach_y
            F1 = round(eval(str(Fx)), 3)
            F2 = round(eval(str(Fy)), 3)
            result_table.append(F1)
            result_table.append(F2)
            determinant = round(sqrt(F1 ** 2 + F2 ** 2), 3)
            result_table.append(determinant)
            if self.Method == 1:
                h = self.H
            else:
                h = Symbol('h')
                if self.ToMin:
                    exec(Prx + '=znach_x-h*F1')
                    exec(Pry + '=znach_y-h*F2')
                else:
                    exec(Prx + '=znach_x+h*F1')
                    exec(Pry + '=znach_y+h*F2')
                h = solve(diff(eval(str(FUN)), h))
                h = round(h[0], 3)
            exec(Prx + '=znach_x')
            exec(Pry + "=znach_y")
            result_table.append(h)
            res_f = round(eval(str(FUN)), 3)
            result_table.append(res_f)
            result_table.append(i)
            if self.ToMin:
                znach_x = round(znach_x - h * F1, 3)
                znach_y = round(znach_y - h * F2, 3)
            else:
                znach_x = round(znach_x + h * F1, 3)
                znach_y = round(znach_y + h * F2, 3)
            result_table.append(znach_x)
            result_table.append(znach_y)
            print('''
На шаге №{11}:
{0}(k) = {2}
{1}(k) = {3}
F'{0} = {4}
F'{1} = {5}
||dF|| = {6}
h = {7}
F({0},{1}) = {8}
{0}(k+1) = {9}
{1}(k+1) = {10}
'''.format(Prx, Pry, ANX, ANY, F1, F2, determinant, h, res_f, znach_x, znach_y, i))
        exec(Prx + '=znach_x')
        exec(Pry + '=znach_y')
        print('Таблица:')
        print('|{0[0]:^5}|{0[1]:^7}|{0[2]:^7}|{0[3]:^7}|{0[4]:^7}|{0[5]:^10}|{0[6]:^7}|{0[7]:^8}|'.format(Table))
        print('|{0:^5}|{1:^7}|{2:^7}|'.format(result_table[0], result_table[1], result_table[2]), end='')
        for k in range(3, len(result_table), 8):
            print('''{0:^7}|{1:^7}|{2:^10}|{3:^7}|{4:^8}|
|{5:^5}|{6:^7}|{7:^7}|'''.format(result_table[k], result_table[k + 1], result_table[k + 2], result_table[k + 3],
                                 result_table[k + 4], result_table[k + 5], result_table[k + 6], result_table[k + 7]),
                  end='')
        print()
        ans = {True: 'Наименьшее', False: 'Наибольшее'}
        que = round(eval(str(FUN)), 3)
        warprint('{3} найденное значение функции F({0},{1}) = {2}'.format(Prx, Pry, que, ans[self.ToMin]))

    def CheckMin(self):
        FUN = self.DualFunction
        Prx = self.Prx
        Pry = self.Pry
        exec(Prx + '=Symbol(Prx)')
        exec(Pry + '=Symbol(Pry)')
        exec(Prx + '=self.StartPoint[0]')
        exec(Pry + '=self.StartPoint[1]')
        H = array(([eval(str(diff(FUN, Prx, Prx))), eval(str(diff(FUN, Prx, Pry)))],
                   [eval(str(diff(FUN, Prx, Pry))), eval(str(diff(FUN, Pry, Pry)))]))
        if H[0][0] < 0 < det(H):
            reg = False
        elif H[0][0] > 0 and det(H) > 0:
            reg = True
        else:
            erprint('Невозможно определить направление экстремума для заданной функции!')
            return False
        if reg != self.ToMin:
            erprint('Неверно выбрано направление экстремума (min/max). Замена значения.')
            self.ToMin = reg
            return True

    def newton(self):
        Prx = self.Prx
        Pry = self.Pry
        exec(Prx + '=Symbol(Prx)')
        exec(Pry + '=Symbol(Pry)')
        FUN = self.DualFunction
        XMATRIX = array(([self.StartPoint[0]], [self.StartPoint[0]]))
        print('Начальные точки:', XMATRIX, sep='\n')
        exec(Prx + '=XMATRIX[0]')
        exec(Pry + '=XMATRIX[1]')
        HMATRIX = array(([eval(str(diff(FUN, Prx, Prx))), eval(str(diff(FUN, Prx, Pry)))],
                         [eval(str(diff(FUN, Prx, Pry))), eval(str(diff(FUN, Pry, Pry)))]))
        print('Матрица Гессе:', HMATRIX, sep='\n')
        OPR = det(HMATRIX)
        HMATRIX = inv(HMATRIX) * OPR
        print('Обратная матрица:', '''\n{0} / {1}'''.format(HMATRIX, round(OPR, 3), sep='\n'))
        Fx = diff(FUN, Prx)
        Fy = diff(FUN, Pry)
        print('Производная по {0}: '.format(Prx), Fx)
        print('Производная по {0}: '.format(Pry), Fy)
        PRMATRIX = array(([float(eval(str(Fx)))], [float(eval(str(Fy)))]))
        print('Значения производных:', PRMATRIX, sep='\n')
        XMATRIX = XMATRIX - dot(HMATRIX, PRMATRIX) / OPR
        exec(Prx + '=XMATRIX[0]')
        exec(Pry + "=XMATRIX[1]")
        answer = [round(XMATRIX[0][0], 3), round(XMATRIX[1][0], 3)]
        print('''Новая точка: {0}
F({1},{2}) = {3}'''.format(answer, Prx, Pry, eval(str(FUN))[0]))
        return


t = Dual_iteration()
t.Starter()
