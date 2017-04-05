from sympy.parsing.sympy_parser import parse_expr

def inFu(text='Введите: ',feedback='Функция задана неверно!'):
        C = False
        while True:
            Z = input(text)
            try:
                Z = parse_expr(Z)
                C = False
            except:
                print(feedback)
                C = True
            if not C:
                return Z
